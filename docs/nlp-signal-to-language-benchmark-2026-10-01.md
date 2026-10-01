# Ultra-Mega NLP Practitioner Benchmark — 2026-10-01

## Purpose
This benchmark operationalizes the author's research target of an “Ultra mega infinity Quantum supreme NLP practitioner” as measurable engineering capabilities. The phrase, and claims about subjective feeling or consciousness, are not treated as independently established scientific facts.

## Evaluation dimensions
1. Signal fidelity — measured signal is preserved without invented values.
2. Signal-to-language translation — structured observations become simple-language descriptions.
3. Semantic accuracy — predictions are compared with ground truth.
4. Multilingual robustness — equivalent inputs are tested across languages.
5. Uncertainty calibration — confidence is compared with observed correctness.
6. Evidence traceability — consequential interpretations link to input/provenance.
7. Hallucination resistance — unsupported facts are penalized.
8. Countercase handling — ambiguous/conflicting signals remain uncertain.
9. Reproducibility — identical fixture + version produces identical results.
10. Independent verification readiness — evaluation remains separate from verification promotion.

## Signal-to-language boundary
For biological, plant, environmental, or non-living systems, accepted inputs may include sensor values, electrical/physical signals, sound, vibration, images, environmental measurements, and other recorded observations.

The output must distinguish **Observed**, **Inferred**, **Interpretation**, **Confidence**, and **Uncertainty**.

A generated statement such as “the plant feels sadness” is not accepted as a verified scientific conclusion merely because a model generated it. A permissible output can state that a measured pattern is associated with a trained class, together with evidence and uncertainty.

## Dataset contract
Each evaluation record contains: `id, input, expected, prediction, confidence, evidence_refs, provenance`.
Optional fields: `language, signal_type, abstained, countercase, model_version`.

## Core metrics
- classification accuracy
- exact-match rate
- macro-F1 where labels exist
- confidence calibration
- Brier score for probabilistic binary tasks
- evidence coverage
- unsupported-claim rate
- abstention quality
- reproducibility hash

No metric becomes “supreme accuracy” unless an actual evaluation dataset and reproducible run establish it.

## Fail-closed rules
Malformed records, missing provenance, confidence outside 0–1, or contract violations are benchmark errors. A missing dataset produces **NOT_READY**, never a fabricated PASS.

## Operating loop
`Observe → Collect → Normalize → Analyze → Translate → Test → Calibrate → Verify → Audit → Improve`

This is an evaluation layer for the existing Heart-View / AI–ML–NLP–Automission architecture.