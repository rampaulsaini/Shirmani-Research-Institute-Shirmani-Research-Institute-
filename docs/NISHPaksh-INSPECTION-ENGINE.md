# Nishpaksh Inspection Engine — implementation blueprint

## Goal
Build a scalable, purpose-first inspection application inside the Shirmani Research Institute. The application supports self-reflection, education, employment/role assessment and authorized public-service assessment while keeping evidence, inference and human judgment separate.

## Purpose gate
No assessment starts until the participant selects exactly one purpose:
- self as human
- education
- employment/role
- public service
- ministerial role
- chief minister role
- prime minister role
- other authorized role

Changing purpose creates a new scope and consent record.

## Evidence model
`REGISTERED → EVIDENCE_PENDING → CHECK → HUMAN_REVIEW → VERIFIED / NOT_VERIFIED / DISPUTED → ARCHIVED`

A generated score, model output, workflow success or sensor reading is not independent verification.

## Multimodal analysis
### NLP
- claim extraction
- fact/inference separation
- ambiguity detection
- contradiction and consistency prompts
- source/provenance linking
- multilingual normalization
- question generation

### Voice
Accessibility and communication features may be supported. Emotion, honesty, intent or character must not be inferred as fact.

### Eye / face
Use only for narrowly defined, consented measurements or identity/security functions where lawful and technically validated. Gaze or facial movement is not a truth detector.

### Finger-vein
Treat as an optional identity/security factor, never as evidence of morality, honesty, intelligence or fitness.

### Cross-modal layer
Disagreement becomes an uncertainty flag and requests human review. It must not become an automated deception verdict.

## Role certificate
The system may issue:
1. completion certificate — proves that a defined process was completed;
2. evidence review record — records evidence state and provenance;
3. role assessment report — summarizes evidence and human review.

It must not issue a certificate claiming that a person is absolutely truthful, morally pure, universally fit, or intrinsically superior.

## AI/ML automation
Source → Normalize → Claims → Sources → Evidence → Formulation/Test → Verification → QC → Publication → Archive

Operational workflows should additionally implement:
- idempotency keys
- queue isolation by assessment
- retry with bounded backoff
- dead-letter queue
- replay/recovery
- audit event chain
- consent revocation
- data retention expiry
- export/delete controls
- model/version provenance
- human-review checkpoints
- appeal/dispute workflow

## Scale
The product should be designed for very large public adoption, but a claim such as “850 crore users” is a capacity target, not a guaranteed usage figure. Capacity should be established through load tests, queue saturation tests, database partitioning tests, privacy/security tests and disaster-recovery exercises.

## Public-authority use
A public official cannot be made subject to an assessment merely by software design. Any mandatory use would require a lawful authority, defined scope, due process, privacy safeguards, human review and an appeal mechanism. The app can provide the technical workflow without deciding who must legally use it.
