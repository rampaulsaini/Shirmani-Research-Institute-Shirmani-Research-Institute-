# SHIRMANI Scientific Validation & Independent Replication Protocol

## Purpose

Convert author-proposed Heart-View / Yatharth propositions and multimodal NLP hypotheses into testable scientific propositions without silently treating experience, interpretation, metaphor, or project terminology as established scientific fact.

This protocol extends the existing Source → Claims → Evidence → Formulation/Test → Verification → QC → Publication → Archive architecture.

## Evidence classes

1. AUTHOR_CLAIM — preserved verbatim as a source claim.
2. LITERATURE_SUPPORTED — supported by identified external literature.
3. MEASUREMENT — directly instrumented observation with provenance.
4. MODEL_INFERENCE — statistical/ML output derived from measurements.
5. REPLICATION — independently reproduced result under a declared protocol.
6. VERIFIED — only after the defined independent-verification gate passes.

A workflow PASS is never equivalent to scientific verification.

## Hypothesis contract

Every scientific test must declare:

- hypothesis and operational definition;
- target population/system;
- observable variables;
- measurement instrument and calibration;
- inclusion/exclusion criteria;
- control/comparison condition;
- primary endpoint;
- secondary endpoints;
- statistical/evaluation method;
- minimum sample size or justified stopping rule;
- preregistration timestamp/version;
- dataset and code fingerprints;
- blinding/randomization where applicable;
- expected failure modes;
- uncertainty/confidence interval or calibrated uncertainty;
- replication requirement;
- independent verifier identity/process;
- limitations and competing explanations.

## Biological / plant / non-living signal boundary

Instrumented signals may be analyzed and translated into natural language. Examples include electrical, acoustic, vibration, thermal, chemical, motion and environmental measurements.

The system must not infer subjective feeling, consciousness, intention or a human-like emotional state solely from a signal pattern.

Instead it should output:

**Measurement → Pattern → Statistical/model inference → Plain-language interpretation → Confidence/uncertainty → Alternative explanations → Unknowns.**

For example:

> “A repeatable signal pattern was detected during condition X. The current model associates it with Y with calibrated uncertainty Z. This does not establish subjective experience or intention.”

Plant research already demonstrates that plants can produce measurable chemical responses to stress, while temporal resolution matters for interpreting those signals; this supports measurement research, not an automatic inference of human-like subjective feeling. citeturn0search7

## Independent verification

Independent verification must use:

- a separately generated analysis environment or reviewer;
- frozen dataset/protocol version;
- no access to the candidate's hidden labels during primary evaluation where feasible;
- independent recomputation of metrics;
- provenance/hash checks;
- contradiction and negative-control checks;
- documented acceptance criteria;
- signed or otherwise traceable verification evidence.

The original author, model, workflow, or agent cannot verify its own claim merely by repeating its own result.

## Replication ladder

LEVEL 0 — internal deterministic test  
LEVEL 1 — held-out test set  
LEVEL 2 — independent dataset  
LEVEL 3 — independent analyst/reimplementation  
LEVEL 4 — independent laboratory/team replication  
LEVEL 5 — cross-context/generalization

Promotion must record the highest completed level rather than collapsing all levels into “verified”.

## Statistical discipline

For quantitative claims record, where applicable:

- effect size;
- uncertainty/confidence interval;
- sample size;
- missing-data treatment;
- multiple-comparison handling;
- calibration/error metrics;
- subgroup/slice performance;
- sensitivity analysis;
- negative controls;
- robustness to reasonable perturbations.

A large numerical improvement on one benchmark is not evidence of universal superiority.

## AI/NLP TEVV

NLP and agent systems should be evaluated separately for:

- factuality;
- semantic fidelity;
- calibration;
- hallucination rate;
- abstention quality;
- robustness;
- multilingual performance;
- domain shift;
- adversarial/ambiguous input;
- provenance preservation;
- explanation consistency;
- safety and governance compliance.

NIST's current AI evaluation work explicitly frames Test, Evaluation, Verification and Validation as applicable to statistical ML, LLMs, multimodal models and agentic systems. citeturn0search4

## Fail-closed rules

BLOCK promotion when:

- preregistration is absent for a claim requiring prospective testing;
- primary endpoint is changed after seeing results without explicit disclosure;
- provenance is incomplete;
- required controls fail;
- independent verification is missing;
- contradictory evidence is hidden;
- benchmark/test data are contaminated;
- uncertainty is omitted where material;
- the system converts signal into subjective-experience claims without evidence.

## Scientific status vocabulary

PROPOSED → PREREGISTERED → MEASURED → ANALYZED → REPLICATED → INDEPENDENTLY_VERIFIED

Also:

UNVERIFIED — evidence exists but the independent gate is incomplete.

CONTRADICTED — credible evidence conflicts with the proposition.

INCONCLUSIVE — available evidence cannot resolve the proposition.

BLOCKED — integrity/safety/evidence requirements prevent promotion.

These states are deliberately descriptive rather than rhetorical.

## Governance

Automission may discover, structure, test, compare and propose improvements. It must not silently rewrite the scientific acceptance criteria, fabricate evidence, or promote its own output to VERIFIED.

NIH guidance emphasizes rigor, transparency and reproducibility, including independent replication as a mechanism for validating findings. citeturn0search0turn0search3
