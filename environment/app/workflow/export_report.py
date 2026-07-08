#!/usr/bin/env python3
"""Broken settlement rollup workflow used for repair task."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

SCHEMA_VERSION = "settlement-rollup-v2"


def load_events(path: Path) -> list[dict]:
    return json.loads(path.read_text())


def export_report(events: list[dict], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    priority_counts = {name: 0 for name in ("critical", "debug", "info", "risk")}
    merchants: set[str] = set()
    for event in events:
        priority = str(event.get("priority", ""))
        if priority in priority_counts:
            priority_counts[priority] += 1
        merchants.add(str(event.get("merchant", "")))

    escalations = []
    for event in events:
        priority = event.get("priority")
        if priority == "critical":
            escalations.append(
                {
                    "txn_id": event["txn_id"],
                    "posted_ms": event["posted_at"] if "posted_at" in event else 0,
                    "priority": event["priority"],
                    "merchant": event["merchant"],
                    "note": event["note"],
                }
            )

    escalations.sort(key=lambda row: row["posted_ms"])

    summary = {
        "schema_version": SCHEMA_VERSION,
        "raw_record_count": len(events),
        "unique_txn_ids": len({str(event["txn_id"]) for event in events}),
        "total_records": len(events),
        "priority_counts": priority_counts,
        "merchants": sorted(merchants),
        "escalated_count": len(escalations),
        "waived_excluded_count": 0,
    }

    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    (output_dir / "service_matrix.json").write_text(json.dumps({}, indent=2) + "\n")
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
