# SHIRMANI Independent Verification Execution Plan — 2026-10-03

## Purpose

Advance the existing fail-closed Evidence → VERIFIED system without fabricating verification. The target is measurable independent verification, not merely additional workflow runs.

## Current repository state

- Queue baseline: 10 records.
- Evidence-supported: 4/10.
- Author-defined/proposed: 2/10.
- Not verified: 4/10.
- Independently VERIFIED: 0/10 (0%).
- Verification readiness: 100%.
- Independent-verification conveyor: scheduled every 5 minutes.
- Evidence-to-VERIFIED control plane: scheduled every 5 minutes.
- Verification progress dashboard: scheduled every 5 minutes.
- VERIFIED promotion remains fail-closed.

## Execution sequence

1. Preserve the existing canonical source and the 0% VERIFIED baseline.
2. Bootstrap one review task for each current queue record.
3. Require an operational definition for every claim before review.
4. Attach independent sources or a reproducible experiment/observation.
5. Record counter-evidence and the reviewer’s treatment of it.
6. Reproduce the test or observation and record the environment and result.
7. Record reviewer identity/role, timestamp, decision and audit hash.
8. Run the machine gates.
9. Promote only records whose complete independent review satisfies every gate.
10. Recompute the dashboard from the registry; never infer verification from workflow success.

## Completion criteria

A record is complete only when its registry entry contains:

CLAIM → OPERATIONAL DEFINITION → INDEPENDENT SOURCE/TEST → COUNTER-EVIDENCE → REPRODUCIBLE RESULT → INDEPENDENT REVIEWER → AUDIT RECORD → EXPLICIT DECISION.

A scheduled or successful GitHub Actions run alone can never satisfy this criterion.

## Current review priority

- IV-001 through IV-004: evidence-supported claims; perform independent review and reproducibility checks.
- IV-005: retain as AUTHOR-DEFINED unless an independently testable proposition is separated from the author’s definition.
- IV-006 through IV-009: require operational definitions and test protocols before any verification decision.
- IV-010: retain as AUTHOR-PROPOSED; evaluate specific empirical environmental propositions separately from the normative objective.

## Safety against false completion

No workflow, generated packet, dashboard, benchmark, or automated agent may manufacture reviewer identity, counter-evidence review, experimental results, or a VERIFIED decision.

## Success metric

Primary metric:

independently_verified / total_queue_records × 100

Secondary metrics:

evidence_supported / total_queue_records × 100
verification_readiness
promotion_gate_error_count
orphan_queue_tasks

The authoritative VERIFIED percentage remains 0% until an actual independent review decision is recorded.
