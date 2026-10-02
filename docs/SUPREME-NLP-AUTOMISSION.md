# Supreme NLP + Automission

This layer extends the existing Heart-View/Research Factory without replacing its
fail-closed verification gates.

## Pipeline

observe -> normalize -> quality -> feature extraction -> interpretation -> NLP -> audit -> improvement

The baseline implementation accepts observable multimodal records (for example
sensor, audio, image-derived or environmental features) and converts them into
simple Hindi language. It explicitly separates **signal interpretation** from
claims about subjective experience.

## Accuracy contract

No software component in this repository may honestly guarantee absolute or
"fully supreme" accuracy. Accuracy must be measured on labelled test data,
calibration sets, independent validation and regression suites.

The layer therefore reports:
- evidence grade;
- signal quality;
- agreement/disagreement;
- model confidence;
- limitations;
- deterministic fingerprint.

## Automission contract

Every five-minute cycle may audit the current status and produce an improvement
plan. Improvement recommendations are advisory unless repository governance
and verification gates authorize a code change. Existing publication and
independent-verification gates remain authoritative.

## Biological/physical interpretation

A model can translate measured signals into language such as "high variability
pattern". That does not establish that a plant, animal or object experienced
a human-like emotion. Establishing such a claim requires a domain-specific
operational definition, controlled experiments, labelled data, independent
replication and appropriate scientific review.


## Multimodal Supreme NLP extension (2026-10-02)

The continuous layer now includes a formal observation schema, multimodal regression tests and a synthetic benchmark. It converts registered observable signals into simple-language descriptions while preserving confidence, provenance, limitations and an explicit UNVERIFIED boundary.

The system does not treat a signal as direct evidence of subjective experience. Stronger claims require labelled evaluation, domain calibration and independent replication.
