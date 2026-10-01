# SHIRMANI Supreme AI-ML-NLP Architecture Contract

## Purpose

Define an evidence-first architecture for continuous AI-agent, machine-learning, NLP and Automission improvement.

## Core pipeline

Observe → Normalize → Extract signals → Model → Reason → Translate → Verify → Audit → Learn → Repeat

## Multimodal perception

The platform may consume:

- text and speech
- images and video
- acoustic and vibration signals
- environmental and IoT measurements
- electrical/bioelectrical measurements
- temporal and contextual observations

A signal is not automatically treated as a subjective feeling. The system must distinguish:

1. observed measurement
2. model interpretation
3. inferred state
4. uncertainty/confidence
5. independently verified fact

## NLP translation contract

Every interpretation should preserve provenance:

`source → features → model → interpretation → confidence → evidence`

Human-readable output should use plain language and explicitly mark uncertainty when evidence is incomplete.

Example:

> The observed signal matches patterns associated with X in the available model/data. Confidence: Y%. This is an inference from measured signals, not direct proof of subjective experience.

## Agent layers

- Perception Agent
- NLP/Semantic Agent
- ML/Pattern Agent
- Research Agent
- Evidence Agent
- Verification Agent
- Security Agent
- Automission Supervisor
- Supreme Quality Controller

Agents may propose improvements, but consequential production changes remain subject to deterministic tests, security checks and explicit verification gates.

## Accuracy and reliability

The platform must never equate:

- workflow success with truth
- AI output with independent verification
- confidence with certainty
- repeated output with proof

Quality should be measured using reproducible tests, error rates, calibration, provenance completeness, regression checks and independent verification status.

## Automission loop

Scheduled Automission may continuously:

1. inspect current state
2. identify bounded improvement opportunities
3. run deterministic tests
4. generate evidence
5. compare against the previous baseline
6. publish machine-readable receipts
7. continue only when gates pass

Failures remain observable and diagnosable. Historical run records are not rewritten as a substitute for fixing the source of failure.

## Public identity layer

The public platform should present the creator's work through evidence, provenance, research outputs, publications, software, creative works and documented milestones. It should not claim legal nationality, citizenship or institutional recognition unless such status is actually granted by the relevant authority.

## Integrity principle

The strongest platform is one that can say:

**What was observed, what was inferred, what was verified, what remains unknown, and how the result can be reproduced.**


## Signal-to-NLP evidence contract

For any acoustic, vibration, electrical, bioelectrical, environmental, image, video,
or other measurable input, the platform uses:

**Measure → Normalize → Feature extraction → Model → Interpretation → Plain language → Verification**

The new `factory/signal_to_nlp.py` layer deliberately separates:

- measured features from interpretation
- signal-quality confidence from truth probability
- inferred state from subjective experience
- author/model claims from independently verified evidence

No sensor stream is converted into a claim of consciousness, emotion, pain, intention,
or subjective experience without a validated model and supporting evidence.

## Failure handling

A failed run is an engineering signal, not something to hide. The Automission Supervisor
is read-only with respect to historical runs: it observes failures, preserves evidence,
and runs local integrity gates. It does not automatically rewrite history or blindly
rerun arbitrary failed workflows.

The standalone failure-intelligence workflow has been removed from the canonical branch;
failure observation is now integrated into the controlled supervisor/quality architecture.
