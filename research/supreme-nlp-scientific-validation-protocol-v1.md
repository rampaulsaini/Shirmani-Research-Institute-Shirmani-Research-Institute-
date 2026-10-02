# Supreme NLP Scientific Validation Protocol v1

## Purpose

This protocol converts the Supreme NLP / signal-to-language idea into falsifiable, reproducible experiments. It separates measured observations, model inferences, and claims about subjective experience.

## Claim classes

1. **OBSERVATION** — a sensor or instrument measured a defined signal.
2. **PHYSIOLOGICAL_INFERENCE** — a validated model links a signal pattern to a defined physiological state.
3. **BEHAVIOURAL_OR_FUNCTIONAL_PREDICTION** — the model predicts a measurable future response better than a pre-registered baseline.
4. **SUBJECTIVE_EXPERIENCE** — a claim about felt experience, consciousness, intention, or emotion. This class is blocked by default and requires a separately defined scientific operationalization; signal detection alone is insufficient evidence.

## Required evidence record

- operational definition
- subject/species/system
- instrumentation and calibration
- raw-data provenance
- sampling rate and preprocessing
- preregistered primary endpoint
- training/validation/test split
- blinded or otherwise protected evaluation where feasible
- baseline/control condition
- confounders and alternative explanations
- effect size and uncertainty interval
- failure cases and counter-evidence
- independent replication
- reviewer identity/role and timestamp
- immutable evidence/task hash

## Plant / living-system track

The repository may ingest electrical, calcium/ROS, hydraulic, chemical, temperature, light, acoustic/vibration and environmental measurements.

The system must report:

measured signal -> detected pattern -> physiological hypothesis -> predicted outcome -> observed outcome -> replication status

It must never silently transform:

signal -> organism feels X

without an independently validated operational bridge.

## NLP evaluation

For each task, report at minimum:

- precision, recall, F1 where classification applies
- calibration error and Brier score for probabilistic outputs
- false-positive and false-negative rates
- abstention rate
- robustness under sensor noise and distribution shift
- cross-source agreement
- out-of-domain performance
- reproducibility across independent runs

A confidence number is not a scientific probability until calibration has been demonstrated on an appropriate labelled evaluation set.

## Independent verification gate

EVIDENCE_COLLECTION -> INDEPENDENT_TEST -> REPRODUCIBLE_RESULT -> COUNTERCASE_REVIEW -> AUDIT -> VERIFIED

Automission can prepare evidence and execute deterministic tests. It must not declare a scientific claim VERIFIED by workflow success alone.

## External scientific alignment

This protocol is designed to align with established AI test/evaluation/verification/validation principles, including NIST AI RMF and its TEVV work, while remaining specific to this repository.

Relevant background includes published reviews of plant electrical and chemical signalling and current multimodal emotion-recognition research. These sources support the existence of measurable signalling and multimodal inference methods; they do not constitute evidence for any particular metaphysical or subjective-experience claim.

## Decision states

- SUPPORTED_BY_DATA
- REVIEW
- UNVERIFIED
- BLOCKED
- VERIFIED_BY_INDEPENDENT_REVIEW

Only the final state may enter the VERIFIED registry, and only when every required evidence field and independent-review condition is satisfied.