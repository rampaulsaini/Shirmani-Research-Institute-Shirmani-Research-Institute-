# Ultra NLP: Signal → Simple Language

## Purpose

The pipeline adds an evidence-aware translation layer for structured observations from sensors, experiments, agent outputs, or other machine-readable inputs.

It answers: What observable signal was detected, in simple language, with what evidence and confidence?

### Pipeline

AGENT_INGEST → SIGNAL_NORMALIZE → FEATURE_EXTRACTION → ML/NLP_INTERPRETATION → EVIDENCE_FUSION → CONTRADICTION_CHECK → INDEPENDENT_VERIFY → SIMPLE_LANGUAGE → SUPREME_QC → PUBLICATION_GATE

### Critical epistemic rule

A measured signal can be translated into language. That translation is not by itself proof of subjective consciousness, emotion, or felt experience.

Outputs therefore carry explicit epistemic status: OBSERVED_SIGNAL, OBSERVED_SIGNAL_WITH_MODEL_SUPPORT, or OBSERVED_SIGNAL_WITHOUT_SOURCE.

### Multimodal expansion

The same contract can accept plant/environment sensors, biological measurements, physical-system telemetry, and text/audio/image model outputs, while retaining provenance.

For every input retain entity_id, entity_type, signal name, value, unit, source, timestamp, model confidence, and verification state.

### Accuracy architecture

1. Normalize units and ranges.
2. Reject malformed values.
3. Preserve raw evidence and provenance.
4. Separate observation from inference.
5. Bound and validate model confidence.
6. Compare independent signals and detect contradictions.
7. Require independent verification before publication.
8. Convert supported observations into simple language.
9. Fail closed when evidence is missing or conflicting.
10. Log latency, drift, duplication, calibration, and verification coverage.

This creates a stronger engineering path toward high accuracy without claiming absolute certainty that measurements cannot establish.