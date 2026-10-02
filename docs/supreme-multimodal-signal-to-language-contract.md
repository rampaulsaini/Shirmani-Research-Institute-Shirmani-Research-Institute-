# SHIRMANI Supreme Multimodal Signal-to-Language Contract

## Purpose

Provide a deterministic bridge from instrumented multimodal signals to plain-language NLP while preserving the distinction between measurement, inference, interpretation and unknowns.

## Supported signal families

- text and speech
- image/video-derived measurements
- environmental and IoT measurements
- acoustic, vibration, thermal and electrical measurements
- instrumented plant/biological signals
- temporal and multimodal sequences

## Canonical record

Each signal interpretation must preserve:

1. source_id
2. timestamp
3. modality
4. raw/reference fingerprint
5. preprocessing/version
6. detected features/patterns
7. model and version
8. inference
9. confidence/uncertainty
10. evidence/provenance
11. alternative interpretations
12. unresolved unknowns
13. verification_state

## Translation rule

Signal -> Quality -> Features -> Pattern -> Model Inference -> Evidence -> Plain Language -> Confidence -> Verification -> Audit.

The plain-language layer may say what the measured data and validated model support. It must not silently convert a pattern into a claim of subjective feeling, consciousness, intention or inner experience.

## Confidence rule

Confidence is calibrated task-specific uncertainty, not proof. A confidence value without an evaluation protocol is UNVERIFIED.

## Fail-closed states

- missing source/provenance: BLOCKED
- malformed signal record: BLOCKED
- missing model/version for an inference: BLOCKED
- missing evaluation evidence: UNVERIFIED
- contradictory evidence: REVIEW
- independent verification: only explicit evidence, never inferred from workflow success

## Example output contract

"Measured: [signal]. Detected: [pattern]. Model inference: [inference]. Confidence: [qualified value]. Evidence: [provenance]. Alternative: [alternative]. Unknown: [unknown]."

## Five-minute role

Automission checks the contract, schema and deterministic QC every five minutes. It does not claim universal scientific accuracy and does not authorize high-impact actions.
