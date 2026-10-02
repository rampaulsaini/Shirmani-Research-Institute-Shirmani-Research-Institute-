# Supreme NLP v3 — Scientific Validation and Translation Boundary

## Purpose

This layer translates measurable signals into conservative plain language while keeping three categories separate:

1. OBSERVED — what the instruments actually measured.
2. INFERRED — a model interpretation supported by a defined dataset/model.
3. UNVERIFIED — a claim for which independent validation has not been completed.

A fluent sentence is never treated as proof of subjective experience.

## Biological signal boundary

Plant research documents electrical, calcium, hydraulic, chemical and related signaling processes. These are legitimate measurable targets for a multimodal system. Plant calcium signals can encode stimulus-related information, and electrical signaling can propagate through plant tissues. citeturn0search13turn0search11

That evidence does **not**, by itself, establish that a plant experiences a human-like subjective feeling. Therefore the NLP output must say what was measured, what pattern was inferred, what remains unknown, and what experiment could distinguish competing explanations.

## V3 measurement pipeline

OBSERVATION
→ quality control
→ provenance
→ temporal/baseline features
→ cross-modal comparison
→ model inference
→ abstention check
→ uncertainty/calibration
→ simple-language rendering
→ independent verification

## Accuracy and calibration

The system must not publish an unsupported universal accuracy percentage. NIST emphasizes context-specific measurement, uncertainty, robustness and evaluation, and its current AI evaluation work includes model testing, red teaming and user testing. citeturn0search0turn0search1

For labelled prediction tasks V3 records Brier score and Expected Calibration Error (ECE). For scientific measurements, uncertainty must remain explicit rather than being hidden inside a confidence number; NIST guidance treats uncertainty as part of defensible measurement reporting. citeturn0search9turn0search16

## Required independent experiments

For any proposed “signal → state” interpretation:

- preregister the operational definition;
- collect blinded/controlled observations;
- include negative controls and sham/sensor controls;
- split train/validation/test data by experiment or specimen where appropriate;
- prevent leakage between repeated measurements;
- compare against a simple baseline;
- report sensitivity, specificity, precision/recall where classification applies;
- report calibration and uncertainty;
- test distribution shift;
- publish counter-evidence;
- replicate independently;
- preserve raw data, preprocessing version, model version and hashes.

## NLP output contract

Every high-stakes biological interpretation should expose:

- What was measured?
- What pattern was detected?
- What model/data support the interpretation?
- What alternative explanations remain?
- Is the result calibrated?
- Is the claim independently verified?
- If uncertainty is too high, the system must abstain.

The goal is not to reduce the user's framework to a conventional label. The goal is to make every empirically testable part measurable and auditable while preserving author-defined or experiential propositions as such.
