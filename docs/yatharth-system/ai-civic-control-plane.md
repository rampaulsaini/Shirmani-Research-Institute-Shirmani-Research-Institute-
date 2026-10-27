
# AI Civic Control Plane

## Purpose
Define the AI/ML/NLP/Automission architecture for operating the public Yatharth platform while preserving human agency, due process, safety, privacy, and independent review.

## Layered architecture
### L0 - Human and legal authority
Human users, lawful institutions, independent reviewers, courts and regulators remain outside the model and cannot be silently replaced by an AI workflow.

### L1 - Observation
Collect only necessary, consented and lawfully available signals.

### L2 - NLP understanding
Extract language, entities, claims, intent, topics, language, context and uncertainty without treating model interpretation as fact.

### L3 - ML intelligence
Recommendation, matching, anomaly detection, forecasting and classification are probabilistic services with monitoring and calibration.

### L4 - Agent orchestration
Specialized agents coordinate research, education, commerce, support, content operations and ecological information.

### L5 - Automission supervisor
Schedules jobs, checks dependencies, retries bounded failures, records provenance and stops unsafe or ambiguous actions.

### L6 - Policy and safety gate
Blocks prohibited actions, detects fraud/abuse, enforces privacy controls and routes high-impact decisions to human review.

### L7 - Independent review gate
High-impact claims and decisions require evidence, reproducibility where applicable, human review and an auditable status transition.

### L8 - Public transparency
Expose understandable status, reasons, policies, metrics, change history, appeals and system-health summaries.

## Agent families
- Social Content Agent
- Search and Discovery Agent
- Translation Agent
- Education Agent
- Research Agent
- Evidence Agent
- Marketplace Agent
- Freelancing Agent
- Creator Agent
- Music Agent
- Customer Support Agent
- Trust and Safety Agent
- Fraud Detection Agent
- Accessibility Agent
- Ecological Data Agent
- Audit Agent
- Verification Coordinator
- Federation Agent

## High-impact action policy
AI must not autonomously make irreversible or legally consequential decisions involving account termination without appeal, large financial transfers, legal judgments, denial of essential services, independent scientific verification, political/electoral decisions, or medical diagnosis/treatment decisions.

Such actions require appropriate human and legal oversight.

## Fairness and neutrality
For public services and moderation:
- define measurable criteria
- test error disparities where appropriate
- document thresholds
- maintain appeal
- log model, version and policy provenance
- periodically re-evaluate performance

The system must not use private data to infer political preference or manipulate political choices.

## Fail-closed rule
If evidence, authorization, model confidence, policy applicability or auditability is insufficient for a consequential action:

STOP -> RECORD -> EXPLAIN -> ESCALATE

## Automation health
Track separately:
- workflow success
- agent task completion
- model quality
- safety incidents
- human-review latency
- verification status
- service availability

These metrics must never be collapsed into a single truth or civilization-success percentage.
