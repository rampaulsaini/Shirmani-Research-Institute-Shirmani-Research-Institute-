# Autonomous AI/ML/NLP Automission Control Plane

## Layers
L1 Intake — receive user/content/events.
L2 NLP — classify language, entities, concepts and claims.
L3 ML/Ranking — personalize discovery using documented objectives and safeguards.
L4 Agent orchestration — route tasks to specialized agents.
L5 Safety/Trust — detect abuse, fraud, privacy and policy risks.
L6 Marketplace/Education/Research agents — perform domain workflows.
L7 Verification gate — keep independent verification fail-closed.
L8 Federation — coordinate repositories and services.
L9 Observability — metrics, traces, failures and recovery.
L10 Public presentation — expose understandable status and outcomes.

## Required controls
- Least-privilege credentials
- No secrets in content, issues or logs
- Idempotent jobs
- Retry/backoff and dead-letter handling
- Human escalation for high-impact decisions
- Immutable audit events where appropriate
- Versioned model/agent policies
- Rollback and kill-switch capability
- Continuous contract and smoke testing

## Completion rule
A component is not "fully autonomous" merely because a GitHub workflow succeeds. It must have a deployed service, defined contract, tests, observability, failure handling and an appropriate decision boundary.
