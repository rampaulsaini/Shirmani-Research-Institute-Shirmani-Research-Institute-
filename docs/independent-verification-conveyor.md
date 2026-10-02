# Independent Verification Conveyor

## Objective

Convert the existing 0% independently VERIFIED baseline into a controlled,
evidence-first conveyor without allowing automation to manufacture verification.

## Canonical state machine

EVIDENCE_COLLECTION -> INDEPENDENT_TEST -> REPRODUCIBLE_RESULT -> AUDIT -> VERIFIED

### Evidence collection

Each claim receives precise claim text, an operational definition, independent
source references, provenance and explicit counter-evidence targets.

### Independent test

The test must be separable from the authoring workflow. A successful GitHub
Actions run is only a process result; it is not independent verification.

### Reproducible result

Record exact inputs, method, expected result, observed result, test version,
environment and references required to reproduce the result.

### Audit

Bind the review to the exact queue task using a deterministic hash. Record
reviewer identity/role, timestamp, evidence, countercase review and audit record.

### VERIFIED

Only an independent reviewer can create the final VERIFIED decision. Automission
can prepare, test, detect missing fields, calculate hashes, generate packets and
continuously audit the state, but it cannot promote a claim merely because its
own workflow passed.

## Current baseline

The repository independent-verification status preserves 0% independently
verified records. Evidence-supported records are intentionally distinct from
complete framework verification.

## Continuous Automission contract

Every five minutes:

Observe -> Collect -> Normalize -> Analyze -> Reason -> Execute -> Test -> Verify -> Audit -> Learn -> Improve

The verification conveyor runs as a fail-closed control plane. Missing queues,
missing review records, incomplete reproduction data or absent audit provenance
do not become VERIFIED; they remain blocked and visible.

## Quality metrics

Track separately:
- evidence coverage,
- independent-test coverage,
- reproducibility coverage,
- counter-evidence coverage,
- audit completeness,
- independently VERIFIED count,
- regression/failure count,
- time-to-resolution.

Never collapse these into a single accuracy number.
