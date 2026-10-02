# SHIRMANI Scientific Validation Protocol

## Purpose

Convert research claims into testable hypotheses and reproducible evidence records. A claim may remain **UNVERIFIED, ABSTAIN, BLOCKED or UNRESOLVED** when instrumentation, sample size, controls, measurement quality or independent replication is insufficient.

## Claim classes

- **OBSERVATION:** directly measured or reproducibly recorded.
- **ASSOCIATION:** statistical relationship without causal proof.
- **PREDICTION:** model output tested against held-out data.
- **CAUSAL:** requires an explicit intervention, control and causal design.
- **SUBJECTIVE-EXPERIENCE:** requires operational definitions and evidence beyond a physical signal; a signal pattern alone is never sufficient.

## Production validation chain

Claim -> operational definition -> measurable variables -> instrumentation -> preregistered protocol -> protected train/evaluation split -> controls -> blinded/randomized procedure where appropriate -> held-out test -> statistical analysis -> calibration -> OOD/adversarial checks -> independent replication -> independent verification artifact -> publication record -> VERIFIED or unresolved state.

## Hard verification rules

1. A workflow passing is **never** itself evidence that a scientific claim is true.
2. Training and evaluation data must be separated, and protected test data must not be tuned against.
3. Baselines, negative controls and confounder analysis are required where applicable.
4. Alternative hypotheses must be retained when materially plausible.
5. Missing, noisy, conflicting or out-of-distribution evidence must allow **ABSTAIN**.
6. Confidence is a model property; it is not proof.
7. **VERIFIED** requires held-out evidence, protected testing, successful independent replication and an independent verification artifact.
8. The verifier must have a distinct identity/method/artifact reference and explicitly attest independence.
9. Production Automission may discover, benchmark and propose changes; it must not silently turn a hypothesis into VERIFIED.
10. Extraordinary interpretations require proportionally stronger reproducible evidence.

## Living and non-living systems

The same measurement discipline applies to plants, animals, machines, environments and other systems. A validated mapping can translate measurable patterns into plain language. The output must distinguish:

- what was measured;
- what the model predicts;
- what alternative explanations remain;
- what independently replicated;
- what remains unestablished.

This allows research into biological and non-biological signals without assuming that a signal by itself demonstrates subjective experience.

## Metrics

Track task accuracy/precision/recall/F1, calibration error and reliability, false-positive/false-negative rates, abstention coverage and selective risk, OOD detection, perturbation robustness, latency/resource use, protected-baseline regression delta and independent replication agreement.

## Verification states

**REGISTERED -> UNVERIFIED -> REVIEW -> VERIFIED**

Failure/uncertainty paths:

- **BLOCKED:** required evidence or safety gates fail.
- **ABSTAIN:** evidence is insufficient for a conclusion.

## Five-minute Automission

Observe -> Register -> Validate -> Benchmark -> Challenge -> Compare alternatives -> Audit -> Update evidence ledger -> Propose next experiment.

Production self-modification remains gated by authorization, regression evidence and independent verification.
