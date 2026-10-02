# SHIRMANI Supreme NLP Evaluation & Accuracy Contract

## Purpose

Turn the Supreme NLP Practitioner architecture into a measurable evaluation system. The repository must distinguish **architecture readiness** from **measured model performance**.

## Evaluation dimensions

1. **Semantic correctness** — whether the output preserves the meaning of the input.
2. **Intent classification** — task-specific precision, recall and F1.
3. **Entity / concept extraction** — precision, recall and F1.
4. **Multilingual consistency** — semantic agreement across supported languages.
5. **Signal-to-language interpretation** — agreement with expert-labelled signal states for instrumented datasets.
6. **Calibration** — whether confidence corresponds to observed correctness.
7. **Robustness** — performance under noise, missing fields, perturbations and adversarial inputs.
8. **Provenance fidelity** — every evidence-bearing output must resolve to traceable source records.
9. **Abstention quality** — the system must abstain when evidence is insufficient rather than invent an interpretation.
10. **Regression safety** — new versions must not silently degrade protected benchmark suites.

## Required benchmark record

Each benchmark run should record:

- benchmark_id
- dataset_id and immutable dataset fingerprint
- model/provider identifier
- model/version identifier
- task and language
- sample count
- metric definitions
- measured metrics
- confidence/calibration result where applicable
- error count and representative error classes
- baseline comparison
- regression result
- provenance
- timestamp

## Biological, plant and environmental signal boundary

The platform may translate measurable signals into plain language, but a signal-to-language result is an **inference** unless an independently validated ground truth supports a stronger conclusion.

The output contract is:

**measured signal → detected pattern → model inference → interpretation → confidence → evidence → unresolved uncertainty**

The system must not transform a sensor pattern into a statement that an organism has a particular subjective feeling, consciousness, intention or inner experience unless the benchmark and evidence actually establish that proposition.

## Accuracy gate

The repository must never label a model “fully supreme accuracy” merely because a workflow succeeds.

A performance claim requires:

**defined task + defined population/dataset + metric + measured result + baseline + uncertainty + reproducible evaluation record.**

## Fail-closed evaluation

- Missing dataset fingerprint → BLOCK.
- Missing model/version identity → BLOCK.
- Missing metric definition → BLOCK.
- Missing provenance → BLOCK.
- Unsupported confidence claim → BLOCK.
- Failed protected benchmark → REGRESSION.
- Insufficient evidence → ABSTAIN / NOT_VERIFIED.

## Five-minute Automission evaluation loop

Observe → Collect → Normalize → Evaluate → Diagnose → Test → Verify → Audit → Record → Compare → Improve

The five-minute schedule is an execution cadence, not proof that an external model is continuously available.

## Human gate

High-impact deployment, irreversible changes, financial actions and promotion of an independently verified status require explicit authorization under the existing governance contract.
