#!/usr/bin/env python3
"""Export corrected settlement summary and escalation rows."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

SCHEMA_VERSION = "settlement-rollup-v2"
ESCALATION_PRIORITIES = {"risk", "critical"}
PRIORITY_ORDER = ("critical", "debug", "info", "risk")


def load_events(path: Path) -> list[dict]:
    return json.loads(path.read_text())


def canonicalize_events(events: list[dict]) -> list[dict]:
    deduped: dict[str, dict] = {}
    for event in events:
        normalized = dict(event)
        normalized["priority"] = str(normalized.get("priority", "")).lower()
        txn_id = str(normalized["txn_id"])
        current = deduped.get(txn_id)
        if current is None or normalized["posted_ms"] > current["posted_ms"]:
            deduped[txn_id] = normalized
    return sorted(deduped.values(), key=lambda row: row["posted_ms"])


def is_escalation(event: dict) -> bool:
    if event.get("waived") is True:
        return False
    return event["priority"] in ESCALATION_PRIORITIES


def build_service_matrix(events: list[dict]) -> dict[str, dict[str, int]]:
    matrix: dict[str, dict[str, int]] = {}
    for event in events:
        merchant = str(event.get("merchant", ""))
        priority = str(event.get("priority", ""))
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
        priority = str(event.get("priority", ""))
        if priority in priority_counts:
            priority_counts[priority] += 1
        merchants.add(str(event.get("merchant", "")))

    escalations = []
    for event in canonical:
        if not is_escalation(event):
            continue
        escalations.append(
            {
                "txn_id": event["txn_id"],
                "posted_ms": event["posted_ms"],
                "priority": event["priority"],
                "merchant": event["merchant"],
                "note": event["note"],
            }
        )
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
            if event.get("waived") is True and event["priority"] in ESCALATION_PRIORITIES
        ),
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
