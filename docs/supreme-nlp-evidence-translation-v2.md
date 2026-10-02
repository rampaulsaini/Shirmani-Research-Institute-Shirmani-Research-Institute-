# SHIRMANI Supreme NLP Evidence Translation Gate v2

This layer upgrades the signal-to-language path without treating interpretation as proof of subjective experience.

## Objective

Translate instrumented signals from text, audio, images/video-derived measurements, environmental systems, plants, biological systems and non-living systems into simple language while preserving:

Signal -> Quality -> Features -> Context -> Model output -> Calibration -> Explanation -> Evidence -> Uncertainty -> Verification.

## Core guarantees

1. **No signal-to-feeling shortcut:** a detected pattern is not automatically labeled as feeling, consciousness, intention or inner experience.
2. **Abstention first:** insufficient, conflicting, out-of-distribution or low-quality evidence produces an explicit UNKNOWN/ABSTAIN result.
3. **Calibrated confidence:** confidence is treated as a model property that must be evaluated; it is never treated as proof.
4. **Provenance:** every interpretation can be traced to source data, preprocessing, model/version, evaluation record and timestamp.
5. **Alternative hypotheses:** materially plausible interpretations are retained instead of collapsing uncertainty into one narrative.
6. **Independent verification:** VERIFIED is a separate state and cannot be produced merely because an automated workflow passed.
7. **Regression protection:** a proposed model or prompt change must not degrade protected benchmark slices beyond configured tolerances.
8. **Human gate:** high-impact external actions remain subject to human authorization.

## Output contract

A translation record contains:

- measured signal summary;
- data-quality result;
- detected features/patterns;
- context window;
- model and version;
- inference;
- plain-language translation;
- confidence/calibration status;
- evidence references;
- alternative interpretations;
- uncertainty;
- verification state;
- audit trail.

## Living-system and non-living-system boundary

The same evidence contract applies to all domains. A plant electrical/acoustic/chemical/thermal measurement, an animal physiological signal, a machine vibration signal, or an environmental measurement can be translated into plain language when a validated mapping exists. The system must explicitly state when the available evidence supports only a physical/behavioral pattern and does not establish subjective experience.

## Performance target

The architecture targets high accuracy, low latency and high reliability, but numerical superiority is earned only through reproducible benchmark results. Track task-specific metrics, calibration error, abstention quality, out-of-distribution detection, latency, regression deltas and error categories.

## Five-minute Automission

Observe -> Validate -> Normalize -> Evaluate -> Translate -> Calibrate -> Compare alternatives -> Gate -> Audit -> Publish telemetry -> Propose improvement.

Production self-modification remains disabled; improvement proposals require authorization and regression evidence.
