# Autonomous Operation Boundaries

## Goal

Define what AI agents, ML systems, NLP pipelines, and Automission may do autonomously and what requires authorization or human review.

## Autonomous by default

- content indexing and semantic classification
- translation
- search and retrieval
- recommendation generation
- routine workflow orchestration
- CI/QC checks
- duplicate and spam detection
- routine fraud-risk flagging
- research packet preparation
- evidence-map preparation
- system health monitoring
- non-destructive recovery
- status reporting

## Human authorization or review

- permanent account termination
- high-impact moderation decisions
- disputed financial outcomes
- access to essential services
- legal/justice determinations
- independent verification decisions
- changes to governance rules
- release of sensitive personal information
- irreversible external actions
- actions with substantial physical, financial, or civil consequences

## Agent controls

Every consequential agent action should have:

- authenticated identity
- least-privilege permissions
- policy check
- input provenance
- action log
- result/receipt
- rollback where technically possible
- escalation path

## Fail-closed principle

If authorization, evidence, identity, policy, or safety checks are unavailable, the agent should stop or move the task to review rather than inventing approval.

## Public transparency

The public interface should disclose meaningful automation boundaries so users know when they are interacting with AI, an automated workflow, or a human reviewer.
