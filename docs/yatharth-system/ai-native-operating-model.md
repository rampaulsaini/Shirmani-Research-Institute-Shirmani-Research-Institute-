# AI-Native Operating Model

## Objective
Define how AI agents, ML, NLP and Automission can operate the platform while preserving safety, transparency, human agency and fail-closed controls.

## Agent layers
### L1 Intake
Ingest posts, profiles, listings, requests, research records and system events.

### L2 NLP understanding
Language identification, transcription, extraction, entity/concept recognition, semantic indexing and translation.

### L3 Classification
Route content to social, education, commerce, research, creative, environmental or support workflows.

### L4 Safety and trust
Detect spam, fraud signals, impersonation, abuse, unsafe content and policy conflicts. Produce explainable signals, not automatic certainty.

### L5 Personalization
Search, recommendations and matching using declared preferences and behavioral signals with privacy controls.

### L6 Task agents
Education tutor, research assistant, creator assistant, marketplace assistant, customer-support agent and workflow agents.

### L7 Commerce
Catalog enrichment, search, order-state automation, seller/buyer communication, delivery-state checks and anomaly detection.

### L8 Governance
Policy checks, audit trails, permission enforcement, appeals routing and high-impact decision escalation.

### L9 Automission supervisor
Schedules work, monitors dependencies, retries bounded failures, records receipts and escalates unresolved failures.

### L10 Continuous audit
Tests contracts, provenance, security controls, model/version changes and automation health.

## ML/NLP responsibilities
- semantic retrieval and clustering;
- recommendation and matching;
- language translation;
- classification and anomaly detection;
- speech/text processing;
- quality and relevance estimation;
- model evaluation and drift monitoring.

## Fail-closed rules
Automation must not:
- convert an author's testimony into independent verification;
- declare scientific or historical truth without an evidence contract;
- make irreversible high-impact decisions without required review/appeal;
- silently alter financial balances or regulated records;
- expose private user data;
- fabricate evidence, reviews, transactions or users.

## Human oversight
Human review remains available for high-impact moderation, financial disputes, legal/compliance issues, account appeals, safety incidents and independent verification.

## Operational state vocabulary
PLANNED -> BUILT -> TESTED -> DEPLOYED -> LIVE -> AUTONOMOUS_WITH_GUARDRAILS.

A workflow run alone is not evidence that a product capability is live.
