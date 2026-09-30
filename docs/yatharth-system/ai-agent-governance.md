# AI Agent Governance & Automission Contract

## Objective
Provide a common control contract for AI agents, ML systems, NLP pipelines, and Automission workflows across the Yatharth platform.

## Agent classes
- Observer — reads permitted signals.
- Classifier — categorizes content/events.
- Researcher — retrieves and structures evidence.
- Matcher — connects people, services, jobs, courses, or products.
- Creator Assistant — assists with content creation.
- Auditor — checks provenance, contracts, and anomalies.
- Orchestrator — coordinates bounded workflows.
- Escalation Agent — routes uncertain/high-impact cases to human review.

## Agent contract
Every production agent should declare identity/version, purpose, allowed inputs, prohibited inputs, permitted actions, confidence/uncertainty, source provenance, model/version, audit trail, escalation conditions, and rollback mechanism.

## Decision classes
Low-impact routine indexing, formatting, translation, metadata extraction, duplicate detection, and bounded workflow maintenance may be automated after testing.

Medium-impact recommendations, marketplace matching, content classification, and research triage should expose uncertainty and provide correction/reporting paths.

High-impact account termination, substantial financial actions, justice/dispute outcomes, sensitive eligibility decisions, and independent verification status changes require human oversight and explicit audit records.

## Automission loop
Observe -> Understand -> Validate -> Act within scope -> Record -> Audit -> Improve -> Escalate when uncertain.

The loop must never become an unrestricted self-authorizing action loop.

## ML/NLP requirements
Training/evaluation data should be versioned. Where practical measure precision/recall, false-positive and false-negative rates, calibration, language coverage, drift, subgroup performance where appropriate, and incident rates.

## Fail-closed rule
If provenance, authorization, safety, or required evidence is missing, the agent stops, records the reason, and escalates rather than inventing certainty.

## Continuous improvement
Automission may automatically open improvement work items, run tests, collect failure evidence, and prepare changes. Production deployment remains governed by repository protections, testing, and appropriate review gates.
