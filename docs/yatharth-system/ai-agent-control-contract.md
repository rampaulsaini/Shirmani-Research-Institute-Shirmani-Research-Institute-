# AI Agent Control Contract

## Contract

Every autonomous agent must declare: agent_id, purpose, allowed inputs, prohibited inputs, tools/actions, output schema, evidence requirements, confidence/uncertainty handling, escalation conditions, audit record, and rollback/recovery behavior.

## Agent state

Allowed lifecycle:

PROPOSED → TESTING → BETA → ACTIVE → DEGRADED → PAUSED → RETIRED

An agent cannot mark itself VERIFIED.

## Evidence classes

- AUTHOR_SOURCE
- PRIMARY_EXTERNAL_SOURCE
- SECONDARY_SOURCE
- MODEL_INFERENCE
- USER_REPORT
- HUMAN_REVIEW

The interface must preserve the distinction between these classes.

## High-impact action gate

The following require a human-review or legally compliant external control path before irreversible execution: permanent account actions, major financial actions, serious dispute outcomes, governance/policy changes, independent verification decisions, and safety-critical interventions.

## Privacy

Agents must use data minimization, purpose limitation and access controls. Secrets, credentials and private user information must never be written into public repositories, issues or logs.

## Anti-self-confirmation rule

An agent cannot use its own generated output as independent evidence of that output's truth.

## Recommendation transparency

Where practical, recommendations should expose meaningful reasons, controls and correction/appeal paths.

## Monitoring

Automission should continuously inspect failures, repeated retries, anomalous outputs, unavailable dependencies, stale data, policy violations, security signals, user complaints, and rollback events.

## Recovery

A failed agent should: record the failure; preserve relevant diagnostics without leaking secrets; retry only within bounded policy; degrade safely; escalate when thresholds are reached; and resume only after the recovery condition is satisfied.
