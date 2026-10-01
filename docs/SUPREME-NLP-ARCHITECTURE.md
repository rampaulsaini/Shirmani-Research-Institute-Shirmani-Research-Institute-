# Supreme NLP — Evidence-First Signal Intelligence

## Objective

Build a high-throughput multimodal NLP control plane that can transform
observable signals from people, animals, plants, materials, devices and
environments into simple natural-language descriptions without converting
uncertain inference into fact.

## Pipeline

Observe → Normalize → Fingerprint → Extract Features → Generate Hypotheses →
Translate to Plain Language → Independently Verify → Audit → Learn

### Evidence contract

Every interpretation must retain:

- source and capture timestamp
- modality and units
- deterministic evidence hash
- explicit hypotheses
- confidence in the interpretation
- evidence level
- limitations
- verification status

### Signal-to-language principle

A system may say:

> “The measured signal shows pattern X, which is associated with hypothesis Y
> in the evaluated data.”

It must not silently transform that into:

> “The subject definitely feels Y.”

Subjective experience requires evidence appropriate to that claim. Sensor
measurements can be analyzed without assuming that a detected pattern proves
conscious experience.

## Agent topology

1. **Perception Agent** — ingests multimodal observations.
2. **Feature Agent** — normalizes and extracts reproducible features.
3. **NLP Agent** — maps features and context into candidate descriptions.
4. **Evidence Agent** — attaches provenance and supporting records.
5. **Contradiction Agent** — searches for competing explanations.
6. **Verification Agent** — independently checks the interpretation.
7. **Audit Agent** — checks traceability, schema validity and confidence.
8. **Learning Agent** — proposes model/data improvements; it cannot promote
   unverified claims directly to VERIFIED.

## Accuracy policy

No component may declare “fully supreme accuracy” from architecture alone.
Accuracy is an empirical property measured on representative, labeled and
independently evaluated data.

Required metrics can include:

- classification accuracy / F1
- calibration error
- false-positive and false-negative rates
- robustness under noise
- cross-source reproducibility
- out-of-distribution detection
- latency and throughput
- verification agreement rate

## Controlled self-improvement

Automission may propose code, model, prompt, schema or dataset changes.
Promotion requires tests, provenance, independent evaluation and a fail-closed
verification gate.
