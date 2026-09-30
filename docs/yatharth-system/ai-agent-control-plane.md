# AI Agent Control Plane

## Agent families
Understanding: Language/NLP, Semantic Search, Entity/Concept, Translation.
Research: Claim, Evidence, Counter-Evidence, Comparison, Research Packet, Verification Gate.
Public Platform: Feed/Discovery, Creator Assistant, Education, Marketplace Matching, Customer Support, Accessibility.
Safety/Trust: Spam, Abuse Detection, Fraud/Risk, Provenance, Policy Compliance, Privacy Guard.
Operations: Automission Supervisor, Workflow Router, Federation, Observability, Failure Recovery, Continuous Audit.

## Control contract
Each agent action should record actor, input, intended action, permissions, evidence/context, uncertainty where meaningful, reversibility, audit event, and escalation rule.

Irreversible/high-impact actions require an explicit human-review gate unless a separately approved lawful policy permits otherwise.

## ML lifecycle
Permitted data -> provenance -> evaluation -> quality/bias/safety testing -> monitored deployment -> drift detection -> re-evaluation -> rollback when required.

This document does not claim every listed agent/model is currently deployed.