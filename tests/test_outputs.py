"""Verify settlement audit CLI and repaired rollup workflow."""

from __future__ import annotations

import ast
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest

OUTPUT_DIR = Path("/app/output")
DIAGNOSIS_PATH = OUTPUT_DIR / "diagnosis.json"
SUMMARY_PATH = OUTPUT_DIR / "summary.json"
MATRIX_PATH = OUTPUT_DIR / "service_matrix.json"
FLAGGED_PATH = OUTPUT_DIR / "flagged.jsonl"
REPAIR_AUDIT_PATH = OUTPUT_DIR / "repair_audit.json"
CLI = Path("/app/log_audit.py")
PIPELINE = Path("/app/workflow/export_report.py")
ORIGINAL_PIPELINE = Path("/app/workflow/.export_report.original")
DOSSIER_PATH = Path("/app/incident/export_dossier.md")
INPUT_PATH = Path("/app/data/events.json")
REPORT_SPEC_PATH = Path("/app/docs/report_spec.json")
ALT_INPUT = Path("/tests/fixtures/alt_events.json")
BROKEN_PIPELINE_SHA256 = "08ec3ae69e2aad5b5fe63e582fc2f2473dca126381efb6c8c30183a0c4f25156"
SPEC_DATA = json.loads(REPORT_SPEC_PATH.read_text())
ISSUE_EVIDENCE_TERMS = SPEC_DATA["diagnosis_report"]["issues_found_item"]["evidence"][
    "required_terms_by_issue"
]
REQUIRED_ISSUE_IDS = SPEC_DATA["diagnosis_report"]["issues_found_item"]["allowed_ids"]
FORBIDDEN_TOKENS = tuple(SPEC_DATA["repair_audit"]["forbidden_executable_tokens"])
REQUIRED_TOKENS = tuple(SPEC_DATA["workflow_repair"]["required_executable_tokens"])
ESCALATION_PRIORITIES = {"risk", "critical"}
PRIORITY_ORDER = ("critical", "debug", "info", "risk")
PRIORITY_RANK = {"debug": 1, "info": 2, "risk": 3, "critical": 4}
MERCHANT_ALIASES = {
    "alpha-pay": "alpha",
    "beta-store": "beta",
    "gamma_ops": "gamma",
    "delta-pay": "delta",
}


GUARD_SRC = '''
import builtins
import os
from pathlib import Path

_allowed = {p for p in os.environ.get("VERIFIER_ALLOWED_READS", "").split(os.pathsep) if p}
_blocked_roots = ("/tests", "/solution")

_orig_open = builtins.open
_orig_os_open = os.open
_orig_read_text = Path.read_text
_orig_read_bytes = Path.read_bytes


def _is_blocked(value):
    try:
        resolved = str(Path(value).resolve())
    except Exception:
        return False
    if resolved in _allowed:
        return False
    return any(resolved == root or resolved.startswith(root + "/") for root in _blocked_roots)


def _guarded_open(file, *args, **kwargs):
    if _is_blocked(file):
        raise PermissionError("blocked verifier-tree read: %s" % (file,))
    return _orig_open(file, *args, **kwargs)


def _guarded_os_open(path, *args, **kwargs):
    if _is_blocked(path):
        raise PermissionError("blocked verifier-tree read: %s" % (path,))
    return _orig_os_open(path, *args, **kwargs)


def _guarded_read_text(self, *args, **kwargs):
    if _is_blocked(self):
        raise PermissionError("blocked verifier-tree read: %s" % (self,))
    return _orig_read_text(self, *args, **kwargs)


def _guarded_read_bytes(self, *args, **kwargs):
    if _is_blocked(self):
        raise PermissionError("blocked verifier-tree read: %s" % (self,))
    return _orig_read_bytes(self, *args, **kwargs)


builtins.open = _guarded_open
os.open = _guarded_os_open
Path.read_text = _guarded_read_text
Path.read_bytes = _guarded_read_bytes
'''


def _guarded_env(tmp: str, allowed: tuple[Path, ...] = ()) -> dict[str, str]:
    """Build a subprocess env that blocks /tests and /solution reads.

    Anything in ``allowed`` stays readable, so a pipeline may still consume the
    input file it was explicitly pointed at while remaining unable to rummage
    through the rest of the verifier tree.
    """
    Path(tmp, "sitecustomize.py").write_text(GUARD_SRC)
    env = dict(os.environ)
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{tmp}{os.pathsep}{existing}" if existing else tmp
    env["VERIFIER_ALLOWED_READS"] = os.pathsep.join(
        str(Path(path).resolve()) for path in allowed
    )
    return env


def _normalize_ws(text: str) -> str:
    return " ".join(text.split())


def _executable_text(src: str) -> str:
    docstring_lines: set[int] = set()
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef)):
            continue
        if not node.body:
            continue
        first = node.body[0]
        if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant):
            if isinstance(first.value.value, str):
                end = getattr(first, "end_lineno", first.lineno)
                docstring_lines.update(range(first.lineno, end + 1))

    lines: list[str] = []
    for line_number, line in enumerate(src.splitlines(), start=1):
        if line_number in docstring_lines:
            continue
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if "#" in line:
            line = line.split("#", 1)[0]
        lines.append(line)
    return "\n".join(lines)


def _load_events(path: Path) -> list[dict]:
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


def _replay_lineage(events: list[dict]) -> dict[str, dict[str, int]]:
    grouped: dict[str, list[int]] = {}
    for event in events:
        txn_id = str(event["txn_id"])
        grouped.setdefault(txn_id, []).append(_normalize_posted_ms(event.get("posted_ms", 0)))
    lineage: dict[str, dict[str, int]] = {}
    for txn_id, posted_values in grouped.items():
        replay_depth = max(0, len(posted_values) - 1)
        replay_span_ms = max(posted_values) - min(posted_values) if posted_values else 0
        lineage[txn_id] = {
            "replay_depth": replay_depth,
            "replay_span_ms": replay_span_ms,
        }
    return lineage


def _lineage_pressure_score(replay_depth: int, replay_span_ms: int) -> int:
    return replay_depth * 15 + min(replay_span_ms // 500, 40)


def _canonicalize_events(events: list[dict]) -> list[dict]:
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


def _is_escalation(event: dict) -> bool:
    if _normalize_waived(event.get("waived", False)):
        return False
    return _normalize_priority(event.get("priority", "")) in ESCALATION_PRIORITIES


def _build_service_matrix(events: list[dict]) -> dict[str, dict[str, int]]:
    matrix: dict[str, dict[str, int]] = {}
    for event in events:
        merchant = _normalize_merchant(event.get("merchant", ""))
        priority = _normalize_priority(event.get("priority", ""))
        matrix.setdefault(merchant, {name: 0 for name in PRIORITY_ORDER})
        if priority in matrix[merchant]:
            matrix[merchant][priority] += 1
    return {merchant: matrix[merchant] for merchant in sorted(matrix)}


def _compute_summary(events: list[dict]) -> dict:
    lineage = _replay_lineage(events)
    canonical = _canonicalize_events(events)
    priority_counts = {priority: 0 for priority in PRIORITY_ORDER}
    merchants: set[str] = set()
    escalations = _compute_flagged(events)
    for event in canonical:
        priority = _normalize_priority(event.get("priority", ""))
        if priority in priority_counts:
            priority_counts[priority] += 1
        merchants.add(_normalize_merchant(event.get("merchant", "")))
    return {
        "schema_version": "settlement-rollup-v2",
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
                f"{row['txn_id']}|{row['posted_ms']}|{row['priority']}|{row['merchant']}|"
                f"{row['note']}|{row['replay_depth']}|{row['lineage_pressure_score']}"
                for row in escalations
            ).encode("utf-8")
        ).hexdigest(),
        "max_lineage_pressure_score": max(
            (row["lineage_pressure_score"] for row in escalations), default=0
        ),
        "total_replay_depth": sum(
            lineage[str(event["txn_id"])]["replay_depth"] for event in canonical
        ),
        "replay_lineage_checksum": hashlib.sha256(
            "\n".join(
                f"{event['txn_id']}|{lineage[str(event['txn_id'])]['replay_depth']}|"
                f"{lineage[str(event['txn_id'])]['replay_span_ms']}"
                for event in canonical
            ).encode("utf-8")
        ).hexdigest(),
    }


def _compute_flagged(events: list[dict]) -> list[dict]:
    lineage = _replay_lineage(events)
    rows = []
    for event in _canonicalize_events(events):
        if not _is_escalation(event):
            continue
        txn_id = str(event["txn_id"])
        replay_depth = lineage[txn_id]["replay_depth"]
        replay_span_ms = lineage[txn_id]["replay_span_ms"]
        rows.append(
            {
                "txn_id": event["txn_id"],
                "posted_ms": event["posted_ms"],
                "priority": _normalize_priority(event["priority"]),
                "merchant": _normalize_merchant(event["merchant"]),
                "note": _normalize_note(event["note"]),
                "replay_depth": replay_depth,
                "lineage_pressure_score": _lineage_pressure_score(
                    replay_depth, replay_span_ms
                ),
            }
        )
    rows.sort(
        key=lambda row: (
            -row["posted_ms"],
            -row["lineage_pressure_score"],
            -_priority_rank(row["priority"]),
            str(row["merchant"]),
            str(row["txn_id"]),
        )
    )
    return rows


def _run_pipeline(
    pipeline: Path = PIPELINE,
    input_path: Path = INPUT_PATH,
    output_dir: Path = OUTPUT_DIR,
) -> subprocess.CompletedProcess[str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        return subprocess.run(
            [
                "python3",
                str(pipeline),
                "--input",
                str(input_path),
                "--output-dir",
                str(output_dir),
            ],
            capture_output=True,
            text=True,
            timeout=30,
            env=_guarded_env(tmp, allowed=(input_path,)),
        )


def _flagged_rows(path: Path = FLAGGED_PATH) -> list[dict]:
    rows = []
    for line in path.read_text().splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


@pytest.fixture(scope="module")
def expected() -> dict:
    events = _load_events(INPUT_PATH)
    summary = _compute_summary(events)
    flagged = _compute_flagged(events)
    alternate_events = _load_events(ALT_INPUT)
    alternate_summary = _compute_summary(alternate_events)
    alternate_flagged = _compute_flagged(alternate_events)
    return {
        **summary,
        "record_count": len(events),
        "unique_ids": len({str(event["txn_id"]) for event in events}),
        "expected_service_matrix": _build_service_matrix(
            _canonicalize_events(events)
        ),
        "expected_flagged_ids_desc": [row["txn_id"] for row in flagged],
        "expected_flagged_ts_ms_desc": [row["posted_ms"] for row in flagged],
        "broken_pipeline_sha256": BROKEN_PIPELINE_SHA256,
        "alternate_input": str(ALT_INPUT),
        "alternate_expected": {
            **alternate_summary,
            "flagged_ids_desc": [row["txn_id"] for row in alternate_flagged],
        },
    }


@pytest.fixture(scope="module")
def dossier_text() -> str:
    return _normalize_ws(DOSSIER_PATH.read_text())


@pytest.fixture(scope="module")
def diagnosis() -> dict:
    assert DIAGNOSIS_PATH.exists(), (
        f"Missing {DIAGNOSIS_PATH}. Run: python3 {CLI} repair --output-dir /app/output"
    )
    return json.loads(DIAGNOSIS_PATH.read_text())


@pytest.fixture(scope="module")
def summary(diagnosis: dict) -> dict:
    assert SUMMARY_PATH.exists(), "missing summary.json"
    data = json.loads(SUMMARY_PATH.read_text())
    assert data == diagnosis["verified_summary"]
    return data


@pytest.fixture(scope="module")
def flagged_rows() -> list[dict]:
    assert FLAGGED_PATH.exists(), "missing flagged.jsonl"
    return _flagged_rows()


def test_cli_exists():
    """The agent must create the audit CLI at /app/log_audit.py."""
    assert CLI.exists(), f"CLI not found at {CLI}"


def test_dossier_has_context():
    """The incident dossier must meet the spec's minimum line count for long-context reading."""
    minimum = SPEC_DATA["long_context"]["minimum_line_count"]
    assert len(DOSSIER_PATH.read_text().splitlines()) >= minimum


def test_repair_produces_required_outputs():
    """A repair run writes every required artifact into the output directory."""
    for path in (SUMMARY_PATH, MATRIX_PATH, FLAGGED_PATH, REPAIR_AUDIT_PATH):
        assert path.exists(), f"missing required output: {path}"


def test_diagnosis_schema_repaired(diagnosis: dict):
    """A repair-mode diagnosis.json carries the repaired key set and 'repaired' status."""
    for key in ("pipeline_status", "issues_found", "input_stats", "verified_summary", "output_paths"):
        assert key in diagnosis
    assert diagnosis["pipeline_status"] == "repaired"


def test_output_paths_exact(diagnosis: dict):
    """Repaired diagnosis.json uses the spec's exact output_paths key names, not aliases."""
    paths = diagnosis["output_paths"]
    assert paths["summary_json"] == str(SUMMARY_PATH)
    assert paths["flagged_jsonl"] == str(FLAGGED_PATH)
    assert paths["service_matrix_json"] == str(MATRIX_PATH)


def test_issues_found_exactly_six_allowed_ids(diagnosis: dict):
    """The diagnosis reports every allowed issue id from the spec, and no others."""
    assert len(diagnosis["issues_found"]) == 6
    assert {item["id"] for item in diagnosis["issues_found"]} == set(REQUIRED_ISSUE_IDS)


def test_issue_item_required_fields(diagnosis: dict):
    """Each reported issue carries all spec-required fields."""
    for issue in diagnosis["issues_found"]:
        for key in ("id", "severity", "description", "resolution", "evidence"):
            assert key in issue


def test_issue_evidence(diagnosis: dict):
    """Issue evidence meets the spec's minimum lengths and required substring terms, and quotes the frozen pipeline snapshot verbatim."""
    original_pipeline = ORIGINAL_PIPELINE.read_text()
    issues = {item["id"]: item for item in diagnosis["issues_found"]}
    for issue_id, terms in ISSUE_EVIDENCE_TERMS.items():
        evidence = issues[issue_id]["evidence"]
        for key in ("dossier_quote", "pipeline_evidence", "repair_action"):
            assert key in evidence
            assert len(evidence[key]) >= 10
        assert len(evidence["dossier_quote"]) >= 30
        for term in terms["dossier_quote"]:
            assert term in evidence["dossier_quote"]
        for term in terms["pipeline_evidence"]:
            assert term in evidence["pipeline_evidence"]
        assert evidence["pipeline_evidence"] in original_pipeline
        for term in terms["repair_action"]:
            assert term in evidence["repair_action"]


def test_dossier_quotes_are_verbatim(diagnosis: dict, dossier_text: str):
    """Dossier quotes are verbatim excerpts from the dossier, not paraphrases."""
    for issue in diagnosis["issues_found"]:
        quote = _normalize_ws(issue["evidence"]["dossier_quote"])
        assert quote in dossier_text


def test_input_stats(diagnosis: dict, expected: dict):
    """input_stats reports exactly the spec's fields with values derived from the raw events file."""
    stats = diagnosis["input_stats"]
    assert set(stats) == {"record_count", "unique_txn_ids", "merchants"}
    assert stats["record_count"] == expected["record_count"]
    assert stats["unique_txn_ids"] == expected["unique_ids"]
    assert stats["merchants"] == expected["merchants"]


def test_verified_summary_matches_independent_computation(
    diagnosis: dict, expected: dict
):
    """verified_summary matches a summary computed independently from the input events."""
    verified = diagnosis["verified_summary"]
    for key in (
        "schema_version",
        "raw_record_count",
        "unique_txn_ids",
        "total_records",
        "priority_counts",
        "merchants",
        "escalated_count",
        "waived_excluded_count",
        "canonical_fingerprint",
        "escalation_checksum",
        "max_lineage_pressure_score",
        "total_replay_depth",
        "replay_lineage_checksum",
    ):
        assert verified[key] == expected[key]
    assert list(verified["priority_counts"].keys()) == list(PRIORITY_ORDER)
    assert len(verified["canonical_fingerprint"]) == 64
    assert len(verified["escalation_checksum"]) == 64


def test_summary_computed_from_events(summary: dict):
    """summary.json is derived from the input events rather than hard-coded."""
    assert summary == _compute_summary(_load_events(INPUT_PATH))


def test_service_matrix_matches_independent_computation(expected: dict):
    """service_matrix.json is a flat merchant-to-priority-count map computed from canonical rows."""
    matrix = json.loads(MATRIX_PATH.read_text())
    assert matrix == expected["expected_service_matrix"]
    assert matrix == _build_service_matrix(_canonicalize_events(_load_events(INPUT_PATH)))


def test_flagged_computed_from_events(flagged_rows: list[dict]):
    """flagged.jsonl is derived from the input events rather than hard-coded."""
    assert flagged_rows == _compute_flagged(_load_events(INPUT_PATH))


def test_flagged_sorted_descending(flagged_rows: list[dict], expected: dict):
    """Flagged rows appear in the spec's required sort order."""
    assert [row["txn_id"] for row in flagged_rows] == expected["expected_flagged_ids_desc"]
    assert [row["posted_ms"] for row in flagged_rows] == expected["expected_flagged_ts_ms_desc"]


def test_flagged_priorities(flagged_rows: list[dict]):
    """Flagged rows are escalations only and carry integer replay lineage fields."""
    for row in flagged_rows:
        assert row["priority"] in ESCALATION_PRIORITIES
        for key in ("replay_depth", "lineage_pressure_score"):
            assert key in row
            assert isinstance(row[key], int)


def test_flagged_jsonl_compact_format():
    """flagged.jsonl uses compact JSON separators with no space after the colon."""
    for line in FLAGGED_PATH.read_text().splitlines():
        if not line.strip():
            continue
        assert ": " not in line
        parsed = json.loads(line)
        assert json.dumps(parsed, separators=(",", ":")) == line


def test_original_snapshot_preserved(expected: dict):
    """The frozen pre-repair pipeline snapshot is left byte-for-byte untouched."""
    assert ORIGINAL_PIPELINE.exists()
    digest = hashlib.sha256(ORIGINAL_PIPELINE.read_bytes()).hexdigest()
    assert digest == expected["broken_pipeline_sha256"]
    original = ORIGINAL_PIPELINE.read_text()
    for token in FORBIDDEN_TOKENS:
        assert token in original
    assert ".lower(" not in original


def test_broken_snapshot_produces_wrong_export(expected: dict):
    """The original pipeline genuinely produces wrong output, so the task is not already solved."""
    with tempfile.TemporaryDirectory() as tmp:
        broken = Path(tmp) / "export_report.py"
        out = Path(tmp) / "out"
        shutil.copy(ORIGINAL_PIPELINE, broken)
        result = _run_pipeline(pipeline=broken, output_dir=out)
        assert result.returncode == 0, result.stderr
        summary = json.loads((out / "summary.json").read_text())
        flagged = _flagged_rows(out / "flagged.jsonl")
        assert summary != _compute_summary(_load_events(INPUT_PATH))
        assert flagged != _compute_flagged(_load_events(INPUT_PATH))
        assert all(row["posted_ms"] == 0 for row in flagged)


def test_pipeline_patched():
    """The patched pipeline parses, drops every forbidden token, and gains the required repair markers."""
    ast.parse(PIPELINE.read_text())
    code = _executable_text(PIPELINE.read_text())
    for token in FORBIDDEN_TOKENS:
        assert token not in code
    for token in REQUIRED_TOKENS:
        assert token in code


def test_repaired_sources_do_not_reference_verifier_artifacts():
    """Repaired sources never reference the verifier or solution trees."""
    for source_path in (PIPELINE, CLI):
        source = source_path.read_text()
        for token in (
            "/tests",
            "/solution",
            "expected_summary.json",
            "test_outputs.py",
        ):
            assert token not in source


def test_repair_runtime_does_not_read_verifier_trees():
    """Repair must not read from /tests or /solution at runtime."""
    with tempfile.TemporaryDirectory() as tmp:
        output_dir = Path(tmp) / "repair-output"
        env = _guarded_env(tmp)
        result = subprocess.run(
            [
                "python3",
                str(CLI),
                "repair",
                "--output-dir",
                str(output_dir),
            ],
            capture_output=True,
            text=True,
            timeout=60,
            env=env,
        )
        assert result.returncode == 0, result.stderr
        assert (output_dir / "summary.json").exists()


def test_repair_audit(diagnosis: dict, expected: dict, summary: dict):
    """repair_audit.json records pre-repair state before patching and post-repair counts that agree with the summary."""
    audit = json.loads(REPAIR_AUDIT_PATH.read_text())
    code = _executable_text(PIPELINE.read_text())
    assert audit["patched_workflow"] == str(PIPELINE)
    assert audit["processing_steps"] == SPEC_DATA["repair_audit"]["processing_steps"]
    assert audit["removed_tokens"] == {token: token not in code for token in FORBIDDEN_TOKENS}
    assert all(audit["removed_tokens"].values())
    assert audit["pre_repair"]["pipeline_source_sha256"] == expected["broken_pipeline_sha256"]
    assert audit["pre_repair"]["pipeline_tokens_present"] == {token: True for token in FORBIDDEN_TOKENS}
    assert audit["post_repair"]["escalated_count"] == summary["escalated_count"]
    assert audit["post_repair"]["rerun_escalated_count"] == summary["escalated_count"]


def test_pipeline_reruns_idempotently(summary: dict, flagged_rows: list[dict], tmp_path_factory):
    """Rerunning the patched pipeline on the same input reproduces identical output."""
    rerun_dir = tmp_path_factory.mktemp("rerun")
    result = _run_pipeline(output_dir=rerun_dir)
    assert result.returncode == 0, result.stderr
    rerun_summary = json.loads((rerun_dir / "summary.json").read_text())
    rerun_flagged = _flagged_rows(rerun_dir / "flagged.jsonl")
    assert rerun_summary == summary
    assert rerun_flagged == flagged_rows


def test_patched_pipeline_supports_alternate_input(expected: dict, tmp_path_factory):
    """The patched pipeline computes correct results for an input file it has never seen."""
    alt_dir = tmp_path_factory.mktemp("alt")
    alt_input = Path(expected["alternate_input"])
    result = _run_pipeline(input_path=alt_input, output_dir=alt_dir)
    assert result.returncode == 0, result.stderr
    summary = json.loads((alt_dir / "summary.json").read_text())
    flagged = _flagged_rows(alt_dir / "flagged.jsonl")
    events = _load_events(alt_input)
    assert summary == _compute_summary(events)
    assert flagged == _compute_flagged(events)
    alt = expected["alternate_expected"]
    assert summary["raw_record_count"] == alt["raw_record_count"]
    assert summary["escalated_count"] == alt["escalated_count"]
    assert summary["waived_excluded_count"] == alt["waived_excluded_count"]
    assert summary["canonical_fingerprint"] == alt["canonical_fingerprint"]
    assert summary["escalation_checksum"] == alt["escalation_checksum"]
    assert [row["txn_id"] for row in flagged] == alt["flagged_ids_desc"]


def test_cli_diagnose_subcommand(expected: dict, dossier_text: str):
    """Diagnose mode writes a 'diagnosed' report and omits the repair-only keys."""
    report = OUTPUT_DIR / "diagnosis_redundant.json"
    if report.exists():
        report.unlink()
    result = subprocess.run(
        [
            "python3",
            str(CLI),
            "diagnose",
            "--dossier",
            str(DOSSIER_PATH),
            "--report",
            str(report),
        ],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert report.exists(), f"diagnose failed (rc={result.returncode}): {result.stderr}"
    data = json.loads(report.read_text())
    assert data["pipeline_status"] == "diagnosed"
    assert "input_stats" in data
    assert data["input_stats"]["record_count"] == expected["record_count"]
    assert data["input_stats"]["unique_txn_ids"] == expected["unique_ids"]
    assert data["input_stats"]["merchants"] == expected["merchants"]
    for key in ("verified_summary", "output_paths"):
        assert key not in data
    assert {item["id"] for item in data["issues_found"]} == set(REQUIRED_ISSUE_IDS)
    for issue in data["issues_found"]:
        for key in ("id", "severity", "description", "resolution", "evidence"):
            assert key in issue
        for key in ("dossier_quote", "pipeline_evidence", "repair_action"):
            assert key in issue["evidence"]
            assert len(issue["evidence"][key]) >= 10
        quote = _normalize_ws(issue["evidence"]["dossier_quote"])
        assert quote in dossier_text


def test_diagnose_rejects_separate_input_flag(tmp_path_factory):
    """Diagnose rejects an --input flag with the argparse 'unrecognized arguments' error."""
    report = tmp_path_factory.mktemp("diagnose-interface") / "diagnosis.json"
    result = subprocess.run(
        [
            "python3",
            str(CLI),
            "diagnose",
            "--dossier",
            str(DOSSIER_PATH),
            "--report",
            str(report),
            "--input",
            str(INPUT_PATH),
        ],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode != 0
    assert "unrecognized arguments: --input" in result.stderr
    assert not report.exists()


def test_repair_supports_custom_output_dir(tmp_path_factory, expected: dict):
    """Repair honours a custom --output-dir and records those paths in the diagnosis."""
    custom_dir = tmp_path_factory.mktemp("custom_output")
    current = PIPELINE.read_text()
    try:
        shutil.copy(ORIGINAL_PIPELINE, PIPELINE)
        result = subprocess.run(
            ["python3", str(CLI), "repair", "--output-dir", str(custom_dir)],
            capture_output=True,
            text=True,
            timeout=60,
        )
        assert result.returncode == 0, result.stderr
        summary = json.loads((custom_dir / "summary.json").read_text())
        flagged = _flagged_rows(custom_dir / "flagged.jsonl")
        diagnosis = json.loads((custom_dir / "diagnosis.json").read_text())
        assert summary == _compute_summary(_load_events(INPUT_PATH))
        assert flagged == _compute_flagged(_load_events(INPUT_PATH))
        assert diagnosis["output_paths"]["summary_json"] == str(custom_dir / "summary.json")
        assert diagnosis["output_paths"]["flagged_jsonl"] == str(custom_dir / "flagged.jsonl")
        assert diagnosis["output_paths"]["service_matrix_json"] == str(custom_dir / "service_matrix.json")
        assert summary["escalated_count"] == expected["escalated_count"]
    finally:
        PIPELINE.write_text(current)


def test_dedupe_tie_break_priority_and_note():
    """On a posted_ms tie, dedupe prefers higher priority rank, then the larger normalized note."""
    events = [
        {
            "txn_id": "x1",
            "posted_ms": 100,
            "priority": "info",
            "merchant": "Alpha ",
            "note": "aaa",
            "waived": False,
        },
        {
            "txn_id": "x1",
            "posted_ms": 100,
            "priority": "RISK",
            "merchant": "alpha",
            "note": "bbb",
            "waived": False,
        },
        {
            "txn_id": "x1",
            "posted_ms": 100,
            "priority": "risk",
            "merchant": "alpha",
            "note": "zzz",
            "waived": False,
        },
    ]
    canonical = _canonicalize_events(events)
    assert len(canonical) == 1
    assert canonical[0]["priority"] == "risk"
    assert canonical[0]["note"] == "zzz"
    assert canonical[0]["merchant"] == "alpha"


def test_waived_string_normalization_excludes_escalation():
    """Waived-like strings are coerced to true and excluded from escalations."""
    events = [
        {
            "txn_id": "w1",
            "posted_ms": 100,
            "priority": "critical",
            "merchant": "beta",
            "note": "x",
            "waived": "true",
        },
        {
            "txn_id": "w2",
            "posted_ms": 110,
            "priority": "risk",
            "merchant": "beta",
            "note": "y",
            "waived": "1",
        },
        {
            "txn_id": "w3",
            "posted_ms": 120,
            "priority": "critical",
            "merchant": "beta",
            "note": "z",
            "waived": False,
        },
    ]
    flagged = _compute_flagged(events)
    assert [row["txn_id"] for row in flagged] == ["w3"]


def test_flagged_sort_tie_breaks_by_priority_then_merchant_then_txn_id():
    """Flagged ties fall back to priority rank, then merchant, then txn_id."""
    events = [
        {
            "txn_id": "c2",
            "posted_ms": 500,
            "priority": "critical",
            "merchant": "zzz",
            "note": "c2",
            "waived": False,
        },
        {
            "txn_id": "r1",
            "posted_ms": 500,
            "priority": "risk",
            "merchant": "m",
            "note": "r1",
            "waived": False,
        },
        {
            "txn_id": "c1",
            "posted_ms": 500,
            "priority": "critical",
            "merchant": "aaa",
            "note": "c1",
            "waived": False,
        },
    ]
    flagged = _compute_flagged(events)
    assert [row["txn_id"] for row in flagged] == ["c1", "c2", "r1"]


def test_pipeline_coerces_posted_ms_and_normalizes_outputs(tmp_path_factory):
    """The pipeline coerces posted_ms, normalizes priority, merchant and note, and honours waived strings."""
    events = [
        {
            "txn_id": "p1",
            "posted_ms": " 200 ",
            "priority": " CRITICAL ",
            "merchant": " Acme ",
            "note": "  first  note ",
            "waived": "no",
        },
        {
            "txn_id": "p2",
            "posted_ms": "not-a-number",
            "priority": "risk",
            "merchant": "acme",
            "note": "second",
            "waived": False,
        },
        {
            "txn_id": "p3",
            "posted_ms": 150,
            "priority": "risk",
            "merchant": "acme",
            "note": "waived row",
            "waived": "yes",
        },
    ]
    input_path = tmp_path_factory.mktemp("coerce") / "events.json"
    input_path.write_text(json.dumps(events))
    out_dir = tmp_path_factory.mktemp("coerce_out")
    result = _run_pipeline(input_path=input_path, output_dir=out_dir)
    assert result.returncode == 0, result.stderr

    summary = json.loads((out_dir / "summary.json").read_text())
    flagged = _flagged_rows(out_dir / "flagged.jsonl")
    matrix = json.loads((out_dir / "service_matrix.json").read_text())

    assert summary["merchants"] == ["acme"]
    assert summary["escalated_count"] == 2
    assert summary["waived_excluded_count"] == 1
    assert [row["txn_id"] for row in flagged] == ["p1", "p2"]
    assert [row["posted_ms"] for row in flagged] == [200, 0]
    assert flagged[0]["note"] == "first note"
    assert matrix == {"acme": {"critical": 1, "debug": 0, "info": 0, "risk": 2}}


def test_merchant_alias_normalization_is_exercised(tmp_path_factory):
    """Merchant aliases collapse to their canonical names in the summary and matrix."""
    events = [
        {
            "txn_id": "m1",
            "posted_ms": 100,
            "priority": "critical",
            "merchant": " Alpha-Pay ",
            "note": "a",
            "waived": False,
        },
        {
            "txn_id": "m2",
            "posted_ms": 200,
            "priority": "risk",
            "merchant": "beta-store",
            "note": "b",
            "waived": False,
        },
        {
            "txn_id": "m3",
            "posted_ms": 300,
            "priority": "info",
            "merchant": "gamma_ops",
            "note": "c",
            "waived": False,
        },
    ]
    input_path = tmp_path_factory.mktemp("merchant_alias") / "events.json"
    input_path.write_text(json.dumps(events))
    out_dir = tmp_path_factory.mktemp("merchant_alias_out")
    result = _run_pipeline(input_path=input_path, output_dir=out_dir)
    assert result.returncode == 0, result.stderr
    summary = json.loads((out_dir / "summary.json").read_text())
    matrix = json.loads((out_dir / "service_matrix.json").read_text())
    assert summary["merchants"] == ["alpha", "beta", "gamma"]
    assert matrix == {
        "alpha": {"critical": 1, "debug": 0, "info": 0, "risk": 0},
        "beta": {"critical": 0, "debug": 0, "info": 0, "risk": 1},
        "gamma": {"critical": 0, "debug": 0, "info": 1, "risk": 0},
    }


def test_pipeline_dedupe_tie_break_prefers_non_waived_then_note(tmp_path_factory):
    """On a full tie, dedupe prefers a non-waived row, then the larger normalized note."""
    events = [
        {
            "txn_id": "d1",
            "posted_ms": 100,
            "priority": "risk",
            "merchant": "m",
            "note": "zzz",
            "waived": "yes",
        },
        {
            "txn_id": "d1",
            "posted_ms": 100,
            "priority": "risk",
            "merchant": "m",
            "note": "aaa",
            "waived": False,
        },
        {
            "txn_id": "d1",
            "posted_ms": 100,
            "priority": "risk",
            "merchant": "m",
            "note": "bbb",
            "waived": "0",
        },
    ]
    input_path = tmp_path_factory.mktemp("dedupe") / "events.json"
    input_path.write_text(json.dumps(events))
    out_dir = tmp_path_factory.mktemp("dedupe_out")
    result = _run_pipeline(input_path=input_path, output_dir=out_dir)
    assert result.returncode == 0, result.stderr

    flagged = _flagged_rows(out_dir / "flagged.jsonl")
    summary = json.loads((out_dir / "summary.json").read_text())

    assert summary["total_records"] == 1
    assert summary["waived_excluded_count"] == 0
    assert [row["txn_id"] for row in flagged] == ["d1"]
    assert flagged[0]["note"] == "bbb"


def test_canonical_fingerprint_uses_posted_ms_then_txn_id_order(tmp_path_factory):
    """The canonical fingerprint hashes rows ordered by posted_ms, then txn_id."""
    events = [
        {
            "txn_id": "z9",
            "posted_ms": 500,
            "priority": "critical",
            "merchant": "m",
            "note": "late",
            "waived": False,
        },
        {
            "txn_id": "a1",
            "posted_ms": 100,
            "priority": "info",
            "merchant": "m",
            "note": "early",
            "waived": False,
        },
        {
            "txn_id": "c3",
            "posted_ms": 500,
            "priority": "risk",
            "merchant": "m",
            "note": "same-ms-a",
            "waived": False,
        },
    ]
    input_path = tmp_path_factory.mktemp("fingerprint_order") / "events.json"
    input_path.write_text(json.dumps(events))
    out_dir = tmp_path_factory.mktemp("fingerprint_order_out")
    result = _run_pipeline(input_path=input_path, output_dir=out_dir)
    assert result.returncode == 0, result.stderr

    summary = json.loads((out_dir / "summary.json").read_text())
    canonical = _canonicalize_events(events)
    assert [(row["posted_ms"], row["txn_id"]) for row in canonical] == [
        (100, "a1"),
        (500, "c3"),
        (500, "z9"),
    ]
    expected_fingerprint = hashlib.sha256(
        "\n".join(
            f"{row['txn_id']}|{row['posted_ms']}|{row['priority']}|{row['merchant']}|"
            f"{row['note']}|{1 if _normalize_waived(row.get('waived', False)) else 0}"
            for row in canonical
        ).encode("utf-8")
    ).hexdigest()
    assert summary["canonical_fingerprint"] == expected_fingerprint


def test_primary_data_does_not_mask_canonical_order():
    """The shipped events file distinguishes canonical order from plain txn_id order."""
    events = _load_events(INPUT_PATH)
    canonical = _canonicalize_events(events)
    by_txn = [row["txn_id"] for row in sorted(canonical, key=lambda row: str(row["txn_id"]))]
    by_canonical = [row["txn_id"] for row in canonical]
    assert by_canonical != by_txn


def test_escalation_checksum_matches_final_flagged_order(tmp_path_factory):
    """The escalation checksum hashes flagged rows in their final output order."""
    events = [
        {
            "txn_id": "e1",
            "posted_ms": 900,
            "priority": "critical",
            "merchant": "beta-store",
            "note": "top",
            "waived": False,
        },
        {
            "txn_id": "e2",
            "posted_ms": 900,
            "priority": "critical",
            "merchant": "alpha-pay",
            "note": "top",
            "waived": False,
        },
    ]
    input_path = tmp_path_factory.mktemp("escalation_checksum") / "events.json"
    input_path.write_text(json.dumps(events))
    out_dir = tmp_path_factory.mktemp("escalation_checksum_out")
    result = _run_pipeline(input_path=input_path, output_dir=out_dir)
    assert result.returncode == 0, result.stderr
    summary = json.loads((out_dir / "summary.json").read_text())
    flagged = _flagged_rows(out_dir / "flagged.jsonl")
    expected = hashlib.sha256(
        "\n".join(
            f"{row['txn_id']}|{row['posted_ms']}|{row['priority']}|{row['merchant']}|"
            f"{row['note']}|{row['replay_depth']}|{row['lineage_pressure_score']}"
            for row in flagged
        ).encode("utf-8")
    ).hexdigest()
    assert summary["escalation_checksum"] == expected


def test_replay_lineage_pressure_breaks_posted_ms_ties(tmp_path_factory):
    """When posted_ms ties, higher replay lineage pressure ranks earlier."""
    events = [
        {
            "txn_id": "r1",
            "posted_ms": 1000,
            "priority": "critical",
            "merchant": "alpha",
            "note": "single",
            "waived": False,
        },
        {
            "txn_id": "r2",
            "posted_ms": 1000,
            "priority": "critical",
            "merchant": "beta",
            "note": "replay-a",
            "waived": False,
        },
        {
            "txn_id": "r2",
            "posted_ms": 1000,
            "priority": "critical",
            "merchant": "beta",
            "note": "replay-b",
            "waived": False,
        },
        {
            "txn_id": "r3",
            "posted_ms": 500,
            "priority": "info",
            "merchant": "gamma",
            "note": "shadow",
            "waived": False,
        },
        {
            "txn_id": "r3",
            "posted_ms": 1000,
            "priority": "critical",
            "merchant": "gamma",
            "note": "wide-replay",
            "waived": False,
        },
    ]
    input_path = tmp_path_factory.mktemp("replay_lineage") / "events.json"
    input_path.write_text(json.dumps(events))
    out_dir = tmp_path_factory.mktemp("replay_lineage_out")
    result = _run_pipeline(input_path=input_path, output_dir=out_dir)
    assert result.returncode == 0, result.stderr
    flagged = _flagged_rows(out_dir / "flagged.jsonl")
    assert [row["txn_id"] for row in flagged] == ["r3", "r2", "r1"]
    assert flagged[0]["lineage_pressure_score"] > flagged[1]["lineage_pressure_score"]
    summary = json.loads((out_dir / "summary.json").read_text())
    assert summary["total_replay_depth"] == 2
    assert summary["max_lineage_pressure_score"] == flagged[0]["lineage_pressure_score"]


def test_lineage_pressure_span_contribution_is_capped(tmp_path_factory):
    """The span term of lineage pressure is capped at 40 points per the final dossier ruling."""
    events = [
        {
            "txn_id": "w1",
            "posted_ms": 1000,
            "priority": "critical",
            "merchant": "alpha",
            "note": "replay-open",
            "waived": False,
        },
        {
            "txn_id": "w1",
            "posted_ms": 31000,
            "priority": "critical",
            "merchant": "alpha",
            "note": "replay-close",
            "waived": False,
        },
        {
            "txn_id": "w2",
            "posted_ms": 31000,
            "priority": "critical",
            "merchant": "beta",
            "note": "single",
            "waived": False,
        },
    ]
    input_path = tmp_path_factory.mktemp("span_cap") / "events.json"
    input_path.write_text(json.dumps(events))
    out_dir = tmp_path_factory.mktemp("span_cap_out")
    result = _run_pipeline(input_path=input_path, output_dir=out_dir)
    assert result.returncode == 0, result.stderr
    flagged = _flagged_rows(out_dir / "flagged.jsonl")
    scores = {row["txn_id"]: row["lineage_pressure_score"] for row in flagged}
    # span 30000ms -> 30000 // 500 = 60, capped at 40; depth 1 adds 15.
    assert scores["w1"] == 55
    assert scores["w2"] == 0
    summary = json.loads((out_dir / "summary.json").read_text())
    assert summary["max_lineage_pressure_score"] == 55


def test_merchant_alias_fold_covers_the_delta_acquirer(tmp_path_factory):
    """The acquirer fold table folds delta-pay, not only the original three aliases."""
    events = [
        {
            "txn_id": "d1",
            "posted_ms": 1000,
            "priority": "critical",
            "merchant": "delta-pay",
            "note": "onboarded acquirer",
            "waived": False,
        },
        {
            "txn_id": "d2",
            "posted_ms": 900,
            "priority": "critical",
            "merchant": "delta",
            "note": "existing label",
            "waived": False,
        },
    ]
    input_path = tmp_path_factory.mktemp("delta_alias") / "events.json"
    input_path.write_text(json.dumps(events))
    out_dir = tmp_path_factory.mktemp("delta_alias_out")
    result = _run_pipeline(input_path=input_path, output_dir=out_dir)
    assert result.returncode == 0, result.stderr
    flagged = _flagged_rows(out_dir / "flagged.jsonl")
    # delta-pay folds to delta, so both rows settle under the one merchant; a
    # pipeline built only from the three-alias table leaves them split.
    assert {row["merchant"] for row in flagged} == {"delta"}


def test_pipeline_read_guard_blocks_verifier_tree_access(tmp_path_factory):
    """The pipeline read-guard bites: a pipeline reaching into /tests is denied."""
    rogue = tmp_path_factory.mktemp("rogue") / "export_report.py"
    rogue.write_text(
        "from pathlib import Path\n"
        "Path('/tests/test_outputs.py').read_text()\n"
    )
    result = _run_pipeline(
        pipeline=rogue, output_dir=tmp_path_factory.mktemp("rogue_out")
    )
    assert result.returncode != 0
    assert "blocked verifier-tree read" in result.stderr
