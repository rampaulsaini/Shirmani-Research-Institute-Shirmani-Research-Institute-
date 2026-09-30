# AI Agent / ML / NLP / Automission Operating Contract

## Purpose

Provide one bounded operating contract for the platform's future AI-native services.

## Agent layers

### L1 — Intake
Collect requests, content, reports, research inputs and platform events.

### L2 — NLP understanding
Language detection, transcription where available, normalization, entity/concept extraction, classification and semantic indexing.

### L3 — Evidence
Retrieve candidate sources, preserve provenance, identify supporting and counter-evidence, and mark uncertainty.

### L4 — ML / reasoning support
Ranking, clustering, anomaly detection, matching, trend analysis and scenario analysis. Models must expose limitations where practical.

### L5 — Safety / integrity
Detect spam, fraud patterns, abuse, privacy risks, malicious inputs and policy conflicts; route uncertain cases for review.

### L6 — Action routing
Create bounded tasks for publishing, support, marketplace operations, research packets, notifications or workflow automation.

### L7 — Automission supervisor
Schedule, retry, monitor, reconcile, record outcomes and stop unsafe or repeatedly failing tasks.

### L8 — Federation
Coordinate repositories/services using least privilege, explicit contracts and auditable receipts.

### L9 — Public presentation
Expose capability status, limitations, evidence state, user controls, appeals and meaningful uncertainty.

## Core loop

`Observe → Understand → Separate → Verify inputs → Act within scope → Record → Audit → Learn → Improve`

## Non-negotiable controls

- Least privilege and scoped credentials.
- No secrets in source, prompts, issues or logs.
- Idempotent and reversible automation where feasible.
- Rate limits and resource budgets.
- Audit trail for consequential actions.
- Human review for high-impact legal, financial, civic, rights, safety and moderation decisions.
- User appeal and correction paths.
- Independent verification remains separate from AI output.
- Fail closed when required evidence or dependencies are missing.

## Production readiness

A capability can move toward LIVE only after implementation, tests, security/privacy review, monitoring, rollback/disable controls, user-facing status and operational ownership are documented.

## ML/NLP truth boundary

Model confidence is not truth. Semantic similarity is not evidence. A generated summary is not a primary source. A successful workflow is not independent verification.
