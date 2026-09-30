# AI / ML / NLP / Automission Operating Model

## Architecture

Event layer → NLP layer → ML layer → specialized agents → policy/safety layer → Automission → audit → human escalation.

## Agent boundaries

Every agent must have explicit scope, least-privilege tools, auditable inputs/outputs, rate limits, failure handling, escalation rules and no secret leakage. Agents must not mark substantive claims independently VERIFIED without the defined evidence contract.

## Continuous operation

Automission should ingest events, classify work, route tasks, execute bounded jobs, validate outputs, retry recoverable failures, record provenance, detect anomalies, escalate unresolved cases and publish safe status metrics.

## Verification boundary

Automation can establish engineering facts such as workflow completion, tests passing, artifact generation and schema validation. It cannot substitute for independent human or scientific verification of substantive claims.

## Safety and satisfaction

Optimization should include quality, accessibility, privacy, security, user satisfaction, successful task completion, dispute resolution, low abuse/fraud and environmental/resource awareness. Raw session duration must not be the sole optimization target.
