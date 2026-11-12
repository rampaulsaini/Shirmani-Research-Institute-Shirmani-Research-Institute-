# Shirmani Live Character System — v1

## Purpose
Live presentation subsystem: Voice → authorized voice → question/context understanding → evidence gate → bounded answer → facial/gaze presentation → accurate lip-sync → live response.

## Core principles
1. Simple • natural • clear • transparent.
2. Use only an explicitly authorized identity, voice, and visual presentation.
3. Keep philosophical / identity statements separate from source-backed facts and independently verified scientific evidence.
4. If evidence is insufficient, say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
5. Never demean a person, caste, religion, community, organization, or economic group.
6. Never promote UNVERIFIED to VERIFIED because a workflow, model, avatar, or automation succeeded.
7. Preserve provenance when evidence exists.
8. Fail safely when evidence, authorization, or synchronization is unavailable.

## Live pipeline
User speech → speech recognition → question/context understanding → evidence/provenance gate → bounded answer or abstention → authorized voice synthesis → presentation timing → face/gaze/expression/lip-sync → live presentation → interaction/provenance log.

## Presentation contract
- natural eye-contact and gaze changes;
- natural facial movement;
- speech-to-face timing coherence;
- accurate lip-sync;
- calm, respectful delivery;
- source detail when evidence exists;
- no certainty beyond evidence.

These are presentation-quality targets, not claims of consciousness, mind-reading, or scientific reproduction of a person's inner state.

## Claim boundary
Each answer carries a claim type: identity_statement, philosophical_statement, source_backed_fact, empirical_finding, independently_verified, or unverified.
Only the evidence layer may assert independently_verified.

## Evidence response contract
When evidence exists: answer → source/provenance → confidence/limitations.
When evidence is insufficient: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
Never invent citations, measurements, or certainty.

## Voice authorization
Allowed states: VOICE_AUTHORIZED, VOICE_UNAVAILABLE, VOICE_NOT_AUTHORIZED.
Only VOICE_AUTHORIZED enters the normal live presentation path.

## Synchronization
Track audio duration, phoneme/viseme timing when available, gaze events, facial-expression events, pauses, and emphasis. If synchronization quality falls below threshold, prefer safe neutral presentation.

## Production readiness
Always-live is an engineering availability goal, not a perpetual-uptime promise. Production requires external runtime, HTTPS, authentication, authorization, secret management, monitoring, health checks, restart/recovery, rate limiting, audit logs, rollback, dependency-failure handling, fallback mode, and human review for high-impact claims.

GitHub Actions success is not production uptime evidence.

## Q&A tests
- provenance on source-backed answers;
- explicit abstention on insufficient evidence;
- identity/philosophy remains labelled;
- conflicting sources do not produce false certainty;
- unauthorized voice cannot render;
- missing audio cannot enter lip-sync;
- malformed provenance fails closed;
- unsupported claims never become VERIFIED;
- respectful language under adversarial prompts;
- audio/face timing stays within tolerance.

## Public UI
Keep the Shirmani visual language and add: Live Character, LIVE/DEGRADED/OFFLINE, voice authorization state, evidence state, current topic, transcript, provenance drawer, presentation controls, and safe fallback indicator.

No online/avatar status may imply scientific verification.

## Status
DESIGN READY / LIVE PRODUCTION NOT YET DECLARED.