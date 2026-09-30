# Yatharth Public Platform — Core Data Model

The public platform should use a modular data model so social, research, education, marketplace and AI services can interoperate without collapsing their trust boundaries.

## Core entities

UserAccount, Profile, Creator, Organization, Post, MediaAsset, Comment, Reaction, Follow, Community, Product, Service, Course, Lesson, Order, PaymentRecord, Review, Dispute, EvidenceRecord, Claim, ResearchPacket, VerificationDecision, AgentTask, AgentRun, AuditEvent, SafetyEvent, RecommendationEvent.

## Required provenance

Trust-sensitive content and decisions retain creator/source identifier, timestamp, version, transformation history where applicable, AI/agent involvement, moderation outcome, evidence references, reviewer identity for human decisions, and audit-event identifiers.

## Trust boundaries

### User content
User content is controlled according to published terms and applicable law. AI may assist with processing but should not silently rewrite the source.

### Research claims
A claim record distinguishes author-source material from normalized claims, evidence, comparative analysis and independent verification.

### Marketplace
Products/services track seller identity, listing, transaction, delivery, refund/dispute and review state.

### AI agents
Every consequential agent action should have an AgentRun and AuditEvent. Agent permissions should be scoped to the smallest required capability.

## Public status model

DESIGNED | IMPLEMENTED | TESTED | DEPLOYED | LIVE | AUTONOMOUS | HUMAN_REVIEW_REQUIRED

The UI must never convert a workflow green check into a claim that a public capability is live.

## Account safety

Authentication, session security, privacy controls, consent/preferences, blocking/reporting, data export/deletion mechanisms, appeals, rate limits and abuse detection are required.

## AI/ML/NLP observability

For every production model/agent family record model/agent version, input/output class, confidence or uncertainty where meaningful, policy decision, escalation reason, latency, failure/retry state, human override and evaluation version.
