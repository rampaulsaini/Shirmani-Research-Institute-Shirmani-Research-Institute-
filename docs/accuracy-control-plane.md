# Deterministic Accuracy Control Plane

## Purpose

The accuracy control plane increases **measurable research readiness** without
pretending that an automation pipeline can manufacture truth.

Each claim receives a bounded readiness score based on:

1. claim presence;
2. evidence presence;
3. content-hash integrity;
4. provenance locator completeness;
5. reproducibility metadata;
6. counterevidence/countercase coverage;
7. independent-verification status.

The score is **not** a probability of truth, model confidence, scientific
accuracy, or a substitute for an independent reviewer.

## Fail-closed rules

- Missing claim or invalid content hash blocks the generated report.
- The control plane never changes \`UNVERIFIED\` to \`VERIFIED\`.
- Independent verification remains a separate gate.
- Generated outputs remain derivatives of source material.
- External/financial side effects remain behind explicit authorization.

## Pipeline position

The control plane runs after claim/evidence construction and before the unified
publication gate. This makes the pipeline optimize for:

**traceability -> reproducibility -> counterevidence -> independent verification -> publication**

rather than merely increasing the number of automated runs.

## Speed and scale

The implementation is Python standard-library only. It is linear in the number
of claim records, so it can run quickly on GitHub-hosted runners without model
downloads or paid inference.

Optional ML/NLP components can consume this report later, but no external model
is required for the integrity path.
