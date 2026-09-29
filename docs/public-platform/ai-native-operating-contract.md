# AI-Native Operating Contract

## Objective
Build toward an AI/ML/NLP/Automission-native platform in which routine operations are automated while high-impact decisions remain auditable and appealable.

## Agent layers
### L1 Intake Agent
Ingests permitted user actions and content.

### L2 NLP Understanding Agent
Language detection, transcription, extraction, classification, summarization and semantic representation.

### L3 Safety and Policy Agent
Detects spam, abuse, prohibited content, fraud signals and policy conflicts; escalates uncertain cases.

### L4 Discovery and Recommendation Agent
Search, semantic retrieval, personalized discovery and marketplace matching with user controls.

### L5 Creator and Education Agents
Assist with creation, translation, lesson generation, metadata, accessibility and publishing.

### L6 Commerce Agent
Catalog, order-state automation, seller/buyer support and transaction workflow coordination.

### L7 Research and Verification Agents
Claim extraction, evidence mapping, counter-evidence, comparison, reproducibility checks and verification-gate preparation.

### L8 Automission Supervisor
Coordinates agents, schedules tasks, retries safe failures, records provenance and prevents uncontrolled recursive actions.

### L9 Audit and Resilience Agents
Continuous health checks, anomaly detection, incident records, rollback/recovery and audit trails.

## Fail-closed requirements
- Never claim independent verification from automation success.
- Never hide uncertainty.
- Never execute irreversible high-impact actions solely from an unreviewed model output.
- Preserve provenance for consequential decisions.
- Provide user reporting and appeal paths.
- Protect credentials, payment information and private user data.

## Operational maturity states
PLANNED -> BUILT -> TESTED -> LIVE -> MONITORED -> AUDITED -> AUTONOMOUS_ROUTINE.

AUTONOMOUS_ROUTINE means routine operations can run automatically; it does not mean that every decision is made without human oversight.

## Current status
This contract is an architecture and implementation target. Existing GitHub Actions demonstrate active automation, but they do not establish that the complete public social, commerce, education, AI/ML/NLP and economic platform is already live.
