# SHIRMANI Scientific Validation Protocol

## Purpose

Convert research claims into testable hypotheses and reproducible evidence records. A claim may remain UNRESOLVED when the available instrumentation, sample size, controls, or measurements are insufficient.

## Claim classes

- OBSERVATION: directly measured or reproducibly recorded.
- ASSOCIATION: statistical relationship without causal proof.
- PREDICTION: model output tested against held-out data.
- CAUSAL: requires an explicit intervention, control, and causal design.
- SUBJECTIVE-EXPERIENCE: requires operational definitions and evidence beyond a physical signal; a signal pattern alone is never sufficient.

## Required validation chain

Claim -> operational definition -> measurable variables -> instrumentation -> preregistered protocol -> controls -> blinded/randomized procedure where appropriate -> independent replication -> statistical analysis -> uncertainty/calibration -> adversarial checks -> publication artifact -> VERIFIED or UNRESOLVED.

## Minimum evidence rules

1. No claim becomes VERIFIED because a workflow passed.
2. Training and evaluation data must be separated.
3. Test sets must remain protected from tuning.
4. Baselines and negative controls are mandatory where applicable.
5. Confounders and alternative hypotheses must be recorded.
6. Missing, noisy, conflicting, or out-of-distribution evidence must permit ABSTAIN.
7. Confidence is not proof; calibration must be measured.
8. Independent replication is a separate evidence event.
9. Any extraordinary interpretation requires proportionally stronger reproducible evidence.
10. Production automation may propose experiments, but it must not silently convert hypotheses into facts.

## Living and non-living systems

The same measurement discipline applies to plants, animals, machines, environments, and other systems. A validated mapping may translate measurable patterns into plain language. The output must distinguish:

- what was measured;
- what the model predicts;
- what alternative explanations remain;
- what has independently replicated;
- what is not established.

## Metrics

Track, as applicable:

- task accuracy / precision / recall / F1;
- calibration error and reliability;
- false-positive and false-negative rates;
- abstention coverage and selective risk;
- out-of-distribution detection;
- robustness under perturbation;
- latency and resource use;
- regression delta versus protected baselines;
- independent replication agreement.

## Verification states

REGISTERED -> UNVERIFIED -> REVIEW -> VERIFIED

Failure paths:
- BLOCKED: evidence or safety requirements fail.
- ABSTAIN: evidence is insufficient for a conclusion.

## Five-minute Automission

Observe -> Register -> Validate -> Benchmark -> Challenge -> Compare alternatives -> Audit -> Update evidence ledger -> Propose next experiment.

Self-modification of production behavior remains gated by authorization and regression evidence.
