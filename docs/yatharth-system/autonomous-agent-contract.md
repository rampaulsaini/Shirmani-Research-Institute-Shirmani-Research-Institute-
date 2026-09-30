# Autonomous Agent Contract

## Agent classes
- Intake Agent
- Identity/Account Agent
- Content Agent
- NLP Understanding Agent
- Safety Agent
- Research Agent
- Evidence Agent
- Education Agent
- Creator/Music Agent
- Marketplace Agent
- Employment/Freelancing Agent
- Customer Support Agent
- Justice/Complaint Routing Agent
- Audit Agent
- Automission Supervisor
- Recovery Agent

## Required properties
Every agent action must have:
- task ID
- actor/agent identity
- input provenance
- policy/version reference
- action/result
- confidence or uncertainty where applicable
- timestamp
- audit record
- escalation path

## Fail-closed
Agents must stop and escalate when authority, evidence, identity, safety, payment, or policy conditions are insufficient.

## No hidden authority
Agents cannot silently invent verification, legal authority, ownership, currency value, scientific certainty or public governance status.
