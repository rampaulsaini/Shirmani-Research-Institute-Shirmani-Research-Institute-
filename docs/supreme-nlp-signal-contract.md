# Supreme NLP–Signal Interpretation Contract

## Purpose

Define an evidence-first interface for translating measurable multimodal signals into simple natural-language descriptions without converting model inference into unverified claims of subjective feeling, consciousness, or intent.

## Signal chain

`source → acquisition → quality → normalization → features → model → fusion → interpretation → confidence → evidence → verification → plain-language output`

## Required separation

Every interpretation record MUST keep these fields conceptually separate:

1. **measured_signal** — observed data or derived measurement.
2. **model_output** — classifier/regressor/embedding/anomaly result.
3. **interpretation** — human-readable hypothesis about the pattern.
4. **confidence** — calibrated model confidence or uncertainty estimate.
5. **evidence** — provenance, dataset/model version and supporting observations.
6. **verification_state** — NOT_VERIFIED, TESTED, VERIFIED_BY_DEFINED_PROTOCOL, or REJECTED.
7. **limitations** — known confounders and unresolved uncertainty.

## Plain-language rule

The NLP layer may say:

> "The measured signals show a pattern associated with X in the reference data. Confidence is Y. This is an interpretation of measurable signals, not direct proof of subjective experience."

It must not silently rewrite a signal into a claim of emotion, consciousness, intention, pain, pleasure, or other subjective state unless an explicit validated protocol and evidence support that claim.

## Accuracy and speed

Optimize jointly for:

- calibrated accuracy
- precision / recall / F1 where applicable
- false-positive and false-negative rates
- robustness to distribution shift
- latency
- reproducibility
- provenance completeness
- verification coverage

"Supreme accuracy" is an engineering target, not a preset factual result. The system must measure it against named test sets and retain failed cases.

## Continuous improvement

Automission may propose model, prompt, schema, routing, or test improvements. A proposed change must pass:

`unit tests → schema validation → regression tests → security checks → evidence/verification gates → human approval for consequential production changes`

No agent may mark its own output as independently verified.

## Five-minute operating loop

`Observe → Collect → Normalize → Analyze → Reason → Execute → Test → Verify → Audit → Learn → Improve`
