# SHIRMANI Supreme NLP — Evaluation & Accuracy Standard

## Purpose
Define measurable evaluation gates for the Supreme NLP Practitioner without claiming unearned perfect accuracy.

## Evaluation dimensions
Every model/version evaluation should record:
- task and intended use;
- dataset/version and fingerprint;
- population/scope;
- baseline;
- metrics;
- sample count;
- confidence/uncertainty method;
- error categories;
- regression comparison;
- provenance;
- verification status.

## Required metrics by task
Classification: accuracy, macro-F1, per-class recall/precision, confusion matrix, and calibration when probabilities are available.

Speech/audio: word error rate or task-specific recognition metric, signal-quality coverage, and failure categories.

Translation/plain-language interpretation: semantic agreement, factual consistency, omission/addition checks, and human evaluation where appropriate.

Multimodal signal interpretation: signal-quality pass rate, detection metric, false-positive/false-negative analysis, temporal robustness, and cross-sensor consistency.

Retrieval/evidence grounding: Recall@k or equivalent retrieval metric, source-resolution rate, and unsupported-claim rate.

## Accuracy gate
The platform must not label a model “fully supreme accurate” merely because a workflow passed.

Release states:
- READY_FOR_EVALUATION — contracts and test wiring exist;
- EVALUATED — defined benchmark results exist;
- REGRESSION_PASS — current model meets the configured regression gate;
- VERIFIED — independent verification evidence exists.

These states are distinct.

## Biological and environmental interpretation
Signals from living organisms, plants, environments or non-living systems may be translated into plain language only through measurable observations and model inference.

The output must preserve:
measured signal → detected pattern → model inference → interpretation → confidence → evidence → unresolved uncertainty

No sensor pattern alone establishes subjective feeling, consciousness or intention.

## Fail-closed release rule
Missing benchmark evidence, missing provenance, failed regression checks, contradictory evidence or unresolved safety/integrity failures prevent a VERIFIED status.

## Continuous improvement record
Each evaluation cycle should preserve model version, dataset fingerprint, metrics, errors, regression result and timestamp so improvement can be demonstrated quantitatively.
