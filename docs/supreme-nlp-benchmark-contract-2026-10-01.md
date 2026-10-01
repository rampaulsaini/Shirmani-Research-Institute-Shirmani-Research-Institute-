# SHIRMANI Supreme NLP Benchmark Contract — 2026-10-01

## Purpose

Turn the Supreme NLP Practitioner target into a measurable continuous-evaluation system. The benchmark does not declare perfect or “fully supreme” accuracy; it records measurable performance, uncertainty, regression and evidence coverage.

## Evaluation dimensions

1. Signal fidelity — whether the extracted representation preserves the measured input.
2. Semantic accuracy — correctness against task-specific labeled evaluation data.
3. Multimodal consistency — agreement across available modalities without silently inventing missing signals.
4. Plain-language fidelity — whether the explanation remains faithful to the model output.
5. Calibration — whether confidence corresponds to observed correctness.
6. Uncertainty discipline — whether unknown or unsupported conclusions remain explicitly unknown.
7. Evidence traceability — whether outputs link to source/provenance records.
8. Robustness — performance under controlled perturbations and distribution shifts.
9. Regression safety — whether a new model/version degrades protected benchmark slices.
10. Verification separation — whether model/QC success is kept distinct from independent verification.

## Biological / environmental interpretation

For living organisms, plants and non-living systems, the benchmark evaluates translation of instrumented, observable signals into language. It does not treat a detected signal as automatic proof of subjective feeling, consciousness, intention or inner experience.

Each evaluated record must preserve the sequence: measured signal → representation → model inference → interpretation → confidence → evidence → uncertainty.

## Required benchmark record

Each future model evaluation should be traceable to: benchmark version; model/version identifier; dataset/evaluation-set fingerprint; task and population; metric definitions; sample count; result; uncertainty interval or equivalent qualification; baseline; regression comparison; provenance; verification state.

## Gates

- Missing benchmark metadata → BLOCK.
- Missing evaluation evidence → UNVERIFIED.
- Missing provenance → BLOCK.
- Unsupported confidence claim → BLOCK.
- Regression beyond the configured tolerance → REVIEW.
- Independent verification is never inferred from automated QC.

## Five-minute operating integration

Observe → Collect → Normalize → Analyze → Reason → Translate → Benchmark → Verify → Audit → Learn → Improve

## Definition of progress

Progress means a reproducible improvement in one or more measured dimensions without unacceptable regression in protected dimensions. “Khraab/arb guna better” or “supreme accuracy” remains a project goal unless measurable evidence establishes it.
