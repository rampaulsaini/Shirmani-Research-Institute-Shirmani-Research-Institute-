# SHIRMANI Supreme NLP — Scientific Validation Protocol v2

## Purpose

This protocol converts the project's broad Heart-View / signal-to-language objective into experimentally testable research questions without treating a philosophical proposition as an empirical fact.

The system must distinguish:
1. Observed — directly measured signal.
2. Correlated — statistically associated with a labeled condition.
3. Inferred — model-derived interpretation.
4. Hypothesis — proposed explanation requiring testing.
5. Verified — independently replicated result satisfying the preregistered gate.

## Research tracks

### A. Biological signalling
Plant and other living systems can produce measurable electrical, chemical, optical, acoustic, thermal and mechanical responses. Plant electrophysiology and impedance measurements are established research areas, and machine-learning analysis of plant electrical/impedance data is a legitimate research direction.

The system must therefore test signal classification and prediction tasks rather than assume that a signal is a subjective feeling.

### B. Subjective experience
A measurable physiological response is not by itself evidence of subjective experience. Consciousness research itself uses operational proxies and acknowledges unresolved measurement problems.

Therefore the NLP system must never transform a signal directly into a factual claim of feeling. Instead use: signal -> measured pattern -> validated association -> calibrated interpretation -> uncertainty.

### C. Quantum / biophysical hypotheses
Quantum biology is an established research field for particular biological processes, including photosynthetic energy transfer. That does not by itself establish a quantum mechanism for subjective experience or a universal quantum explanation of biological signals.

Any such claim enters the system as a HYPOTHESIS until a specific mechanism, measurable prediction, experiment, controls and independent replication exist.

## Minimum experimental design

- preregister the target label and operational definition;
- record sensor/device model and calibration;
- timestamp every observation;
- randomize or counterbalance experimental conditions where applicable;
- include sham/control recordings;
- blind the classifier evaluator to condition labels where feasible;
- split data by specimen/individual/experiment, not only by rows;
- keep a held-out test set untouched until final evaluation;
- report sensitivity, specificity, precision, recall, F1 and calibration;
- report confidence intervals where sample size permits;
- report false-positive and false-negative examples;
- test robustness to sensor drift, batch effects and environmental confounders;
- reproduce the result using an independent dataset or laboratory before VERIFIED.

## Anti-leakage rule

No specimen, experiment session, duplicated recording, near-duplicate window or preprocessing artifact may occur in both training and final test partitions.

## Independent verification gate

A claim can become VERIFIED only when all of these are satisfied: predefined hypothesis; adequate provenance; independent test; predefined metric threshold; counter-evidence check; reproducible artifact; independent reviewer; replication.

Model agreement is not independent verification.

## NLP output contract

The language layer must explicitly separate:
- What was measured
- What pattern was detected
- What the model predicts
- Evidence supporting the prediction
- Alternative explanations
- What remains unknown
- Confidence / calibration
- Verification state

Preferred wording:
"The measured signals show pattern X under condition Y. In the evaluated dataset, the model predicts class Z with calibrated probability P. This is evidence for an association between the measured pattern and Z; it is not, by itself, evidence of subjective experience."

## Research status

This protocol is an implementation and validation framework. It does not assert that the project's broader philosophical propositions have already been scientifically verified.
