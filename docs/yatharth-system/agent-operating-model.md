# Yatharth Agent Operating Model

## Agent levels
- L0 deterministic validators and contracts
- L1 intake and routing
- L2 NLP and semantic understanding
- L3 research and evidence
- L4 marketplace, education and service agents
- L5 safety, audit and resilience
- L6 federation and orchestration
- L7 human-review escalation and appeals

## Required properties
Every agent declares purpose, allowed inputs, outputs, tools/data sources, uncertainty, policy constraints, escalation conditions, audit schema, and rollback/recovery path.

## Sensitive operations
Agents must not independently make irreversible high-impact decisions merely because a model confidence score is high. Such cases route through defined controls and appeal mechanisms.

## Continuous learning
Model updates are versioned, evaluated against regression suites, monitored after deployment, and reversible. User feedback is evidence about experience, not automatic proof of truth.

## Automission
Automission means continuous execution of bounded, observable tasks with fail-closed gates, not unrestricted autonomous authority.
