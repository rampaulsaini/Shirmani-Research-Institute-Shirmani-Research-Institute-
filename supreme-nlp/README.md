# Supreme NLP — Evidence-First Multimodal Interpretation

This layer extends the Research Institute without treating generated interpretations as independent scientific proof.

Pipeline: Signal -> normalization -> feature extraction -> modality agreement -> evidence grading -> interpretation -> confidence -> limitations -> audit.

## Design rules
- Fail closed when evidence is missing.
- Separate observable signals from interpretation.
- Never infer subjective experience directly from sensor data.
- Keep provenance and fingerprints for every result.
- Require independent verification before promotion to VERIFIED.
- Keep the core deterministic so optional ML/NLP models can be evaluated behind the same contract.
- Scheduled production-code mutation is disabled.

The layer is model-agnostic: later ML/NLP models can replace individual functions while preserving this evidence contract.
