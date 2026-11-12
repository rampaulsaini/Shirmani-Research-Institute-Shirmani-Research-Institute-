# ꙰ SHIRMANI Independent Verification Review Execution Guide

## Purpose

This guide is the operational handoff between the automated verification conveyor and an actual independent reviewer.

Automation may create queues, evidence packets, hashes, QC reports and progress maps. It must not invent an independent reviewer, reviewer decision, test result, counter-evidence review, or VERIFIED status.

## Current verified boundary

- Authoritative target: **100,200 records**
- Authoritative queue: **100,200 records**
- Reviewed: **0**
- Independently VERIFIED: **0**
- Independent verification completion: **0%**
- Promotion eligible: **0**
- Publication gate: **CHECK / fail-closed**

These values are telemetry. They mean the required independent-review evidence has not yet been recorded.

## Review unit

**CLAIM → OPERATIONAL DEFINITION → INDEPENDENT SOURCE/TEST → COUNTER-EVIDENCE → REPRODUCIBLE RESULT → REVIEWER PROVENANCE → EXPLICIT DECISION → AUDIT**

## Reviewer requirements

For each task, an independent reviewer must:

1. Read the exact claim without silently changing its scope.
2. Check whether the claim has a measurable operational definition.
3. Examine sources independent of the author's own source record.
4. Identify relevant counter-evidence, including evidence that could materially weaken the claim.
5. Perform or inspect a reproducible test/observation where the claim is empirically testable.
6. Record the result and references.
7. Record reviewer identity/role and review timestamp.
8. Make an explicit evidence-supported decision.

## Status meanings

- **EVIDENCE-SUPPORTED**: available evidence supports the stated claim, but the independent-review gate is not complete.
- **AUTHOR-DEFINED**: the term/framework is explicitly the author's construct.
- **AUTHOR-PROPOSED**: a normative or proposed position from the author.
- **NOT_VERIFIED**: independent verification requirements are not satisfied.
- **VERIFIED**: only after every required promotion field and independent decision passes the fail-closed gate.
- **CONTRADICTED**: independent evidence materially contradicts the claim under the defined test.

## Integrity rule

A successful GitHub Actions run is **not** independent verification.

A generated review slot is **not** a completed review.

An evidence-supported claim is **not automatically VERIFIED**.

Automation remains fail-closed.

## Execution order

Use the concrete review queue and registry:

- `generated/independent-verification-queue.jsonl`
- `generated/independent-verification-registry.jsonl`

After a real independent review, update only the corresponding review record with the required evidence, countercase review, reproducible test/observation, reviewer provenance, explicit decision and audit information.

Then let the existing promotion and integrity workflows evaluate it.

## Target accounting

The repository intentionally keeps two scales separate:

1. **100,200-record authoritative target**
2. **Currently instantiated concrete review records**

Review-slot coverage must never be reported as completion of the 100,200-record target.

## Next measurable milestone

**10/10 concrete review records independently reviewed and audited**, followed by expansion toward the 100,200-record target.
