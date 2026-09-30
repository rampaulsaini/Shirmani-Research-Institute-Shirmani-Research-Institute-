# Yatharth AI Agent Control Plane

## Objective

Coordinate AI, ML, NLP and Automission agents across the public platform without granting any agent unrestricted authority.

## Agent classes

### A — Understanding
NLP extraction, language detection, semantic classification, entity linking, summarization and translation.

### B — Discovery
Search, recommendation, matching, retrieval and research-source discovery.

### C — Creation
Writing assistance, media assistance, music workflow support, education-content assistance and creator tooling.

### D — Operations
Marketplace routing, customer support, scheduling, notifications, workflow orchestration and quality checks.

### E — Trust
Spam/abuse detection, fraud signals, provenance checks, policy checks, anomaly detection and verification routing.

### F — Audit
Continuous audit, failure intelligence, resilience monitoring, traceability and reproducibility checks.

### G — Federation
Cross-repository Automission dispatch, receipts, health checks and bounded inter-system coordination.

## Permission model

Each agent must have:
- stable agent ID;
- declared capability;
- minimum required permissions;
- input/output schema;
- model/version metadata;
- rate limits;
- escalation rules;
- rollback path;
- audit events.

## Control hierarchy

User intent
→ policy engine
→ task router
→ specialized agent
→ validation
→ action
→ audit
→ feedback.

High-impact actions additionally require human review or explicit jurisdiction-specific authorization.

## Fail-closed conditions

Stop or escalate when:
- identity/permission is ambiguous;
- required evidence is missing;
- confidence is insufficient;
- a safety policy is triggered;
- a financial/legal/high-impact action exceeds authorization;
- agents disagree materially;
- audit logging fails;
- downstream service health is unknown.

## ML/NLP lifecycle

Collect permitted data → clean/minimize → label → train/evaluate → bias/error analysis → version → deploy → monitor drift → audit → rollback/retrain.

No model should be treated as permanently correct.

## Automission lifecycle

Discover → Plan → Execute → Verify → Record → Repair → Report.

A successful workflow run proves execution of that workflow, not truth of a philosophical, scientific, legal or social claim.

## Public transparency

The public dashboard should show service availability, system health, major incidents, verification state and meaningful aggregate metrics without exposing private user data or secrets.
