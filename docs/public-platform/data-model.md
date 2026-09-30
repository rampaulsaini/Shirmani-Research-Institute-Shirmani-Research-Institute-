# Yatharth Global Platform — Public Data Model

This model defines the minimum interoperable objects for the next implementation layer. It is a contract, not a claim that a production backend already exists.

## Core objects

| Object | Purpose | Minimum fields |
|---|---|---|
| Account | identity and access state | id, handle, display_name, locale, status, created_at |
| Profile | public presentation | account_id, bio, avatar_ref, skills, interests, links |
| Content | posts, articles, audio, video, research material | id, owner_id, type, title, body_ref, visibility, provenance |
| Product | digital goods/store listing | id, seller_id, title, description, price, currency, asset_ref, status |
| Service | freelance/service offer | id, provider_id, title, skills, pricing_model, availability, status |
| Job | employment opportunity | id, publisher_id, title, skills, location_mode, compensation, status |
| Course | education offering | id, instructor_id, title, modules, language, price, status |
| Order | commerce intent | id, buyer_id, seller_id, item_type, item_id, amount, currency, status |
| WorkOrder | client-provider fulfilment | id, client_id, provider_id, service_id, milestones, status |
| LearningRecord | course/skill progress | id, learner_id, course_id, progress, assessment_refs |
| Report | safety/trust report | id, reporter_id, target_type, target_id, reason, status |
| Dispute | contested transaction/action | id, parties, subject_ref, evidence_refs, status, reviewer |
| AIJob | machine task | id, requester_id, agent_class, input_refs, output_refs, status, audit_ref |
| VerificationRecord | independent verification | id, claim_id, evidence_refs, reviewer, method, status, reviewed_at |

## State discipline

Every implementation should distinguish: PLANNED -> BUILT -> TESTED -> LIVE -> AUTONOMOUS.

A page, workflow, generated artifact, or automation run must not be marked LIVE merely because its code exists.

## Provenance

Content representing the author's framework should carry source identifier/version, author/source status, extraction method when AI/NLP was used, evidence links for factual claims, counter-evidence where applicable, and verification status.

## High-impact boundaries

Production implementation must provide appropriate authentication, authorization, payment controls, privacy controls, abuse prevention, audit logging, appeals, and human review for high-impact account, financial, safety, dispute, and independent-verification decisions.

## Backend boundary

GitHub Pages can host the public/static interface, but secure multi-user accounts, shared feeds, persistent marketplace transactions, payments, private data, and production AI services require a separately deployed backend and appropriate providers.