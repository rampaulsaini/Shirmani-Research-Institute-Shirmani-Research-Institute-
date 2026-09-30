# AI Impartiality Control Plane

## Core rule

AI is a decision-support and monitoring layer, not an unelected sovereign.

## Agent classes

- Observe: collect permitted data.
- Understand: NLP/ML extraction and classification.
- Compare: evidence and alternative interpretations.
- Test: policy, safety, bias, security, and consistency tests.
- Escalate: route consequential cases to authorized humans.
- Audit: preserve provenance and detect anomalies.
- Explain: publish understandable reasons and limitations.

## Permission model

Every agent has:
- unique identity;
- explicit capability list;
- read/write scope;
- data classification;
- expiration/rotation policy;
- audit log;
- human owner;
- independent oversight path.

Agents must not create hidden privileges, alter their own access, delete audit evidence, suppress appeals, impersonate human authorities, or declare themselves final verifiers.

## Multi-agent independence

For high-impact decisions, use independent components where feasible:
- policy/rule engine;
- evidence retriever;
- adversarial checker;
- fairness checker;
- audit logger;
- human review.

Agreement between multiple AI agents is not equivalent to independent human verification when agents share the same model, data, or operator.

## Change control

Material changes require:
1. versioned proposal;
2. automated tests;
3. security review;
4. impact analysis;
5. human authorization;
6. rollback plan;
7. public change record where appropriate.

## Incident states

OBSERVED -> TRIAGED -> HUMAN_REVIEW -> ACTIONED -> AUDITED -> CLOSED

No automated system should silently convert an observation into punishment or deprivation.

## Transparency

Every public AI-assisted decision surface should disclose:
- that AI was used;
- purpose;
- relevant data sources;
- model/version where appropriate;
- confidence/uncertainty;
- human review status;
- appeal/correction route.

## Research boundary

A model can discover evidence and contradictions, but the repository must preserve:
AI-generated -> QC-tested -> evidence-mapped -> human-reviewed -> independently verified.
