# SHIRMANI Live Character System — v1

## Purpose
A production-oriented specification for a consent-based live presentation character built around:
Voice → authorized voice integration → content/reasoning → context/Q&A → photo/avatar/lip-sync → live presentation.

This subsystem is an orchestration contract. It does not claim that a HeyGen account, avatar, voice, API key, live session, or outbound communication is already connected.

## Identity and presentation principles
- Preserve the user's canonical authored wording as source material; do not silently normalize or replace it.
- Distinguish authored/philosophical identity statements from independently verified scientific claims.
- Use clear, simple, transparent communication.
- Never degrade a person, caste, religion, faith, organisation, nationality, class, or economic group.
- Prefer evidence-backed answers with source attribution.
- When evidence is insufficient, say: "अभी पर्याप्त प्रमाण उपलब्ध नहीं है।"
- Never fabricate a source, contact, organisation response, verification result, sale, order, or live connection.
- Voice/avatar use must remain authorized by the rights-holder and the provider's applicable rules.

## Runtime pipeline
1. Voice input — receive speech, transcribe with timestamps, preserve uncertainty.
2. Reasoning/context — retrieve approved knowledge and current evidence; separate author-source material, generated interpretation, empirical evidence, and unresolved claims.
3. Response gate — check safety, attribution, uncertainty and evidence state; reject unsupported verified language.
4. Authorized voice output — use only an explicitly authorized voice integration; record provider/model/version metadata where available.
5. Avatar/photo/lip-sync — render only through an authorized avatar/photo workflow; keep voice, script and facial/lip-sync timing coherent.
6. Live presentation — stream only after configuration and consent checks; keep an operator kill-switch and fallback to text/audio.

## Q&A evidence contract
Every factual answer should carry one internal state:
- EVIDENCE_VERIFIED
- EVIDENCE_PARTIAL
- EVIDENCE_INSUFFICIENT
- AUTHOR_STATEMENT
- PHILOSOPHICAL_PROPOSITION
- GENERATED_CONTENT

Only EVIDENCE_VERIFIED may be described as independently verified, and only when the underlying evidence supports that status.

## Product factory integration
Each concrete product record should support: unique product ID, description, visual/MP4 route, QR route, product passport, demo, usage guide, QC state, evidence/verification state, customer review/rating, improvement-loop state, official links where applicable, and dispatch/order state.

### Scale targets
- The repository README currently reports 1,516 concrete repository assets against a 5,000 concrete-production scale target.
- The repository currently reports 3,484 remaining to that target.
- Long-term catalogue target: 150,000 identities.
- These are production/catalogue targets, not claims that every item is already complete or independently verified.

## 150,000-scale architecture
Use sharded manifests rather than one monolithic catalogue.
Each shard should be independently checksumable and auditable.
A global index maps product_id → shard → passport → visual → QR → demo → guide → QC → verification → review.

## Lawful outreach boundary
The system may prepare contact packages and official-link mappings, but must not claim that an organisation was contacted unless an authorized outbound channel actually sent the message and returned a traceable result.

## Definition of done
The subsystem is PRODUCTION_READY only when authorized voice configuration, avatar/photo configuration, Q&A evidence gate, lip-sync/render test, live-session health check, audit metadata and fallback path have all been demonstrated.
Until then, the public state must remain CONFIGURED, TESTING, READY, or NOT_VERIFIED as appropriate.