# SHIRMANI Supreme NLP Evidence + Multimodal V2

## Purpose

This specification extends the existing SHIRMANI Supreme NLP Practitioner and Automission layers with a stricter evidence-preserving multimodal pipeline.

The target is faster iteration **without trading away verification, reproducibility, uncertainty reporting, or fail-closed governance**.

## Core pipeline

`observe -> validate -> normalize -> fuse -> infer -> translate -> verify -> audit -> learn`

### Input modalities

- text
- speech/audio
- image/video
- time-series sensor signals
- electrical/biophysical measurements
- environmental measurements
- structured metadata

Every observation MUST retain:

- source
- timestamp
- modality
- quality
- preprocessing version
- feature/model version
- provenance fingerprint

## Evidence classes

Each result MUST be classified as one of:

1. `OBSERVED` — directly measured.
2. `INFERRED` — produced by a model from observations.
3. `CORRELATED` — statistically associated but not causally established.
4. `HYPOTHESIS` — a candidate explanation requiring testing.
5. `UNKNOWN` — insufficient evidence.

The natural-language layer MUST preserve this distinction.

## Simple-language contract

The translator should answer four questions:

1. What was actually measured?
2. What pattern was detected?
3. What interpretation is supported by the available evidence?
4. What remains unknown?

It MUST NOT convert an inferred biological/sensor state into a claim of subjective experience unless an independently validated measurement protocol establishes that claim.

## Accuracy ladder

Accuracy is measured separately for:

- signal quality
- detection
- classification
- calibration
- language translation
- evidence attribution
- temporal consistency
- robustness to noise
- cross-modal agreement
- independent verification

A single aggregate score MUST NOT hide failures in a critical layer.

## Confidence and abstention

The system MUST be able to abstain:

`insufficient evidence -> NO_CLAIM`

Low-quality or conflicting observations should reduce confidence or trigger `UNKNOWN`, rather than forcing a fluent answer.

## Multimodal fusion

When multiple modalities describe the same event:

`independent observations -> alignment -> agreement/disagreement analysis -> fused inference`

The system should preserve disagreement instead of averaging it away.

## Independent verification gate

A result becomes `VERIFIED` only after:

- deterministic contract tests pass;
- provenance is present;
- uncertainty is present where applicable;
- an independent verification path reproduces the result;
- no governance assertion is violated.

Preparation, generation, and verification remain separate states.

## Automission improvement loop

Each cycle should produce:

- current status
- detected weakness
- proposed improvement
- expected metric change
- regression tests
- verification result
- immutable fingerprint

Scheduled automation MUST remain fail-closed. Production-code mutation is not authorized merely because an agent proposes an improvement.

## Performance objective

Optimize in this order:

1. correctness
2. evidence fidelity
3. safety/governance
4. reproducibility
5. latency
6. resource efficiency

Never optimize latency by silently reducing evidence quality.

## Research boundary

Sensor-to-language systems can describe measured signals and model-supported interpretations. They do not, by language fluency alone, establish consciousness, feelings, subjective experience, or quantum claims.

Those questions require explicit operational definitions, measurable variables, labelled data, controlled experiments, and independent replication.
