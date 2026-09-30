# Yatharth Control Plane

## Purpose

This document defines the single control-plane contract for the Yatharth public platform. It consolidates the rapidly expanding research, social, education, commerce, creative, justice, economy, AI/ML/NLP and Automission layers without treating architecture as deployed capability.

## Operating loop

Intake → understand → classify → protect → route → execute → verify → measure → learn → audit → recover.

## Public domains

- Social and profiles
- Research and knowledge
- Education and skills
- Yatharth AI and AI services
- Yatharth AI Music and creative studio
- Digital Store and creator commerce
- Freelancing, employment and services
- Yatharth economy and any proposed Yatharth currency model
- Yatharth justice, complaints, appeals and transparency
- Nature, Earth and humanity protection
- Community, media, podcast and live experiences
- Trust, evidence and independent verification

## Agent planes

1. Experience agents — discovery, accessibility, multilingual interaction and support.
2. Content agents — NLP extraction, classification, translation, moderation and metadata.
3. Commerce agents — catalog, matching, fulfillment signals, seller/buyer support and fraud monitoring.
4. Education agents — learning paths, assessment support and personalized assistance.
5. Research agents — claim extraction, evidence mapping, comparison and packet generation.
6. Safety agents — abuse, spam, fraud, privacy and security signals.
7. Verification agents — evidence contracts, provenance checks and verification queues.
8. Operations agents — workflow orchestration, health monitoring, recovery and federation.

## Decision boundaries

AI agents may automate routine, reversible operations. High-impact actions must remain subject to explicit policy, auditability, user appeal and appropriate human review. This includes account termination, material financial actions, legal/justice decisions, and independent scientific verification.

## Truth-state model

Every capability and claim must expose its state independently:

- PLANNED — specified but not implemented.
- BUILT — implementation exists.
- TESTED — automated tests pass for the defined scope.
- LIVE — deployed and reachable for the defined audience.
- AUTOMATED — routine operation is handled by the defined automation layer.
- VERIFIED — evidence requirements are satisfied by the appropriate independent process.

No state may be inferred from a workflow run alone.

## Reliability requirements

- Idempotent jobs where practical.
- Retry with bounded backoff.
- Dead-letter/failure queues for unrecoverable tasks.
- Trace IDs across agent handoffs.
- Immutable audit events for material actions.
- Least-privilege credentials.
- Secret values never stored in source, prompts, issues or logs.
- Safe rollback for deployable changes.
- Human escalation for unresolved high-impact cases.

## Continuous improvement

Every new user-provided source is preserved as source material first. Normalization, comparison, evidence mapping and verification remain separate stages. Platform telemetry may improve software operation but does not independently verify philosophical, scientific or metaphysical claims.

## Launch gate

A public feature is launch-ready only when its user contract, data model, security boundary, accessibility behavior, failure path, audit trail, support path and deployment test are defined. A feature must not be presented as live merely because its architecture or documentation exists.
