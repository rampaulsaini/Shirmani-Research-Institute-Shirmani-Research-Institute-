# AI Agent + ML + NLP + Automission Operating System

## Objective

Provide a bounded autonomous operating layer for the Yatharth platform.

## Agent layers

### L1 Intake Agent
Receives structured events from public products and internal research pipelines.

### L2 NLP Understanding Agent
Performs language detection, transcription where supported, entity/concept extraction, classification and semantic indexing.

### L3 Safety and Trust Agent
Screens spam, abuse, fraud indicators, unsafe content and policy violations. It must expose uncertainty and escalation paths.

### L4 Research Agent
Extracts claims, links sources, identifies counter-evidence and prepares research packets.

### L5 Recommendation and Discovery Agent
Matches people with content, services, learning, products and communities using relevance and safety signals.

### L6 Commerce Agent
Supports catalog quality, product metadata, order-state automation and customer support.

### L7 Education Agent
Supports learning paths, explanations, assessments and multilingual educational assistance.

### L8 Creator Agent
Assists creators with drafting, translation, metadata, publishing workflows and media organization.

### L9 Verification Gate
Maintains the distinction between generated output, evidence-mapped claims, human review and independent verification.

### L10 Automission Supervisor
Schedules bounded jobs, checks dependencies, retries recoverable failures, records receipts and stops unsafe or ambiguous operations.

### L11 Federation Agent
Coordinates approved repositories/services through authenticated, least-privilege interfaces.

### L12 Audit Agent
Continuously checks contracts, provenance, status transitions, security signals and operational health.

## ML layer

Potential ML functions include ranking, recommendation, anomaly detection, spam/fraud detection, semantic retrieval and quality prediction.

ML outputs are probabilistic. They must not be represented as human judgment or independent verification.

## NLP layer

The NLP pipeline should support:

Input -> language detection -> normalization -> segmentation -> entity/concept extraction -> claim extraction -> semantic indexing -> evidence linking -> task routing -> audit trail.

## Autonomous-operation contract

Every automated action should have:

- actor/agent identity;
- input reference;
- policy/rule reference;
- timestamp;
- action;
- result;
- confidence/uncertainty where applicable;
- rollback or appeal path where applicable;
- audit receipt.

## Fail-closed rules

Automation must stop or escalate when:

- required evidence is missing;
- authorization is ambiguous;
- a high-impact decision is detected;
- a security boundary is crossed;
- an irreversible action lacks confirmation;
- model confidence is insufficient for the permitted action.

## Human control

Automation can operate routine workflows, but high-impact decisions involving account termination, significant financial consequences, legal disputes, safety, or independent verification require appropriate human oversight and appeal.

## Reality-status rule

A workflow run proves that a workflow executed. It does not by itself prove that a product feature is deployed, that an AI model performed a claimed capability, or that a philosophical/scientific claim is independently verified.
