# Supreme NLP Evidence Architecture

This layer extends the existing evidence-first factory with a model-agnostic contract for translating measured observations into simple language.

## Pipeline

Sensor / source observation
→ schema validation
→ normalization
→ measured-signal description
→ hypothesis/inference boundary
→ uncertainty
→ independent validation
→ human-reviewed publication

## What the system may say

It may describe a recorded measurement, its timestamp, unit, source and processing steps.

## What the system must not silently say

A measured biological, environmental or physical signal is not automatically a subjective feeling, consciousness state, intention or experience. Such an interpretation requires an operational definition and independent validation.

## Accuracy architecture

“Supreme accuracy” is implemented as a quality target rather than a factual guarantee:

- fail-closed input contracts;
- deterministic regression tests;
- provenance and hashes;
- explicit uncertainty;
- abstention when evidence is insufficient;
- independent verification before promotion;
- human review for high-impact interpretation;
- reproducible model/version records when ML models are added.

## Future ML/NLP plug-in contract

A future model can consume the observation schema and return:

- model identifier/version;
- preprocessing configuration;
- input provenance;
- output hypothesis;
- confidence/calibration metadata;
- validation dataset/version;
- error metrics;
- known limitations;
- abstention decision.

No model output becomes VERIFIED merely because its confidence score is high.

## Research boundary

The repository may investigate whether measurable signals correlate with specific biological or environmental states. It should not pre-label such correlations as universal evidence of subjective experience.

The purpose is to make the NLP layer more powerful **without weakening the evidence boundary**.
