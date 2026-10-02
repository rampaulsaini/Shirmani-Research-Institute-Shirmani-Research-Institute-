# SHIRMANI Supreme NLP Multimodal Signal-to-Language Contract

## Purpose

Define a reproducible interface for converting instrumented multimodal signals into simple human-readable language while preserving the boundary between observation, model inference and claims about subjective experience.

## Supported inputs

- text and speech
- audio and vibration
- image/video-derived measurements
- temperature, light, humidity and environmental telemetry
- electrical/biopotential measurements when appropriately instrumented
- chemical measurements when appropriately instrumented
- temporal and multimodal sequences

## Canonical pipeline

Raw signal → Quality → Calibration/context → Normalization → Feature representation → Pattern detection → Model inference → Evidence lookup → Alternative interpretations → Plain-language translation → Confidence/uncertainty → Verification → Audit

## Interpretation boundary

The system may describe measured patterns and model-supported interpretations.

It must not silently convert a measured pattern into a statement that a living organism, plant, object or environment has a subjective feeling, consciousness, intention or human-like emotion.

If a task is explicitly designed to study a possible biological state, the output must use evidence-bounded language such as:

- "The measured signal contains pattern X."
- "Model Y associates this pattern with state Z in dataset D."
- "This interpretation has confidence/uncertainty U."
- "Alternative explanation A remains possible."
- "Subjective experience was not measured by this instrument."

## Required interpretation record

Every published interpretation should preserve:

1. source and provenance
2. signal modality
3. acquisition context
4. data quality status
5. detected pattern
6. model name/version
7. task and population scope
8. model inference
9. benchmark reference
10. confidence/uncertainty
11. evidence references
12. alternative interpretations
13. unresolved questions
14. verification state
15. timestamp

## Fail-closed rules

- Missing provenance → BLOCKED.
- Missing signal modality or acquisition context → BLOCKED.
- Missing model/version for an inferred result → BLOCKED.
- Missing evidence or benchmark reference → UNVERIFIED.
- Subjective-experience claim without direct supporting evidence → BLOCKED.
- Contradictory evidence → REVIEW.
- Verification cannot be inferred from workflow success.
- High-impact actions require human authorization.

## Accuracy

Accuracy is task-specific. A system-wide "fully supreme accuracy" claim is prohibited unless supported by defined benchmarks, populations, metrics, uncertainty and reproducible evidence.

## Automission

The five-minute cycle validates contracts, schemas, provenance, regression gates and committed evidence. It does not fabricate measurements, perform uncontrolled training, or promote an unverified interpretation to VERIFIED.
