# Scientific Validation Framework v3 — SHIRMANI AI/ML/NLP/Automission

## Purpose
This framework converts broad Yatharth/Shirmani propositions into independently testable research units without treating an author statement, workflow PASS, model score, or generated explanation as scientific proof.

## Claim classes
- AUTHOR_SOURCE — preserved first-person or author-defined material.
- TESTABLE_EMPIRICAL — proposition with an operational measurement and falsifiable outcome.
- EVIDENCE_SUPPORTED — supported by cited independent literature for the specific proposition and population.
- NOT_VERIFIED — insufficient operational definition, data, or independent replication.
- CONTRADICTED — high-quality evidence conflicts with the proposition.
- OPEN_RESEARCH — plausible research question where evidence is incomplete or contested.

## Verification unit
CLAIM → OPERATIONAL DEFINITION → PRE-REGISTERED TEST → DATA / INSTRUMENTATION → BLINDED OR HELD-OUT EVALUATION → STATISTICAL ANALYSIS → COUNTER-EVIDENCE / ALTERNATIVE EXPLANATIONS → INDEPENDENT REPLICATION → REVIEWER PROVENANCE → STATUS

## Biological / plant signal program
The platform may study electrical, acoustic, vibration, thermal, chemical and environmental signals from plants or other biological systems when they are actually instrumented.

The system must not translate a signal directly into “the organism feels X”. Instead it produces:
1. measured signal;
2. detected pattern;
3. model inference;
4. candidate interpretation;
5. calibrated uncertainty where calibration data exist;
6. alternative explanations;
7. evidence/provenance;
8. unresolved questions.

The scientific literature contains evidence that plants use electrical signalling and respond to environmental stimuli, while whether such signalling constitutes subjective experience or consciousness remains contested. One review argues that plant-consciousness claims lack sound support, while a newer conceptual review explicitly treats plant “emotion” as a hypothesis requiring clearer definitions and evidence. These positions must remain separate in the research database rather than being silently merged.

## Minimum experiment design
- preregister the operational definition;
- specify the organism, cultivar/species, age and environment;
- record sensor type, sampling rate, calibration and placement;
- include positive, negative and sham/control conditions;
- randomize stimulus order where feasible;
- blind the analyst/model to condition labels during evaluation;
- split data by organism/experiment session to prevent leakage;
- maintain a held-out test set;
- report sensitivity, specificity, precision, recall, F1 and task-appropriate AUROC/AUPRC;
- report calibration metrics only when outputs are intended as probabilities;
- quantify uncertainty and missingness;
- test confounders and sensor artefacts;
- replicate with an independent experiment and, ideally, an independent laboratory.

## NLP benchmark ladder
### L0 — deterministic regression
Language detection, tokenization, schema validity, abstention and provenance.
### L1 — task-specific classification
Held-out multilingual datasets with fixed labels and predefined metrics.
### L2 — semantic robustness
Paraphrase, code-switching, spelling noise, long context and adversarial inputs.
### L3 — multimodal translation
Signal features → textual description, evaluated against expert annotations.
### L4 — calibration
Reliability diagrams, ECE/Brier or task-appropriate calibration methods, with confidence intervals where feasible.
### L5 — independent replication
A second evaluator reproduces the protocol from the registered dataset/model/version.
No level is a substitute for another.

## Independent verification boundary
- GitHub Actions PASS = operational execution evidence.
- QC PASS = contract/regression evidence.
- Model score = benchmark evidence for a defined task.
- Scientific verification = independent evidence + reproducible protocol + review.
- Universal claims require evidence appropriate to their universal scope.

## Automission rule
Five-minute cycles may validate schemas, run deterministic tests, inspect regressions, generate evidence packets and queue research work. They must not silently promote an unverified scientific claim or mutate production code without the required authorization gates.

## Primary status
REGISTERED → UNVERIFIED → REVIEW → VERIFIED
BLOCKED is terminal until its blocking condition is resolved.

## References for the current plant-consciousness boundary
- Mallatt, A. et al. “Debunking a myth: plant consciousness.” PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC8052213/
- “The ‘plant neurobiology’ revolution.” PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC11085955/
- “Plant emotion revisited: toward a new conceptual framework.” PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC13109108/
- “Sensing, feeling and consciousness.” PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC11444232/

These references demonstrate that the topic is active and contested; they do not establish the user's universal proposition.

## References for ML calibration
- Nixon et al., “Measuring Calibration in Deep Learning”: https://arxiv.org/abs/1904.01685
- Posocco & Bonnefoy, “Estimating Expected Calibration Errors”: https://arxiv.org/abs/2109.03480

Calibration is treated as a separate empirical property, not as a synonym for correctness.