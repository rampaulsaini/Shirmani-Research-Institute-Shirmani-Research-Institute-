# SHIRMANI Supreme NLP Practitioner — Runtime Layer

This runtime makes the existing Supreme NLP contract executable and deterministic.

## Runtime flow

Signal → Quality Check → Normalization → Representation → Context → Inference
→ Plain-Language Translation → Confidence → Evidence → Independent Verification → Audit

The runtime provides the evidence boundary; it is not presented as a trained
universal ML model. Domain-specific models must be evaluated against declared
datasets and baselines before stronger verification states are allowed.

## Required input

record_id, signal, pattern, inference, provenance.

Optional: confidence, alternative_interpretations, unresolved_unknowns,
verification_state, verification_evidence.

## Fail-closed behavior

- Missing required evidence → BLOCKED.
- Invalid verification state → BLOCKED.
- VERIFIED without explicit verification evidence → REVIEW.
- A signal pattern is never automatically treated as proof of subjective experience.
- Provenance is preserved in every report.
- Confidence is uncertainty information, not truth.

## Biological/environmental signals

Instrumented electrical, acoustic, vibration, thermal, chemical or other
measurable signals may be processed and translated into simple language while
maintaining the distinction between measurement and claims about experience.
