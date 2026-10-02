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


## Heart-View source governance

The Heart-View / Yatharth-Yug vocabulary is retained as user-authored source
material. The governance layer records whether a statement is a source
statement, observation, hypothesis, evidence-supported claim or independently
verified claim.

It also preserves counter-evidence. A generator cannot act as its own
independent verifier, and a source statement is never promoted to scientific
fact merely because it is repeated by an AI agent.

The source profile is stored in
`automation/heart-view-source-profile.json`, while the fail-closed claim
guard is implemented in `agents/claim_guard.py`.
