# AI-Native Autonomous Service Model

## Objective

Define how AI agents, ML, NLP, automation, and Automission can operate the routine parts of the Yatharth public ecosystem while preserving human agency and fail-closed controls.

## Agent layers

### L1 — Intake Agent
Receives posts, products, jobs, courses, research records, complaints, and service requests.

### L2 — NLP Understanding Agent
Performs language detection, transcription where applicable, semantic extraction, classification, entity/concept linking, and multilingual normalization.

### L3 — Trust & Safety Agent
Detects spam, fraud indicators, abusive content, impersonation, manipulation, and policy risks. It produces signals and explanations rather than silently making irreversible high-impact decisions.

### L4 — Discovery & Matching Agent
Matches users with content, courses, jobs, freelancers, products, services, communities, and research resources using transparent preference controls.

### L5 — Creator & Commerce Agent
Assists with listings, descriptions, pricing information, catalog structure, fulfillment status, customer communication, and analytics.

### L6 — Education Agent
Builds personalized learning paths, explanations, practice material, translation, accessibility support, and progress summaries.

### L7 — Research Agent
Extracts claims, builds evidence maps, identifies counter-evidence, compares sources, and prepares review packets. It cannot independently convert an author's statement into a verified fact.

### L8 — Justice/Resolution Agent
Routes complaints, identifies applicable rules, proposes mediation steps, preserves evidence, and tracks deadlines. High-impact adjudication remains appealable and subject to human/legal governance.

### L9 — Ecological Stewardship Agent
Aggregates environmental information, identifies conservation opportunities, and supports transparent reporting. It must distinguish measured data from model estimates.

### L10 — Automission Supervisor
Coordinates jobs, retries recoverable failures, checks contracts, records provenance, and escalates unresolved exceptions.

### L11 — Federation Agent
Coordinates approved work across repositories/services using least-privilege credentials and explicit delivery receipts.

### L12 — Public Presentation Agent
Publishes approved status, documentation, dashboards, translations, and user-facing explanations.

## ML/NLP responsibilities

ML/NLP may support:
- classification
- retrieval
- recommendation
- clustering
- anomaly detection
- translation
- summarization
- speech/text processing
- semantic search
- fraud-risk signals
- quality signals

Model outputs are evidence/signals, not automatic proof of truth.

## Fail-closed requirements

The system must stop or escalate when:
- identity or authorization is uncertain
- evidence is insufficient for a verification decision
- a financial action exceeds its authorized threshold
- a legal/justice decision requires human authority
- a model confidence/quality threshold is not met
- safety rules conflict
- provenance is missing
- an external service is unavailable
- a user appeals a high-impact decision

## Human agency

Users must have:
- understandable notices
- access to their data where appropriate
- correction mechanisms
- appeal/review routes
- controls over recommendation personalization
- clear commercial terms
- clear distinction between AI-generated and human-authored material where relevant

## Autonomous does not mean uncontrolled

The target is high automation with bounded authority, observable decisions, recoverability, and independent auditing—not an unaccountable system.
