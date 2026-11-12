# SHIRMANI Supreme NLP Evidence Translation Gate v2

This layer upgrades signal-to-language translation while preserving the distinction between measurable signal, model inference and subjective-experience claims.

## Objective

Translate instrumented signals from text, audio, images/video-derived measurements, environmental systems, plants, biological systems and non-living systems into simple language while preserving:

**Signal -> Quality -> Features -> Context -> Model -> Calibration -> OOD check -> Explanation -> Evidence -> Alternatives -> Uncertainty -> Verification.**

## Core guarantees

1. **No signal-to-feeling shortcut:** a detected pattern is not automatically labeled as feeling, consciousness, intention or inner experience.
2. **Abstention first:** insufficient, conflicting, low-quality or out-of-distribution evidence produces explicit UNKNOWN/ABSTAIN behavior.
3. **Calibrated confidence:** confidence must be measured and evaluated; it is never proof.
4. **Provenance:** every interpretation traces to source data, preprocessing, model/version, evaluation record and timestamp.
5. **Alternative hypotheses:** materially plausible interpretations remain visible instead of being collapsed into one narrative.
6. **Independent verification:** VERIFIED is a separate evidence state and cannot be produced merely because an automated workflow passed.
7. **Regression protection:** model/prompt changes must be compared against protected benchmark slices.
8. **Human gate:** high-impact external actions remain subject to human authorization.

## Output contract

A translation record contains:

- measured signal summary;
- data-quality result;
- detected features/patterns;
- context;
- model and version;
- inference;
- plain-language translation;
- confidence and calibration status;
- OOD status/method;
- evidence references;
- alternative interpretations;
- uncertainty;
- verification state;
- independent-verification metadata when VERIFIED;
- audit trail.

## Living-system and non-living-system boundary

Plant electrical/acoustic/chemical/thermal measurements, animal physiological signals, machine vibration and environmental measurements can be translated into plain language when a validated mapping exists. The system must explicitly distinguish a measured physical/behavioral pattern from a claim about subjective experience.

## Performance

The architecture targets high accuracy, low latency and high reliability, but numerical superiority is earned only through reproducible benchmark results. Track task metrics, calibration error, abstention quality, OOD detection, latency, protected-baseline regression and error categories.

## Five-minute Automission

Observe -> Validate -> Normalize -> Evaluate -> Translate -> Calibrate -> Detect OOD -> Compare alternatives -> Gate -> Audit -> Publish telemetry -> Propose improvement.

Production self-modification remains disabled; improvement proposals require authorization, regression evidence and independent verification.
