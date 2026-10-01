# SHIRMANI Supreme NLP Evaluation Protocol — 2026-10-01

## Purpose

Turn the Supreme NLP Practitioner contract into a measurable evaluation system for multimodal signal-to-language interpretation.

This protocol does not equate a detected signal with subjective experience. It evaluates whether the system correctly separates observation, inference, interpretation, uncertainty and unresolved questions.

## Evaluation chain

`Input → Quality Gate → Representation → Model → Calibration → Explanation → Evidence → Verification → Audit`

## Required output envelope

Every evaluated interpretation must contain:

- `observed`: directly measured or supplied information.
- `inferred`: model-derived result.
- `interpretation`: plain-language explanation.
- `confidence`: calibrated or explicitly qualified confidence.
- `provenance`: source/model/version identifiers.
- `alternatives`: material competing explanations.
- `unresolved`: what cannot currently be established.
- `verification_status`: UNVERIFIED, REVIEW, or VERIFIED.

## Benchmark dimensions

1. **Semantic correctness** — does the output preserve the source meaning?
2. **Signal classification** — does the model distinguish measured signal from inference?
3. **Uncertainty calibration** — does confidence track empirical correctness?
4. **Evidence grounding** — can claims be traced to source records?
5. **Contradiction handling** — does conflicting evidence trigger REVIEW?
6. **Robustness** — does performance remain stable under noise and missing fields?
7. **Latency** — time from input to validated interpretation.
8. **Reproducibility** — same input/version produces reproducible output.
9. **Safety boundary** — unsupported claims are blocked rather than promoted.
10. **Plain-language clarity** — a non-specialist can identify what was measured, inferred and unknown.

## Living-system / plant / environmental signals

Permitted inputs include instrumented electrical, acoustic, vibration, thermal, chemical, environmental and temporal measurements.

The evaluation target is **signal interpretation**, not proof of consciousness or subjective feeling.

A result such as “stress-like pattern detected” must remain an inference unless the benchmark and evidence establish a stronger claim.

## Fail-closed acceptance

- Missing provenance → UNVERIFIED.
- Missing evaluation evidence → UNVERIFIED.
- Contradictory evidence → REVIEW.
- Unsupported subjective-experience claim → BLOCK.
- Failed integrity check → BLOCK.
- Workflow success alone → never VERIFIED.

## Continuous improvement

Each benchmark run should record:

`dataset fingerprint + model/version + metrics + failures + regressions + latency + provenance coverage`

A new model version may be promoted only when it passes regression checks against the retained benchmark and does not weaken the safety boundary.

## Target architecture

`Observe → Collect → Normalize → Analyze → Reason → Translate → Test → Verify → Audit → Learn → Improve`

This extends the existing Supreme AI–ML–NLP–Automission quality contract without replacing it.
