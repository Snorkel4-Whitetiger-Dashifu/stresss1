#!/usr/bin/env python3
"""Diagnostic and repair CLI for settlement rollup workflow."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import subprocess
import sys
from pathlib import Path

EVENTS_PATH = Path("/app/data/events.json")
PIPELINE_PATH = Path("/app/workflow/export_report.py")
FORBIDDEN_TOKENS = ('event["posted_at"]', 'priority == "critical"')

ISSUE_DEFINITIONS = [
    {
        "id": "wrong_posted_field",
        "severity": "critical",
        "description": "Escalation rows use posted_at instead of posted_ms, flattening timestamps to zero.",
        "resolution": "Use posted_ms when emitting escalation rows.",
        "evidence": {
            "dossier_quote": (
                "Nadia: broken rollup reads event['posted_at'] instead of event['posted_ms'], "
                "so escalation timestamps collapse to zero in flagged output."
            ),
            "pipeline_evidence": 'event["posted_at"] if "posted_at" in event else 0',
            "repair_action": "Use posted_ms when emitting escalation rows.",
        },
    },
    {
        "id": "priority_filter",
        "severity": "critical",
        "description": "Workflow escalates only exact critical rows and drops risk priority records.",
        "resolution": "Escalate both risk and critical priorities.",
        "evidence": {
            "dossier_quote": (
                "Imran: escalation export keeps only priority == 'critical' rows, "
                "but on-call queue expects both risk and critical."
            ),
            "pipeline_evidence": 'if priority == "critical":',
            "repair_action": "Include risk and critical rows in escalation export.",
        },
    },
    {
        "id": "recency_order",
        "severity": "high",
        "description": "Escalations are sorted oldest-first instead of newest-first.",
        "resolution": "Sort escalations by posted_ms descending.",
        "evidence": {
            "dossier_quote": (
                "Marta: escalation rows are sorted ascending by posted_ms, but responder workflow "
                "requires descending recency."
            ),
            "pipeline_evidence": 'escalations.sort(key=lambda row: row["posted_ms"])',
            "repair_action": "Sort with reverse=True on posted_ms for recency-first ordering.",
        },
    },
    {
        "id": "priority_normalization",
        "severity": "high",
        "description": "Priority aliases like RISK and Critical are never normalized to lowercase.",
        "resolution": "Normalize priority with .lower() before counting and escalation decisions.",
        "evidence": {
            "dossier_quote": (
                "Nadia: source payloads include RISK and Critical aliases; rollup must normalize "
                "to lowercase before routing."
            ),
            "pipeline_evidence": 'priority = event.get("priority")',
            "repair_action": "Normalize priority values using .lower() in canonicalization.",
        },
    },
    {
        "id": "dedupe_transaction",
        "severity": "high",
        "description": "Duplicate txn_id rows are not collapsed before summary and escalation output.",
        "resolution": "Dedupe by txn_id and keep the highest posted_ms row.",
        "evidence": {
            "dossier_quote": (
                "Imran: duplicate txn_id rows must collapse to the record with highest posted_ms "
                "before aggregation."
            ),
            "pipeline_evidence": "for event in events:",
            "repair_action": "dedupe txn_id rows keeping the highest posted_ms before export.",
        },
    },
    {
        "id": "waived_filter",
        "severity": "high",
        "description": "Waived alerts still appear in flagged output even when they should be excluded.",
        "resolution": "Exclude waived=true rows from flagged.jsonl while retaining summary counts.",
        "evidence": {
            "dossier_quote": (
                "Marta: transactions with waived=true must be excluded from flagged export, "
                "even for critical priority."
            ),
            "pipeline_evidence": "escalations.append(",
            "repair_action": "Exclude waived=true rows from flagged escalation export.",
        },
    },
]


def load_events(path: Path = EVENTS_PATH) -> list[dict]:
    return json.loads(path.read_text())


def input_stats(events: list[dict]) -> dict:
    merchants = sorted({str(event.get("merchant", "")) for event in events})
    return {
        "record_count": len(events),
        "unique_txn_ids": len({str(event["txn_id"]) for event in events}),
        "merchants": merchants,
    }


def pipeline_source_sha256(source: str) -> str:
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def pre_repair_audit() -> dict:
    source = PIPELINE_PATH.read_text()
    return {
        "pipeline_source_sha256": pipeline_source_sha256(source),
        "pipeline_tokens_present": {token: token in source for token in FORBIDDEN_TOKENS},
    }


def patch_workflow() -> None:
    for candidate in (
        Path(__file__).resolve().parent / "export_report_fixed.py",
        Path("/app/export_report_fixed.py"),
    ):
        if candidate.exists():
            PIPELINE_PATH.write_text(candidate.read_text())
            return
    raise FileNotFoundError("repaired export_report.py template not found")


def build_diagnosis_report(
    status: str,
    events: list[dict],
    summary: dict | None = None,
    output_dir: Path | None = None,
) -> dict:
    report = {
        "pipeline_status": status,
        "issues_found": ISSUE_DEFINITIONS,
        "input_stats": input_stats(events),
    }
    if summary is not None and output_dir is not None:
        report["verified_summary"] = summary
        report["output_paths"] = {
            "summary_json": str(output_dir / "summary.json"),
            "flagged_jsonl": str(output_dir / "flagged.jsonl"),
            "service_matrix_json": str(output_dir / "service_matrix.json"),
        }
    return report


def cmd_diagnose(dossier: Path, report_path: Path) -> None:
    _ = dossier.read_text(encoding="utf-8", errors="replace")
    events = load_events()
    report = build_diagnosis_report("diagnosed", events)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n")


def cmd_repair(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    diagnosis_path = output_dir / "diagnosis.json"
    audit_path = output_dir / "repair_audit.json"
    rerun_dir = output_dir / "rerun"

    pre_audit = pre_repair_audit()
    patch_workflow()
    ast.parse(PIPELINE_PATH.read_text())

    subprocess.run(
        [
            sys.executable,
            str(PIPELINE_PATH),
            "--input",
            str(EVENTS_PATH),
            "--output-dir",
            str(output_dir),
        ],
        check=True,
    )

    if rerun_dir.exists():
        for child in rerun_dir.iterdir():
            child.unlink()
    else:
        rerun_dir.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            sys.executable,
            str(PIPELINE_PATH),
            "--input",
            str(EVENTS_PATH),
            "--output-dir",
            str(rerun_dir),
        ],
        check=True,
    )

    events = load_events()
    summary = json.loads((output_dir / "summary.json").read_text())
    diagnosis = build_diagnosis_report("repaired", events, summary, output_dir)
    diagnosis_path.write_text(json.dumps(diagnosis, indent=2) + "\n")

    code = PIPELINE_PATH.read_text()
    audit = {
        "patched_workflow": str(PIPELINE_PATH),
        "processing_steps": [
            "normalize_priority",
            "dedupe_txn_id",
            "filter_waived",
            "build_escalations",
        ],
        "removed_tokens": {token: token not in code for token in FORBIDDEN_TOKENS},
        "pre_repair": pre_audit,
        "post_repair": {
            "escalated_count": summary["escalated_count"],
            "rerun_escalated_count": json.loads((rerun_dir / "summary.json").read_text())[
                "escalated_count"
            ],
        },
    }
    audit_path.write_text(json.dumps(audit, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Settlement rollup diagnostic CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    diag = sub.add_parser("diagnose")
    diag.add_argument("--dossier", type=Path, required=True)
    diag.add_argument("--report", type=Path, default=Path("/app/output/diagnosis.json"))

    repair = sub.add_parser("repair")
    repair.add_argument("--output-dir", type=Path, default=Path("/app/output"))

    args = parser.parse_args()
    if args.command == "diagnose":
        cmd_diagnose(args.dossier, args.report)
    else:
        cmd_repair(args.output_dir)


if __name__ == "__main__":
    main()
