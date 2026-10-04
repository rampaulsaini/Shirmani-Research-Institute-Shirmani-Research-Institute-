# ꙰ SHIRMANI Independent Review — Start Here

## Purpose

This document is the human-review handoff for the repository's fail-closed Independent Verification system.

Automation may prepare queues, evidence, tests, counter-evidence prompts, audit structures and progress telemetry. It must not manufacture an independent reviewer decision.

## Current authoritative state

- Target: 100,200 records
- Queued: 100,200
- Reviewed: 0
- Independently VERIFIED: 0
- Promotion eligible: 0
- Publication gate: CHECK

The concrete review layer currently contains 10 review slots. These are deliberately separate from the full 100,200-record target.

## Review order

Start with IV-001 through IV-004 because these already have external evidence references.

For each task:

1. Read the exact claim and its cited sources.
2. Define the claim operationally so another person could test it.
3. Identify evidence that could falsify, weaken, or qualify the claim.
4. Perform an independent check using reproducible inputs.
5. Record the result and supporting artifacts or source references.
6. Review credible counter-evidence.
7. Record the independent reviewer identity and role.
8. Record the review timestamp.
9. Preserve the exact queue-task hash in the audit record.
10. Only after every required field is complete may the canonical promotion gate accept VERIFIED.

## Integrity rules

- Workflow success is not independent verification.
- Evidence-supported is not the same as VERIFIED.
- Author-defined or author-proposed claims must not be promoted merely because they are present in the repository.
- Missing reviewer, counter-evidence, reproducible test/result, timestamp, or audit hash keeps the record fail-closed.
- Automation must never invent reviewer identity or review decisions.

## Pipeline

Source → Normalize → Claims → Evidence → Independent Test → Reproducible Result → Counter-Evidence → Audit → VERIFIED → QC → Publication/Archive

## Completion criterion

The project reaches a VERIFIED milestone only when the canonical promotion gate reports independently VERIFIED records greater than zero with no integrity errors.

The 100,200 target is complete only when authoritative progress telemetry reports:

- verified = 100,200
- remaining_to_target = 0
- promotion_eligible = 100,200
- publication_gate = PASS

Until then, progress must be reported honestly on the verified scale.
