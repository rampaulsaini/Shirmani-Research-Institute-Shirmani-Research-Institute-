# Supreme NLP — Evidence-First Signal Intelligence

## Objective

Build a high-throughput multimodal NLP control plane that transforms
observable signals from people, animals, plants, materials, devices and
environments into simple natural-language descriptions without converting
uncertain inference into fact.

The architecture optimizes for **measurable accuracy, traceability, latency,
robustness and reproducibility** rather than an unverified claim of perfect
accuracy.

## Pipeline

Observe → Validate → Normalize → Fingerprint → Extract Features →
Generate Hypotheses → Translate to Plain Language → Contradiction Check →
Independent Verification → Audit → Learn

### Evidence contract

Every observation and interpretation must retain:

- source and capture timestamp
- modality and units where applicable
- deterministic SHA-256 evidence fingerprint
- explicit hypotheses
- confidence in the interpretation
- evidence level
- limitations
- explicit verification status

Non-finite numeric values are rejected before fingerprinting. This prevents
NaN/Infinity payloads from entering an evidence record that cannot be
represented consistently by the JSON schema.

### Signal-to-language principle

A system may say:

> “The measured signal shows pattern X, which is associated with hypothesis Y
> in the evaluated data.”

It must not silently transform that into:

> “The subject definitely feels Y.”

Subjective experience requires evidence appropriate to that claim. Sensor
measurements can be analyzed without assuming that a detected pattern proves
conscious experience.

### Verification states

Interpretations begin as **UNVERIFIED**.

Only an independent verification layer may move an interpretation to
**INDEPENDENTLY_VERIFIED**, and a failed verification may mark it
**REJECTED**. The NLP generation step itself never promotes an interpretation
to verified status.

## Agent topology

1. **Perception Agent** — ingests multimodal observations.
2. **Validation Agent** — rejects malformed, non-finite or unsupported input.
3. **Feature Agent** — normalizes and extracts reproducible features.
4. **NLP Agent** — maps features and context into candidate descriptions.
5. **Evidence Agent** — attaches provenance and supporting records.
6. **Contradiction Agent** — searches for competing explanations.
7. **Verification Agent** — independently checks the interpretation.
8. **Audit Agent** — checks traceability, schema validity and confidence.
9. **Learning Agent** — proposes model/data improvements; it cannot promote
   unverified claims directly to VERIFIED.

## Accuracy policy

No component may declare “fully supreme accuracy” from architecture alone.
Accuracy is an empirical property measured on representative, labeled and
independently evaluated data.

Required metrics can include:

- accuracy / precision / recall / F1 where appropriate
- calibration error and confidence reliability
- false-positive and false-negative rates
- robustness under controlled noise
- cross-source and cross-session reproducibility
- out-of-distribution detection
- latency and throughput
- verification agreement rate
- abstention quality when evidence is insufficient

## Automission policy

Automission can continuously propose code, model, prompt, schema or dataset
improvements. Promotion remains fail-closed:

**propose → test → evaluate → independently verify → audit → promote**

A faster cycle is not automatically a better cycle. Parallel, deterministic
checks are preferred over simply increasing workflow frequency, especially in a
repository already running many automated workflows.

## Research direction

For plant, animal, environmental or material signals, the system should build
empirical datasets linking measurable signal patterns to experimentally
validated states. Natural-language output should preserve the distinction
between:

**measurement → statistical association → validated interpretation → claim**

This keeps the NLP layer scientifically testable while allowing increasingly
rich multimodal signal-to-language research.


## Empirical quality control

The control plane now includes a dependency-free empirical evaluator for labeled
NLP outputs. It measures accuracy, macro precision/recall/F1, abstention rate,
confidence calibration (ECE), and controlled perturbation consistency.

The quality gate is fail-closed:

**measure → compare with thresholds → publish report → PASS/FAIL**

A deterministic fixture is executed by GitHub Actions every 15 minutes and on
relevant changes. The resulting JSON report is uploaded as an artifact. This
fixture validates the machinery; it is not a substitute for a representative,
independently collected research benchmark.

For future real datasets, Automission should compare model versions using
held-out evaluation data, subgroup/condition slices, out-of-distribution
checks, calibration, robustness and reproducibility before proposing
promotion. A failed gate produces telemetry for improvement rather than
silently lowering the threshold.
