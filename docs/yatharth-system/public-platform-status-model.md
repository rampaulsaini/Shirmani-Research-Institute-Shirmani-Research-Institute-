# Public Platform Capability Status Model

Every public capability must expose a machine-readable status and an auditable implementation contract.

## Statuses
- PLANNED: specified but not implemented.
- BUILT: code/content exists.
- TESTED: automated tests pass.
- DEPLOYED: deployed to the target environment.
- LIVE: publicly usable and monitored.
- AUTONOMOUS_WITH_GUARDRAILS: routine operation is automated with monitoring, escalation and appeal controls.

## Required fields
- capability_id
- public_name
- owner/module
- current_status
- implementation_reference
- test_reference
- dependencies
- security/privacy requirements
- human-escalation rule
- last_audit
- evidence_notes

## Public truthfulness rule
Do not label a feature LIVE merely because a GitHub workflow, documentation page or prototype exists.

## Priority domains
Social accounts, publishing, marketplace, freelancing, education, AI music, research, verification, support, environment, justice/fairness, economy and public dashboard.

## Completion rule
A domain is complete only when its user-facing flow, backend/data model, security controls, tests, deployment and monitoring contract are all satisfied.
