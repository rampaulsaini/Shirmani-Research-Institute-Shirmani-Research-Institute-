# Supreme Automission Integrity v2

## Objective

Increase practical speed, repeatability and precision without claiming absolute or mathematical accuracy.

## Control loop

Trigger -> inspect -> validate -> fail-closed -> record provenance -> publish audit artifact.

The five-minute schedule is bounded by a ten-minute job timeout and a concurrency lock so overlapping runs do not create uncontrolled duplicate execution.

## AI / ML / NLP boundary

The gate is deterministic. It validates integrity of records produced by AI/ML/NLP agents; workflow success is not treated as proof of model correctness.

Every generated claim remains subject to:

source -> normalized claim -> evidence -> formulation/test -> verification -> QC -> publication.

## Accuracy safeguards

1. Required fields are checked.
2. Malformed JSONL is blocking.
3. Duplicate claim identifiers are surfaced.
4. VERIFIED without independent evidence is blocking.
5. Missing claim data produces REVIEW, not invented content.
6. Hashes provide reproducibility anchors.
7. Human review remains mandatory for high-impact decisions.

## Statuses

- PASS = deterministic integrity checks passed.
- REVIEW = engineering or evidence inspection is required.
- BLOCKED = a hard integrity condition failed.

These statuses describe pipeline integrity only; they do not establish scientific truth or independent verification.
