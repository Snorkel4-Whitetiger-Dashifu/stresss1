#!/usr/bin/env python3
"""Export corrected settlement summary and escalation rows."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SCHEMA_VERSION = "settlement-rollup-v2"
ESCALATION_PRIORITIES = {"risk", "critical"}
PRIORITY_ORDER = ("critical", "debug", "info", "risk")
PRIORITY_RANK = {"debug": 1, "info": 2, "risk": 3, "critical": 4}
MERCHANT_ALIASES = {
    "alpha-pay": "alpha",
    "beta-store": "beta",
    "gamma_ops": "gamma",
}


def load_events(path: Path) -> list[dict]:
    return json.loads(path.read_text())


def _normalize_priority(value: object) -> str:
    return str(value if value is not None else "").strip().lower()


def _normalize_merchant(value: object) -> str:
    merchant = str(value if value is not None else "").strip().lower()
    return MERCHANT_ALIASES.get(merchant, merchant)


def _normalize_posted_ms(value: object) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        text = value.strip()
        try:
            return int(text)
        except ValueError:
            return 0
    return 0


def _normalize_note(value: object) -> str:
    return " ".join(str(value if value is not None else "").split())


def _normalize_waived(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "1", "yes"}
    return bool(value)


def _priority_rank(priority: str) -> int:
    return PRIORITY_RANK.get(priority, 0)


def canonicalize_events(events: list[dict]) -> list[dict]:
    deduped: dict[str, dict] = {}
    for event in events:
        normalized = dict(event)
        normalized["posted_ms"] = _normalize_posted_ms(normalized.get("posted_ms", 0))
        normalized["priority"] = _normalize_priority(normalized.get("priority", ""))
        normalized["merchant"] = _normalize_merchant(normalized.get("merchant", ""))
        normalized["waived"] = _normalize_waived(normalized.get("waived", False))
        normalized["note"] = _normalize_note(normalized.get("note", ""))
        txn_id = str(normalized["txn_id"])
        current = deduped.get(txn_id)
        if current is None:
            deduped[txn_id] = normalized
            continue
        replace = False
        if normalized["posted_ms"] > current["posted_ms"]:
            replace = True
        elif normalized["posted_ms"] == current["posted_ms"]:
            if _priority_rank(normalized["priority"]) > _priority_rank(current["priority"]):
                replace = True
            elif _priority_rank(normalized["priority"]) == _priority_rank(current["priority"]):
                if int(_normalize_waived(normalized.get("waived", False))) < int(
                    _normalize_waived(current.get("waived", False))
                ):
                    replace = True
                elif int(_normalize_waived(normalized.get("waived", False))) == int(
                    _normalize_waived(current.get("waived", False))
                ):
                    if _normalize_note(normalized.get("note", "")) > _normalize_note(
                        current.get("note", "")
                    ):
                        replace = True
                    elif _normalize_note(normalized.get("note", "")) == _normalize_note(
                        current.get("note", "")
                    ):
                        if _normalize_merchant(normalized.get("merchant", "")) > _normalize_merchant(
                            current.get("merchant", "")
                        ):
                            replace = True
        if replace:
            deduped[txn_id] = normalized
    return sorted(deduped.values(), key=lambda row: (row["posted_ms"], str(row["txn_id"])))


def is_escalation(event: dict) -> bool:
    if _normalize_waived(event.get("waived", False)):
        return False
    return _normalize_priority(event.get("priority", "")) in ESCALATION_PRIORITIES


def build_service_matrix(events: list[dict]) -> dict[str, dict[str, int]]:
    matrix: dict[str, dict[str, int]] = {}
    for event in events:
        merchant = _normalize_merchant(event.get("merchant", ""))
        priority = _normalize_priority(event.get("priority", ""))
        matrix.setdefault(merchant, {name: 0 for name in PRIORITY_ORDER})
        if priority in matrix[merchant]:
            matrix[merchant][priority] += 1
    return {merchant: matrix[merchant] for merchant in sorted(matrix)}


def export_report(events: list[dict], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    canonical = canonicalize_events(events)

    priority_counts = {priority: 0 for priority in PRIORITY_ORDER}
    merchants: set[str] = set()
    for event in canonical:
        priority = _normalize_priority(event.get("priority", ""))
        if priority in priority_counts:
            priority_counts[priority] += 1
        merchants.add(_normalize_merchant(event.get("merchant", "")))

    escalations = []
    for event in canonical:
        if not is_escalation(event):
            continue
        escalations.append(
            {
                "txn_id": event["txn_id"],
                "posted_ms": event["posted_ms"],
                "priority": _normalize_priority(event["priority"]),
                "merchant": _normalize_merchant(event["merchant"]),
                "note": _normalize_note(event["note"]),
            }
        )
    # Stable multi-pass sort to enforce:
    # posted_ms desc, then priority rank desc, then merchant asc, then txn_id asc.
    escalations.sort(key=lambda row: str(row["txn_id"]))
    escalations.sort(key=lambda row: str(row["merchant"]))
    escalations.sort(key=lambda row: _priority_rank(row["priority"]), reverse=True)
    escalations.sort(key=lambda row: row["posted_ms"], reverse=True)

    summary = {
        "schema_version": SCHEMA_VERSION,
        "raw_record_count": len(events),
        "unique_txn_ids": len({str(event["txn_id"]) for event in events}),
        "total_records": len(canonical),
        "priority_counts": priority_counts,
        "merchants": sorted(merchants),
        "escalated_count": len(escalations),
        "waived_excluded_count": sum(
            1
            for event in canonical
            if _normalize_waived(event.get("waived", False))
            and _normalize_priority(event.get("priority", "")) in ESCALATION_PRIORITIES
        ),
        "canonical_fingerprint": hashlib.sha256(
            "\n".join(
                f"{event['txn_id']}|{event['posted_ms']}|{event['priority']}|{event['merchant']}|"
                f"{event['note']}|{1 if _normalize_waived(event.get('waived', False)) else 0}"
                for event in canonical
            ).encode("utf-8")
        ).hexdigest(),
        "escalation_checksum": hashlib.sha256(
            "\n".join(
                f"{row['txn_id']}|{row['posted_ms']}|{row['priority']}|{row['merchant']}|{row['note']}"
                for row in escalations
            ).encode("utf-8")
        ).hexdigest(),
    }

    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    (output_dir / "service_matrix.json").write_text(
        json.dumps(build_service_matrix(canonical), indent=2) + "\n"
    )
    with (output_dir / "flagged.jsonl").open("w", encoding="utf-8") as handle:
        for row in escalations:
            handle.write(json.dumps(row, separators=(",", ":")) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="/app/data/events.json")
    parser.add_argument("--output-dir", default="/app/output")
    args = parser.parse_args()

    events = load_events(Path(args.input))
    export_report(events, Path(args.output_dir))
    print(f"Wrote report to {args.output_dir}")


if __name__ == "__main__":
    main()
