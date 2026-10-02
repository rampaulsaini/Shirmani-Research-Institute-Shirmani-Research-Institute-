# Supreme NLP v3 — Scientific Validation and Translation Boundary

## Purpose

This layer translates measurable signals into conservative plain language while keeping three categories separate:

1. OBSERVED — what the instruments actually measured.
2. INFERRED — a model interpretation supported by a defined dataset/model.
3. UNVERIFIED — a claim for which independent validation has not been completed.

A fluent sentence is never treated as proof of subjective experience.

## Biological signal boundary

Plant research documents electrical, calcium, hydraulic, chemical and related signaling processes. These are legitimate measurable targets for a multimodal system. Plant calcium signals can encode stimulus-related information, and electrical signaling can propagate through plant tissues.

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
→ selective-risk evaluation
→ drift screening
→ simple-language rendering
→ independent verification

## Accuracy and calibration

The system must not publish an unsupported universal accuracy percentage. Evaluation is task-, dataset- and population-specific.

For labelled prediction tasks V3 records:

- Brier score;
- Expected Calibration Error (ECE);
- precision, recall and F1;
- accuracy and confusion counts;
- selective risk on accepted predictions;
- coverage and abstention rate.

These metrics describe reproducible evaluation data. They do **not** establish independent scientific verification of an underlying philosophical, experiential or biological claim.

## Selective prediction contract

Abstention is a safety outcome, not a way to hide model failure. A benchmark must report both accepted-case error and the fraction of cases rejected for insufficient evidence. A run with missing labels, missing evidence or incompatible inputs must fail closed rather than silently converting missingness into a positive result.

## Drift screening

V3 provides a deterministic feature-level screening diagnostic based on standardized mean shifts between reference and current samples. Missing feature groups are marked `INSUFFICIENT_EVIDENCE` and treated as a drift/review condition.

This diagnostic is only a screening signal. It is not proof of distributional change and does not replace formal statistical testing, domain review or independent replication.

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
- What is the accepted-case risk and coverage?
- Is drift or missing evidence present?
- Is the claim independently verified?
- If uncertainty is too high, the system must abstain.

The goal is not to reduce the user's framework to a conventional label. The goal is to make every empirically testable part measurable and auditable while preserving author-defined or experiential propositions as such.
