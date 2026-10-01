# SHIRMANI Supreme NLP Architecture

## Continuous objective

The system is being extended from ordinary text routing toward an auditable
multimodal pipeline:

**observe → normalize → quality-check → feature extraction → ML/model layer →
semantic interpretation → simple-language NLP → provenance → independent
verification → Automission audit**

## Multimodal boundary

Signals may include text, speech/audio, image/video, vibration, temperature,
humidity, light, motion, electrical and chemical measurements.

The NLP layer may describe patterns in those observations. It must not silently
turn a sensor pattern into proof of subjective emotion, consciousness or a
specific internal experience.

## Confidence

Confidence is treated as an evidence-quality quantity unless and until it has
been calibrated on labelled evaluation data. An uncalibrated confidence value
must remain explicitly marked **UNCALIBRATED**.

## ML extension contract

A future learned model must preserve:

- input/source identifiers and fingerprints
- model name and version
- training/evaluation dataset identity
- evaluation metrics and calibration status
- uncertainty and abstention behavior
- counter-evidence/disagreement
- independent verification status

## Multilingual NLP

The deterministic router now recognizes multiple Unicode script families and
routes them to language-specific queues. Script detection is only a routing
signal; it is not treated as proof of language, emotion, intent or consciousness.
Lexical/contextual models may refine the route while retaining verification.

## Automission

The Supreme NLP workflow runs every five minutes and performs contract/QC
validation. Workflow success is not independent scientific verification.
Production-code mutation and verification promotion remain behind the existing
fail-closed governance boundary.
