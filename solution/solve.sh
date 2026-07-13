#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cp "${SCRIPT_DIR}/log_audit.py" /app/log_audit.py
cp "${SCRIPT_DIR}/export_report_fixed.py" /app/export_report_fixed.py
chmod +x /app/log_audit.py
mkdir -p /app/output /app/audit

# Some evaluators may run oracle without Dockerfile snapshot bootstrap.
# If snapshot is missing or stale, refresh from current broken workflow.
if [ ! -f /app/workflow/.export_report.original ]; then
  cp /app/workflow/export_report.py /app/workflow/.export_report.original
  chmod a-w /app/workflow/.export_report.original
elif python3 - <<'PY'
from pathlib import Path
original = Path("/app/workflow/.export_report.original").read_text()
needed = ['event["posted_at"]', 'priority == "critical"']
raise SystemExit(0 if not all(token in original for token in needed) else 1)
PY
then
  if python3 - <<'PY'
from pathlib import Path
workflow = Path("/app/workflow/export_report.py").read_text()
needed = ['event["posted_at"]', 'priority == "critical"']
raise SystemExit(0 if all(token in workflow for token in needed) else 1)
PY
  then
    chmod u+w /app/workflow/.export_report.original
    cp /app/workflow/export_report.py /app/workflow/.export_report.original
    chmod a-w /app/workflow/.export_report.original
  fi
fi

python3 /app/log_audit.py diagnose \
  --dossier /app/incident/export_dossier.md \
  --report /app/audit/diagnosis.json

python3 /app/log_audit.py repair --output-dir /app/output

cp /app/output/repair_audit.json /app/audit/repair_audit.json
