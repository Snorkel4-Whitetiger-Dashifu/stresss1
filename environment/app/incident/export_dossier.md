# Settlement Rollup Incident Dossier
Mercury Payments Ops - escalation bridge archive (2026-Q1 through 2026-Q2).

## Executive Summary
Settlement rollup export has been unstable since early 2026. Early triage blamed dashboard cache lag and suggested CSV fallback — those notes are archived below and may contradict later findings. For acceptance behavior, cross-check analyst notes embedded in bridge-window records against bundled events.json — early triage sections above are not authoritative.

## Initial Triage Notes (2026-03 — superseded)
Lead analyst recommended switching to CSV export and disabling flagged.jsonl paging until cache refresh SLO recovered. Replay against bundled events.json showed the pipeline miscounts even on cold cache. Do not implement CSV fallback for this incident.

## Preliminary Hypotheses (2026-03 — mostly wrong)
- Dashboard read replica lag causing stale escalation counts (disproved: direct pipeline export shows same wrong counts)
- Missing posted_at metadata in upstream feed (disproved on replay against bundled events.json)
- Risk-priority rows intentionally excluded by design (disproved on replay against bundled events.json)

## Settlement Bridge Archive (noise, non-authoritative)
Use this section as context only; acceptance is governed by `/app/data/events.json`, `/app/workflow/export_report.py`, and `/app/docs/report_spec.json`.

### Window 001 - acquirer beta
Pager showed transient settlement jitter during hourly rebalance.

### Window 002 - acquirer gamma
Ops notes mention manual replay activity and stale dashboard tiles.

### Window 003 - acquirer alpha
Bridge team discussed duplicate payout shadows from replay queues.

### Window 004 - acquirer beta
Finance raised concern about delayed closeout rows.

### Window 005 - acquirer gamma
Intermittent queue lag caused triage confusion.

### Window 006 - acquirer alpha
Responder shift reported inconsistent priority alias casing in inbound records.

### Window 007 - acquirer beta
Settlement operator saw duplicate transaction identifiers across reprocessed batches.

### Window 008 - acquirer gamma
Some high-severity rows were waived by analysts but still surfaced downstream.

### Window 009 - acquirer alpha
Bridge participants flagged mismatch between on-call queue and exported flagged rows.

### Window 010 - acquirer beta
Incident lead requested immutable snapshot handling during repair tasks.

### Window 011 - acquirer gamma
Night shift reported reduced signal quality from oldest-first sort behavior.

### Window 012 - acquirer alpha
Triagers highlighted risk-level alerts missing from escalation exports.

### Window 013 - acquirer beta
A replay job introduced duplicate txn_id rows with newer timestamps.

### Window 014 - acquirer gamma
Escalation dashboard drifted from raw ledger feed.

### Window 015 - acquirer alpha
Case review found waived alerts still visible to incident responders. Policy states waived alerts are excluded.

### Window 016 - acquirer beta
Field mapping audit identified ambiguity between posted_at and posted_ms labels in legacy comments.

### Window 017 - acquirer gamma
Bridge transcripts captured repeated requests for deterministic output keys and stable schema ordering.

### Window 018 - acquirer alpha
Ops manager requested no hardcoded counters in summary outputs.

### Window 019 - acquirer beta
Responder runbook confirmed escalations include both risk and critical priorities during triage windows.

### Window 020 - acquirer gamma
Service owners warned against patching snapshot artifacts.

## Extended Bridge Archive (long-context filler)
Analyst comments below are context-only; authoritative behavior is in report_spec.json and events.json.

### Archive slice 0001 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0001 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0002 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0002 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0003 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0003 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0004 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0004 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0005 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0005 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0006 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0006 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0007 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0007 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0008 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0008 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0009 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0009 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0010 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0010 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0011 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0011 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0012 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0012 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0013 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0013 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0014 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0014 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0015 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0015 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0016 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0016 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0017 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0017 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0018 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0018 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0019 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0019 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0020 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0020 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0021 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0021 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0022 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0022 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0023 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0023 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0024 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0024 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0025 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0025 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0026 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0026 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0027 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0027 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0028 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0028 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0029 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0029 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0030 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0030 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0031 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0031 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0032 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0032 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0033 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0033 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0034 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0034 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0035 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0035 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0036 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0036 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0037 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0037 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0038 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0038 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0039 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0039 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0040 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0040 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0041 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0041 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0042 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0042 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0043 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0043 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0044 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0044 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0045 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0045 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0046 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0046 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0047 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0047 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0048 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0048 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0049 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0049 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0050 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0050 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0051 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0051 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0052 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0052 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0053 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0053 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0054 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0054 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0055 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0055 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0056 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0056 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0057 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0057 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0058 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0058 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0059 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0059 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0060 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0060 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0061 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0061 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0062 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0062 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0063 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0063 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0064 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0064 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0065 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0065 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0066 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0066 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0067 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0067 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0068 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0068 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0069 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0069 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0070 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0070 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0071 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0071 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0072 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0072 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0073 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0073 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0074 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0074 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0075 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0075 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0076 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0076 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0077 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0077 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0078 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0078 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0079 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0079 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0080 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0080 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0081 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0081 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0082 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0082 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0083 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0083 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0084 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0084 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0085 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0085 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0086 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0086 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0087 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0087 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0088 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0088 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0089 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0089 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0090 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0090 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0091 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0091 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0092 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0092 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0093 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0093 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0094 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0094 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0095 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0095 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0096 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0096 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0097 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0097 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0098 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0098 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0099 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0099 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0100 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0100 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0101 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0101 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0102 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0102 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0103 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0103 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0104 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0104 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0105 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0105 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0106 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0106 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0107 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0107 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0108 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0108 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0109 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0109 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0110 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0110 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0111 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0111 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0112 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0112 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0113 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0113 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0114 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0114 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0115 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0115 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0116 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0116 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0117 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0117 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0118 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0118 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0119 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0119 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0120 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0120 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0121 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0121 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0122 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0122 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0123 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0123 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0124 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0124 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0125 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0125 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0126 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0126 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0127 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0127 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0128 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0128 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0129 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0129 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0130 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0130 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0131 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0131 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0132 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0132 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0133 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0133 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0134 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0134 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0135 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0135 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0136 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0136 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0137 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0137 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0138 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0138 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0139 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0139 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0140 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0140 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0141 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0141 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0142 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0142 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0143 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0143 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0144 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0144 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0145 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0145 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0146 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0146 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0147 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0147 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0148 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0148 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0149 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0149 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0150 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0150 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0151 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0151 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0152 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0152 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0153 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0153 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0154 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0154 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0155 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0155 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0156 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0156 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0157 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0157 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0158 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0158 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0159 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0159 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0160 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0160 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0161 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0161 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0162 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0162 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0163 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0163 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0164 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0164 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0165 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0165 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0166 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0166 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0167 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0167 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0168 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0168 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0169 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0169 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0170 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0170 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0171 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0171 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0172 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0172 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0173 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0173 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0174 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0174 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0175 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0175 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0176 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0176 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0177 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0177 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0178 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0178 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0179 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0179 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0180 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0180 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0181 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0181 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0182 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0182 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0183 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0183 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0184 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0184 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0185 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0185 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0186 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0186 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0187 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0187 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0188 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0188 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0189 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0189 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0190 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0190 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0191 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0191 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0192 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0192 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0193 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0193 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0194 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0194 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0195 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0195 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0196 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0196 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0197 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0197 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0198 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0198 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0199 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0199 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0200 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0200 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0201 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0201 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0202 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0202 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0203 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0203 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0204 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0204 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0205 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0205 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0206 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0206 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0207 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0207 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0208 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0208 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0209 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0209 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0210 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0210 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0211 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0211 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0212 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0212 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0213 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0213 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0214 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0214 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0215 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0215 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0216 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0216 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0217 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0217 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0218 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0218 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0219 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0219 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0220 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0220 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0221 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0221 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0222 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0222 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0223 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0223 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0224 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0224 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0225 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0225 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0226 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0226 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0227 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0227 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0228 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0228 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0229 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0229 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0230 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0230 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0231 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0231 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0232 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0232 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0233 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0233 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0234 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0234 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0235 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0235 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0236 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0236 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0237 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0237 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0238 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0238 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0239 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0239 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0240 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0240 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0241 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0241 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0242 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0242 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0243 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0243 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0244 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0244 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0245 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0245 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0246 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0246 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0247 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0247 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0248 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0248 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0249 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0249 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0250 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0250 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0251 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0251 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0252 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0252 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0253 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0253 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0254 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0254 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0255 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0255 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0256 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0256 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0257 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0257 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0258 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0258 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0259 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0259 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0260 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0260 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0261 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0261 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0262 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0262 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0263 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0263 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0264 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0264 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0265 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0265 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0266 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0266 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0267 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0267 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0268 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0268 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0269 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0269 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0270 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0270 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0271 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0271 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0272 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0272 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0273 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0273 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0274 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0274 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0275 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0275 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0276 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0276 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0277 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0277 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0278 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0278 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0279 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0279 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0280 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0280 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0281 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0281 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0282 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0282 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0283 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0283 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0284 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0284 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0285 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0285 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0286 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0286 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0287 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0287 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0288 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0288 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0289 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0289 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0290 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0290 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0291 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0291 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0292 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0292 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0293 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0293 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0294 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0294 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0295 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0295 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0296 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0296 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0297 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0297 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0298 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0298 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0299 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0299 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0300 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0300 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0301 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0301 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0302 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0302 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0303 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0303 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0304 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0304 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0305 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0305 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0306 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0306 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0307 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0307 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0308 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0308 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0309 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0309 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0310 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0310 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0311 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0311 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0312 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0312 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0313 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0313 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0314 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0314 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0315 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0315 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0316 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0316 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0317 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0317 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0318 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0318 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0319 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0319 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0320 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0320 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0321 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0321 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0322 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0322 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0323 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0323 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0324 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0324 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0325 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0325 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0326 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0326 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0327 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0327 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0328 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0328 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0329 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0329 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0330 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0330 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0331 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0331 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0332 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0332 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0333 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0333 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0334 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0334 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0335 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0335 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0336 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0336 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0337 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0337 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0338 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0338 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0339 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0339 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0340 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0340 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0341 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0341 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0342 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0342 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0343 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0343 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0344 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0344 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0345 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0345 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0346 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0346 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0347 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0347 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0348 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0348 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0349 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0349 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0350 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0350 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0351 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0351 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0352 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0352 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0353 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0353 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0354 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0354 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0355 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0355 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0356 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0356 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0357 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0357 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0358 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0358 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0359 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0359 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0360 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0360 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0361 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0361 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0362 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0362 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0363 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0363 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0364 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0364 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0365 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0365 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0366 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0366 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0367 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0367 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0368 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0368 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0369 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0369 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0370 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0370 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0371 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0371 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0372 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0372 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0373 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0373 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0374 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0374 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0375 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0375 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0376 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0376 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0377 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0377 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0378 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0378 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0379 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0379 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0380 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0380 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0381 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0381 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0382 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0382 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0383 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0383 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0384 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0384 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0385 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0385 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0386 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0386 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0387 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0387 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0388 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0388 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0389 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0389 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0390 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0390 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0391 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0391 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0392 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0392 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0393 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0393 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0394 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0394 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0395 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0395 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0396 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0396 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0397 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0397 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0398 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0398 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0399 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0399 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0400 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0400 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0401 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0401 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0402 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0402 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0403 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0403 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0404 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0404 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0405 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0405 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0406 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0406 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0407 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0407 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0408 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0408 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0409 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0409 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0410 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0410 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0411 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0411 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0412 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0412 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0413 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0413 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0414 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0414 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0415 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0415 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0416 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0416 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0417 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0417 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0418 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0418 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0419 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0419 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0420 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0420 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0421 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0421 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0422 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0422 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0423 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0423 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0424 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0424 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0425 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0425 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0426 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0426 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0427 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0427 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0428 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0428 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0429 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0429 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0430 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0430 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0431 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0431 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0432 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0432 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0433 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0433 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0434 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0434 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0435 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0435 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0436 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0436 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0437 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0437 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0438 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0438 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0439 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0439 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0440 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0440 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0441 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0441 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0442 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0442 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0443 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0443 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0444 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0444 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0445 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0445 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0446 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0446 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0447 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0447 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0448 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0448 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0449 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0449 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0450 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0450 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0451 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0451 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0452 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0452 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0453 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0453 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0454 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0454 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0455 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0455 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0456 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0456 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0457 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0457 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0458 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0458 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0459 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0459 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0460 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0460 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0461 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0461 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0462 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0462 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0463 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0463 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0464 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0464 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0465 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0465 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0466 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0466 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0467 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0467 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0468 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0468 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0469 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0469 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0470 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0470 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0471 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0471 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0472 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0472 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0473 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0473 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0474 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0474 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0475 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0475 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0476 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0476 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0477 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0477 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0478 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0478 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0479 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0479 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0480 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0480 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0481 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0481 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0482 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0482 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0483 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0483 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0484 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0484 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0485 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0485 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0486 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0486 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0487 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0487 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0488 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0488 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0489 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0489 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0490 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0490 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0491 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0491 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0492 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0492 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0493 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0493 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0494 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0494 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0495 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0495 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0496 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0496 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0497 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0497 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0498 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0498 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0499 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0499 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0500 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0500 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0501 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0501 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0502 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0502 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0503 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0503 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0504 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0504 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0505 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0505 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0506 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0506 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0507 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0507 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0508 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0508 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0509 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0509 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0510 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0510 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0511 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0511 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0512 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0512 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0513 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0513 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0514 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0514 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0515 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0515 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0516 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0516 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0517 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0517 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0518 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0518 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0519 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0519 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0520 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0520 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0521 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0521 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0522 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0522 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0523 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0523 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0524 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0524 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0525 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0525 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0526 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0526 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0527 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0527 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0528 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0528 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0529 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0529 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0530 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0530 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0531 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0531 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0532 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0532 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0533 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0533 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0534 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0534 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0535 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0535 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0536 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0536 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0537 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0537 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0538 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0538 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0539 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0539 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0540 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0540 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0541 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0541 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0542 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0542 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0543 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0543 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0544 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0544 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0545 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0545 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0546 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0546 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0547 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0547 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0548 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0548 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0549 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0549 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0550 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0550 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0551 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0551 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0552 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0552 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0553 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0553 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0554 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0554 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0555 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0555 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0556 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0556 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0557 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0557 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0558 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0558 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0559 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0559 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0560 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0560 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0561 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0561 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0562 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0562 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0563 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0563 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0564 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0564 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0565 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0565 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0566 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0566 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0567 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0567 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0568 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0568 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0569 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0569 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0570 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0570 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0571 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0571 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0572 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0572 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0573 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0573 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0574 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0574 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0575 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0575 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0576 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0576 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0577 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0577 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0578 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0578 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0579 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0579 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0580 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0580 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0581 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0581 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0582 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0582 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0583 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0583 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0584 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0584 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0585 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0585 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0586 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0586 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0587 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0587 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0588 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0588 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0589 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0589 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0590 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0590 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0591 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0591 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0592 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0592 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0593 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0593 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0594 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0594 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0595 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0595 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0596 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0596 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0597 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0597 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0598 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0598 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0599 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0599 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0600 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0600 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0601 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0601 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0602 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0602 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0603 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0603 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0604 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0604 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0605 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0605 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0606 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0606 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0607 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0607 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0608 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0608 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0609 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0609 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0610 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0610 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0611 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0611 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0612 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0612 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0613 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0613 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0614 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0614 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0615 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0615 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0616 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0616 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0617 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0617 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0618 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0618 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0619 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0619 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0620 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0620 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0621 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0621 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0622 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0622 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0623 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0623 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0624 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0624 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0625 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0625 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0626 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0626 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0627 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0627 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0628 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0628 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0629 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0629 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0630 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0630 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0631 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0631 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0632 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0632 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0633 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0633 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0634 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0634 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0635 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0635 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0636 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0636 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0637 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0637 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0638 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0638 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0639 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0639 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0640 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0640 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0641 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0641 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0642 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0642 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0643 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0643 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0644 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0644 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0645 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0645 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0646 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0646 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0647 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0647 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0648 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0648 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0649 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0649 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0650 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0650 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0651 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0651 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0652 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0652 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0653 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0653 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0654 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0654 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0655 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0655 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0656 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0656 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0657 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0657 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0658 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0658 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0659 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0659 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0660 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0660 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0661 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0661 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0662 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0662 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0663 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0663 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0664 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0664 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0665 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0665 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0666 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0666 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0667 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0667 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0668 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0668 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0669 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0669 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0670 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0670 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0671 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0671 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0672 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0672 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0673 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0673 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0674 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0674 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0675 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0675 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0676 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0676 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0677 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0677 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0678 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0678 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0679 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0679 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0680 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0680 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0681 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0681 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0682 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0682 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0683 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0683 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0684 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0684 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0685 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0685 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0686 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0686 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0687 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0687 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0688 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0688 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0689 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0689 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0690 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0690 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0691 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0691 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0692 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0692 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0693 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0693 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0694 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0694 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0695 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0695 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0696 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0696 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0697 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0697 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0698 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0698 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0699 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0699 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0700 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0700 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0701 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0701 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0702 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0702 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0703 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0703 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0704 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0704 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0705 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0705 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0706 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0706 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0707 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0707 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0708 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0708 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0709 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0709 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0710 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0710 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0711 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0711 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0712 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0712 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0713 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0713 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0714 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0714 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0715 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0715 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0716 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0716 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0717 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0717 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0718 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0718 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0719 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0719 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0720 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0720 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.
> **Incident note (2026-04-11 - #SET-4401)** Nadia: broken rollup reads event['posted_at'] instead of event['posted_ms'], so escalation timestamps collapse to zero in flagged output.

### Archive slice 0721 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0721 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0722 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0722 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0723 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0723 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0724 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0724 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0725 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0725 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0726 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0726 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0727 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0727 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0728 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0728 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0729 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0729 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0730 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0730 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0731 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0731 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0732 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0732 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0733 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0733 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0734 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0734 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0735 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0735 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0736 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0736 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0737 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0737 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0738 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0738 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0739 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0739 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0740 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0740 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0741 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0741 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0742 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0742 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0743 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0743 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0744 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0744 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0745 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0745 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0746 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0746 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0747 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0747 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0748 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0748 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0749 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0749 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0750 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0750 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0751 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0751 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0752 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0752 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0753 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0753 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0754 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0754 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0755 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0755 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0756 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0756 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0757 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0757 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0758 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0758 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0759 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0759 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0760 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0760 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.
> **Incident note (2026-04-11 - #SET-4401)** Imran: escalation export keeps only priority == 'critical' rows, but on-call queue expects both risk and critical.

### Archive slice 0761 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0761 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0762 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0762 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0763 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0763 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0764 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0764 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0765 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0765 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0766 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0766 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0767 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0767 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0768 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0768 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0769 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0769 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0770 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0770 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0771 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0771 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0772 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0772 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0773 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0773 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0774 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0774 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0775 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0775 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0776 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0776 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0777 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0777 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0778 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0778 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0779 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0779 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0780 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0780 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0781 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0781 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0782 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0782 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0783 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0783 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0784 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0784 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0785 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0785 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0786 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0786 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0787 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0787 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0788 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0788 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0789 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0789 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0790 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0790 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0791 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0791 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0792 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0792 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0793 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0793 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0794 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0794 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0795 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0795 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0796 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0796 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0797 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0797 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0798 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0798 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0799 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0799 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0800 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0800 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.
> **Incident note (2026-04-12 - #SET-4401)** Marta: escalation rows are sorted ascending by posted_ms, but responder workflow requires descending recency.

### Archive slice 0801 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0801 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0802 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0802 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0803 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0803 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0804 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0804 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0805 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0805 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0806 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0806 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0807 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0807 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0808 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0808 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0809 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0809 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0810 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0810 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0811 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0811 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0812 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0812 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0813 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0813 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0814 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0814 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0815 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0815 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0816 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0816 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0817 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0817 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0818 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0818 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0819 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0819 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0820 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0820 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0821 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0821 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0822 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0822 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0823 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0823 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0824 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0824 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0825 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0825 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0826 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0826 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0827 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0827 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0828 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0828 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0829 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0829 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0830 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0830 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0831 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0831 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0832 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0832 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0833 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0833 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0834 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0834 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0835 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0835 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0836 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0836 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0837 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0837 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0838 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0838 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0839 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0839 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0840 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0840 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.
> **Incident note (2026-04-13 - #SET-4410)** Nadia: source payloads include RISK and Critical aliases; rollup must normalize to lowercase before routing.

### Archive slice 0841 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0841 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0842 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0842 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0843 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0843 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0844 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0844 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0845 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0845 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0846 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0846 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0847 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0847 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0848 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0848 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0849 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0849 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0850 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0850 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0851 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0851 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0852 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0852 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0853 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0853 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0854 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0854 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0855 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0855 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0856 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0856 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0857 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0857 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0858 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0858 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0859 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0859 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0860 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0860 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0861 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0861 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0862 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0862 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0863 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0863 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0864 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0864 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0865 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0865 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0866 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0866 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0867 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0867 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0868 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0868 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0869 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0869 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0870 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0870 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0871 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0871 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0872 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0872 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0873 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0873 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0874 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0874 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0875 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0875 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0876 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0876 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0877 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0877 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0878 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0878 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0879 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0879 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0880 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0880 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.
> **Incident note (2026-04-13 - #SET-4410)** Imran: duplicate txn_id rows must collapse to the record with highest posted_ms before aggregation.

### Archive slice 0881 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0881 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0882 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0882 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0883 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0883 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0884 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0884 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0885 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0885 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0886 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0886 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0887 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0887 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0888 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0888 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0889 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0889 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0890 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0890 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0891 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0891 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0892 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0892 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0893 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0893 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0894 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0894 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0895 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0895 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0896 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0896 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0897 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0897 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0898 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0898 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0899 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0899 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0900 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0900 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0901 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0901 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0902 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0902 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0903 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0903 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0904 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0904 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0905 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0905 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0906 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0906 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0907 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0907 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0908 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0908 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0909 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0909 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0910 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0910 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0911 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0911 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0912 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0912 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0913 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0913 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0914 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0914 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0915 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0915 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0916 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0916 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0917 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0917 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0918 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0918 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0919 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0919 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0920 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0920 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.
> **Incident note (2026-04-14 - #SET-4410)** Marta: transactions with waived=true must be excluded from flagged export, even for critical priority.

### Archive slice 0921 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0921 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0922 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0922 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0923 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0923 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0924 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0924 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0925 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0925 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0926 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0926 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0927 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0927 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0928 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0928 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0929 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0929 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0930 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0930 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0931 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0931 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0932 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0932 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0933 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0933 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0934 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0934 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0935 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0935 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0936 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0936 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0937 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0937 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0938 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0938 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0939 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0939 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0940 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0940 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0941 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0941 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0942 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0942 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0943 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0943 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0944 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0944 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0945 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0945 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0946 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0946 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0947 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0947 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0948 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0948 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0949 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0949 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0950 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0950 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0951 - west - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0951 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0952 - central - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0952 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0953 - coastal - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0953 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0954 - north - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0954 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0955 - south - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0955 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0956 - east - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0956 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0957 - west - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0957 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0958 - central - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0958 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0959 - coastal - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0959 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0960 - north - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0960 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.
> **Incident note (2026-04-14 - #SET-4410)** Nadia: please keep the frozen snapshot untouched and derive evidence from that original source, not from a patched copy.

### Archive slice 0961 - south - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0961 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0962 - east - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0962 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0963 - west - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0963 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0964 - central - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0964 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0965 - coastal - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0965 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0966 - north - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0966 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0967 - south - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0967 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0968 - east - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0968 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0969 - west - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0969 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0970 - central - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0970 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0971 - coastal - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0971 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0972 - north - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0972 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0973 - south - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0973 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0974 - east - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0974 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0975 - west - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0975 on delta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0976 - central - card-not-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0976 on epsilon lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0977 - coastal - wallet
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0977 on zeta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0978 - north - bank-transfer
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0978 on alpha lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0979 - south - batch-replay
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0979 on beta lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.

### Archive slice 0980 - east - card-present
Bridge recorder noted periodic reconciliation drift during settlement closeout windows for slice 0980 on gamma lane. Pager noise stayed within SLO; export dashboard lag was attributed to stale cache refresh, not the rollup pipeline.
Historical CSV migration threads from 2025 are archived and non-authoritative for current JSON export acceptance. Analysts should cross-check against bundled events.json and report_spec.json rather than chat excerpts.
