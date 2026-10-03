# SHIRMANI Supreme Independent Verification Ledger

## Purpose

Create an explicit boundary between automated preparation/QC and independent verification.

The ledger does not manufacture verification. It counts only records that contain the required independent evidence and reviewer attestation.

## Verification rule

A record may be VERIFIED only when all required fields are present:

- source record identity,
- clearly defined verification scope,
- one or more evidence references,
- an identified independent verifier,
- a documented verification method,
- review timestamp,
- explicit VERIFIED state,
- stated limitations.

Automation health, workflow success, QC PASS, benchmark PASS, model confidence or provenance alone cannot promote a record to VERIFIED.

## Fail-closed states

REGISTERED → UNVERIFIED → REVIEW → VERIFIED

BLOCKED remains terminal until its blocking condition is resolved.

If no eligible verification records exist, the ledger reports:

- verified_count = 0
- verification_completion_percent = 0
- status = AWAITING_INDEPENDENT_EVIDENCE

No target count is converted into a claim of completion.

## Five-minute audit

The ledger audit scans the verification-record directory, validates every record against the schema, counts states, and reports blockers and completion percentage.

## Independence boundary

The audit automation validates structure and evidence declarations. It does not itself become the independent verifier. Human review or another genuinely independent verification process remains responsible for the substantive verification decision.
