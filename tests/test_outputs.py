"""Verify settlement audit CLI and repaired rollup workflow."""

from __future__ import annotations

import ast
import hashlib
import json
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
FIXTURES = Path("/tests/fixtures/expected_summary.json")
SPEC_DATA = json.loads(REPORT_SPEC_PATH.read_text())
FIXTURE_DATA = json.loads(FIXTURES.read_text())
ISSUE_EVIDENCE_TERMS = SPEC_DATA["diagnosis_report"]["issues_found_item"]["evidence"][
    "required_terms_by_issue"
]
REQUIRED_ISSUE_IDS = SPEC_DATA["diagnosis_report"]["issues_found_item"]["allowed_ids"]
FORBIDDEN_TOKENS = tuple(SPEC_DATA["repair_audit"]["forbidden_executable_tokens"])
REQUIRED_TOKENS = tuple(SPEC_DATA["workflow_repair"]["required_executable_tokens"])
ESCALATION_PRIORITIES = {"risk", "critical"}
PRIORITY_ORDER = ("critical", "debug", "info", "risk")
PRIORITY_RANK = {"debug": 1, "info": 2, "risk": 3, "critical": 4}


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
    return str(value if value is not None else "").strip().lower()


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
    return sorted(deduped.values(), key=lambda row: row["posted_ms"])


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
    }


def _compute_flagged(events: list[dict]) -> list[dict]:
    rows = []
    for event in _canonicalize_events(events):
        if not _is_escalation(event):
            continue
        rows.append(
            {
                "txn_id": event["txn_id"],
                "posted_ms": event["posted_ms"],
                "priority": _normalize_priority(event["priority"]),
                "merchant": _normalize_merchant(event["merchant"]),
                "note": _normalize_note(event["note"]),
            }
        )
    rows.sort(
        key=lambda row: (
            -row["posted_ms"],
            -_priority_rank(row["priority"]),
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
    )


def _flagged_rows(path: Path = FLAGGED_PATH) -> list[dict]:
    rows = []
    for line in path.read_text().splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


@pytest.fixture(scope="module")
def expected() -> dict:
    return FIXTURE_DATA


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
    assert CLI.exists(), f"CLI not found at {CLI}"


def test_dossier_has_context():
    minimum = SPEC_DATA["long_context"]["minimum_line_count"]
    assert len(DOSSIER_PATH.read_text().splitlines()) >= minimum


def test_repair_produces_required_outputs():
    for path in (SUMMARY_PATH, MATRIX_PATH, FLAGGED_PATH, REPAIR_AUDIT_PATH):
        assert path.exists(), f"missing required output: {path}"


def test_diagnosis_schema_repaired(diagnosis: dict):
    for key in ("pipeline_status", "issues_found", "input_stats", "verified_summary", "output_paths"):
        assert key in diagnosis
    assert diagnosis["pipeline_status"] == "repaired"


def test_output_paths_exact(diagnosis: dict):
    paths = diagnosis["output_paths"]
    assert paths["summary_json"] == str(SUMMARY_PATH)
    assert paths["flagged_jsonl"] == str(FLAGGED_PATH)
    assert paths["service_matrix_json"] == str(MATRIX_PATH)


def test_issues_found_exactly_six_allowed_ids(diagnosis: dict):
    assert len(diagnosis["issues_found"]) == 6
    assert {item["id"] for item in diagnosis["issues_found"]} == set(REQUIRED_ISSUE_IDS)


def test_issue_item_required_fields(diagnosis: dict):
    for issue in diagnosis["issues_found"]:
        for key in ("id", "severity", "description", "resolution", "evidence"):
            assert key in issue


def test_issue_evidence(diagnosis: dict):
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
    for issue in diagnosis["issues_found"]:
        quote = _normalize_ws(issue["evidence"]["dossier_quote"])
        assert quote in dossier_text


def test_input_stats(diagnosis: dict, expected: dict):
    stats = diagnosis["input_stats"]
    assert stats["record_count"] == expected["record_count"]
    assert stats["unique_txn_ids"] == expected["unique_ids"]
    assert stats["merchants"] == expected["merchants"]


def test_verified_summary_matches_fixture(diagnosis: dict, expected: dict):
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
    ):
        assert verified[key] == expected[key]
    assert list(verified["priority_counts"].keys()) == list(PRIORITY_ORDER)


def test_summary_computed_from_events(summary: dict):
    assert summary == _compute_summary(_load_events(INPUT_PATH))


def test_service_matrix_matches_fixture(expected: dict):
    matrix = json.loads(MATRIX_PATH.read_text())
    assert matrix == expected["expected_service_matrix"]
    assert matrix == _build_service_matrix(_canonicalize_events(_load_events(INPUT_PATH)))


def test_flagged_computed_from_events(flagged_rows: list[dict]):
    assert flagged_rows == _compute_flagged(_load_events(INPUT_PATH))


def test_flagged_sorted_descending(flagged_rows: list[dict], expected: dict):
    assert [row["txn_id"] for row in flagged_rows] == expected["expected_flagged_ids_desc"]
    assert [row["posted_ms"] for row in flagged_rows] == expected["expected_flagged_ts_ms_desc"]


def test_flagged_priorities(flagged_rows: list[dict]):
    for row in flagged_rows:
        assert row["priority"] in ESCALATION_PRIORITIES


def test_flagged_jsonl_compact_format():
    for line in FLAGGED_PATH.read_text().splitlines():
        if not line.strip():
            continue
        assert ": " not in line
        parsed = json.loads(line)
        assert json.dumps(parsed, separators=(",", ":")) == line


def test_original_snapshot_preserved(expected: dict):
    assert ORIGINAL_PIPELINE.exists()
    digest = hashlib.sha256(ORIGINAL_PIPELINE.read_bytes()).hexdigest()
    assert digest == expected["broken_pipeline_sha256"]
    original = ORIGINAL_PIPELINE.read_text()
    for token in FORBIDDEN_TOKENS:
        assert token in original
    assert ".lower(" not in original


def test_broken_snapshot_produces_wrong_export(expected: dict):
    with tempfile.TemporaryDirectory() as tmp:
        broken = Path(tmp) / "export_report.py"
        out = Path(tmp) / "out"
        shutil.copy(ORIGINAL_PIPELINE, broken)
        result = _run_pipeline(pipeline=broken, output_dir=out)
        assert result.returncode == 0, result.stderr
        summary = json.loads((out / "summary.json").read_text())
        flagged = _flagged_rows(out / "flagged.jsonl")
        assert summary["escalated_count"] == expected["broken_flagged_count"]
        assert [row["txn_id"] for row in flagged] == expected["broken_flagged_ids_asc"]
        assert all(row["posted_ms"] == 0 for row in flagged)


def test_pipeline_patched():
    ast.parse(PIPELINE.read_text())
    code = _executable_text(PIPELINE.read_text())
    for token in FORBIDDEN_TOKENS:
        assert token not in code
    for token in REQUIRED_TOKENS:
        assert token in code


def test_repair_audit(diagnosis: dict, expected: dict, summary: dict):
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
    rerun_dir = tmp_path_factory.mktemp("rerun")
    result = _run_pipeline(output_dir=rerun_dir)
    assert result.returncode == 0, result.stderr
    rerun_summary = json.loads((rerun_dir / "summary.json").read_text())
    rerun_flagged = _flagged_rows(rerun_dir / "flagged.jsonl")
    assert rerun_summary == summary
    assert rerun_flagged == flagged_rows


def test_patched_pipeline_supports_alternate_input(expected: dict, tmp_path_factory):
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
    assert [row["txn_id"] for row in flagged] == alt["flagged_ids_desc"]


def test_cli_diagnose_subcommand(expected: dict, dossier_text: str):
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


def test_repair_supports_custom_output_dir(tmp_path_factory, expected: dict):
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


def test_flagged_sort_tie_breaks_by_priority_then_txn_id():
    events = [
        {
            "txn_id": "c2",
            "posted_ms": 500,
            "priority": "critical",
            "merchant": "m",
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
            "merchant": "m",
            "note": "c1",
            "waived": False,
        },
    ]
    flagged = _compute_flagged(events)
    assert [row["txn_id"] for row in flagged] == ["c1", "c2", "r1"]


def test_pipeline_coerces_posted_ms_and_normalizes_outputs(tmp_path_factory):
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


def test_pipeline_dedupe_tie_break_prefers_non_waived_then_note(tmp_path_factory):
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
