# SHIRMANI Scientific Validation Protocol v2

## Purpose
This protocol converts signal-to-language research into a reproducible scientific evaluation pipeline.

Evidence states:
1. Observed — directly measured data.
2. Inferred — a model-derived pattern or classification.
3. Interpreted — a plain-language description of the inferred pattern.
4. Verified — a result that survives the predefined independent verification gate.

A model output, confidence score, benchmark pass, workflow success, or user interpretation is not by itself evidence of subjective experience, consciousness, intention, or emotion.

## Required study design
Every scientific claim must register:
- precise operational definition;
- target population and sampling frame;
- sensors/instruments and calibration method;
- preprocessing version;
- model/version and locked inference configuration;
- primary endpoint and metric;
- predefined inclusion/exclusion rules;
- positive controls and negative controls;
- blinded holdout data;
- independent replication plan;
- counter-evidence criteria;
- stopping rule and analysis plan.

## Validation ladder
### Gate A — Instrument validity
Demonstrate that the measurement system detects the physical signal it claims to measure.

### Gate B — Signal reliability
Test repeatability, missingness, noise, drift, calibration and inter-device agreement.

### Gate C — Task validity
Evaluate the exact prediction/translation task against blinded labelled data.

### Gate D — Generalisation
Use a locked holdout population not used for model development or threshold selection.

### Gate E — Independent replication
A separate operator, dataset, instrument or laboratory reproduces the predefined analysis.

### Gate F — Adversarial and counter-evidence testing
Test alternative explanations, confounds, leakage, class imbalance, batch effects and negative controls.

### Gate G — Independent review
Only an independent reviewer can assign VERIFIED status. Automation may calculate eligibility and produce a report; it cannot manufacture an independent decision.

## Required metrics
Classification: accuracy, balanced accuracy, precision/recall/F1, confusion matrix, AUROC/AUPRC where applicable, confidence calibration (ECE/Brier), and abstention/error rate.

Regression: MAE/RMSE, correlation where justified, calibration/coverage for intervals, and error by subgroup/acquisition condition.

Signal processing: SNR, test-retest reliability, drift, missingness, and inter-device/inter-session agreement.

Report confidence intervals and the predefined statistical method. Never replace uncertainty with a single headline accuracy number.

## NLP translation rule
The system must translate only what the measured evidence supports.

Preferred:
"Measured signal X changed in pattern Y under condition Z. The trained model associates this pattern with label L with confidence C on the specified evaluation population."

Do not turn a signal pattern into a direct claim that a plant, object or animal feels something unless that claim has a separately validated operational definition and the study actually measures it.

## Scientific status
UNVERIFIED is the default.

VERIFIED requires all registered gates, reproducibility evidence, reviewed counter-evidence, audit provenance and an explicit independent reviewer decision.

A high benchmark score on a tiny or synthetic fixture remains a regression result, not scientific verification.
