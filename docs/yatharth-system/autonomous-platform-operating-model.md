# Autonomous AI/ML/NLP Automission Operating Model

## Objective
Define how a large public platform can be progressively automated without confusing an automation workflow with a fully autonomous production service.

## Agent layers

### L1 — Intake Agent
Receives posts, profiles, products, services, questions, reports and research submissions.

### L2 — NLP Understanding Agent
Extracts language, topics, entities, claims, intent, language and relationships.

### L3 — Classification & Routing Agent
Routes content to social, research, education, marketplace, support, safety or verification pipelines.

### L4 — Evidence & Trust Agent
Finds evidence, tracks provenance, detects unsupported assertions and preserves counter-evidence.

### L5 — Personalization Agent
Provides user-controlled discovery and recommendations. It must avoid manipulative engagement optimization and provide controls.

### L6 — Marketplace Agent
Matches customers, creators, freelancers, educators and service providers.

### L7 — Education Agent
Builds learning paths, explanations, practice and feedback while exposing source material and limitations.

### L8 — Creative Agent
Supports music, audio, video, writing and other creator workflows with clear ownership/licensing metadata.

### L9 — Safety Agent
Detects spam, fraud, abuse, dangerous content and policy violations; escalates uncertain or high-impact cases.

### L10 — Support Agent
Handles routine customer support and routes unresolved cases to human review.

### L11 — Audit Agent
Continuously checks traceability, reliability, permissions, failures and policy compliance.

### L12 — Automission Supervisor
Coordinates agents, retries recoverable failures, records decisions and stops safely when required conditions are not met.

## Human-control gates
Human review remains available for:
- account appeals
- significant financial disputes
- legal/justice decisions
- safety-critical actions
- independent verification
- irreversible or high-impact decisions

## Fail-closed principle
When evidence, permissions, identity, payment state or policy status is uncertain, the system must pause the affected action rather than silently invent a result.

## Production status vocabulary
Use only:
**PLANNED → SPECIFIED → BUILT → TESTED → STAGED → LIVE → MONITORED**

Never mark a feature LIVE solely because a GitHub workflow succeeded.

