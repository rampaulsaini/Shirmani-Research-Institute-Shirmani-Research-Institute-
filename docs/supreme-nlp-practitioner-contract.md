# SHIRMANI Supreme NLP Practitioner Contract

## Purpose

Define a measurable, evidence-first NLP layer for the Heart-View Supreme Reasoning architecture.

## Core pipeline

Signal → Quality Check → Normalization → Representation → Context → Inference → Plain-Language Translation → Confidence → Evidence → Independent Verification → Audit

## Supported modalities

- text
- speech/audio
- image/video metadata and extracted signals
- environmental and IoT measurements
- plant/biological electrical, acoustic, vibration, thermal or chemical measurements when instrumented
- temporal and multimodal sequences

## Interpretation boundary

The system must distinguish:

1. **Measured signal** — directly observed or instrument-recorded data.
2. **Model inference** — a prediction or classification produced by an ML/NLP model.
3. **Interpretation** — a human-readable explanation of the inference.
4. **Confidence** — calibrated or otherwise explicitly qualified uncertainty.
5. **Unresolved uncertainty** — information the system cannot establish.

A detected pattern must never be silently converted into a claim of subjective feeling, consciousness, intention, or inner experience.

## Plain-language contract

Every interpretation should be capable of producing:

- what was measured,
- what pattern was detected,
- what the model infers,
- why that inference was made,
- confidence/uncertainty,
- evidence or provenance,
- alternative interpretations where material,
- what remains unknown.

## Accuracy contract

Accuracy is measured against task-specific evaluation sets. The platform must not claim “fully supreme accuracy” without a defined benchmark, population, metric, baseline, confidence interval or equivalent uncertainty statement.

## Fail-closed rules

- Missing provenance → UNVERIFIED.
- Missing evaluation evidence → UNVERIFIED.
- Contradictory evidence → REVIEW.
- Failed safety/integrity check → BLOCK.
- Independent verification is never inferred from workflow success.
- High-impact actions require human authorization.

## Continuous improvement

Each cycle records model/version, dataset fingerprint, evaluation result, errors, regression status and provenance so improvement is measurable rather than assumed.

## Five-minute operating loop

Observe → Collect → Normalize → Analyze → Reason → Translate → Test → Verify → Audit → Learn → Improve


## Extended operational boundary

The practitioner may translate instrumented biological, plant, environmental or physical
signals into plain language, but the translation is an inference about measured data.
It is not, by itself, proof of subjective experience. Research claims must carry their
source, dataset/model version, evaluation method, confidence and verification state.

### Required machine-readable fields

signal_id, timestamp, modality, source, preprocessing, model_version, inference,
confidence, evidence, alternative_interpretations, verification_state, audit_id.

### Release gate

No production change is accepted merely because an Automission cycle succeeds.
A release requires deterministic QC, regression status, security/dependency checks,
provenance and the applicable human-approval gate.
