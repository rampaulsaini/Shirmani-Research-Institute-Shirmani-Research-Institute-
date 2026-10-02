# Supreme Evidence Control Plane

This layer connects the existing Supreme NLP Practitioner and Supreme NLP Quality
Gate into one fail-closed control plane.

## Pipeline

observe → normalize → multimodal fusion → uncertainty → quality gate →
independent verification gate

## Non-negotiable controls

- Accuracy is measured, not declared.
- Weak or contradictory evidence is held for improvement.
- Independent verification is required before promotion.
- Subjective experience is never inferred directly from a signal.
- Scheduled automation cannot mutate production code.
- Every control-plane record carries a deterministic fingerprint.

## Scope

The control plane is deliberately dependency-light and deterministic so it can
run frequently in GitHub Actions without turning every five-minute cycle into
a heavyweight model-training job.

Model training, labelled experiments, sensor integrations, calibration and
external scientific replication remain separate evidence-producing stages.
