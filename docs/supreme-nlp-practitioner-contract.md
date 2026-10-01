# Supreme NLP Practitioner — Signal-to-Language Contract

## Purpose
Define a rigorous interface for converting measurable multimodal signals into simple natural-language explanations while preserving uncertainty and provenance.

## Core pipeline
`Acquire → Calibrate → Clean → Segment → Extract Features → Model → Fuse Context → Infer → Explain → Verify → Archive`

## Input classes
- text and speech
- image and video
- environmental measurements
- acoustic/vibration measurements
- electrical/biophysical measurements where technically and ethically appropriate
- time-series sensor data
- machine telemetry

## Output contract
Every interpretation should expose:
1. **OBSERVED** — what was actually measured.
2. **MODEL_INFERENCE** — what the model predicts or classifies.
3. **INTERPRETATION** — the plain-language rendering.
4. **CONFIDENCE** — calibrated confidence or an unavailable state.
5. **ALTERNATIVES** — plausible competing explanations where relevant.
6. **LIMITATIONS** — noise, calibration limits, distribution shift, or insufficient data.
7. **PROVENANCE** — source, model/version, timestamp, preprocessing and artifact hash.
8. **VERIFICATION** — independent check status.

## Living-organism and plant signals
The system may learn correlations between measurable biological/environmental signals and observed states. It must not convert a correlation into an unsupported claim that a plant, animal, object, or system subjectively "feels" something.

Preferred language:
> "The measured signal pattern is associated with X in the available reference data."

A stronger claim requires its own reproducible evidence and independent verification record.

## Supreme accuracy principle
"Fully supreme accuracy" is an engineering target, not a value to be declared in advance.

Track, where applicable:
- accuracy / precision / recall / F1
- calibration error
- false-positive and false-negative rates
- robustness under noise
- out-of-distribution detection
- latency
- reproducibility
- independent verification rate

## Agent roles
- **Perception Agent:** validates inputs.
- **ML Agent:** trains/evaluates models.
- **NLP Agent:** converts structured inference to natural language.
- **Evidence Agent:** links claims to measurements and sources.
- **Verification Agent:** independently challenges results.
- **Security Agent:** checks permissions, dependencies and unsafe actions.
- **Audit Agent:** records provenance and regression outcomes.
- **Automission Supervisor:** schedules, observes and stops failed pipelines.

## Fail-closed rule
No missing evidence is silently promoted to VERIFIED. No generated artifact becomes an authoritative source merely because an automated workflow succeeded.
