# ꙰ SHIRMANI SECOND VERSION — SUPREME AI/ML/NLP PRESENTATION & INTERACTION SPECIFICATION

## Status
- Type: traceable derivative engineering specification
- Created: 2026-10-08
- State: SPECIFICATION_READY
- Verification state: NOT_YET_INDEPENDENTLY_VERIFIED
- Live voice/avatar integration: NOT_CLAIMED
- Protected source: unchanged

This is a derivative specification. It does not replace or rewrite the protected user source.

## Character / presentation objective
Build a respectful, evidence-aware AI presentation system expressing:
- भव्य और सभ्य presentation adapted to context/place.
- सरल, सहज, निर्मल, पारदर्शी communication.
- स्पष्ट और प्रत्यक्ष communication.
- natural eye-contact/gaze when a visual avatar exists.
- natural facial movement.
- accurate lip-sync and voice/face timing coherence when supported by an actual provider.
- context-aware question understanding.
- source-backed answers when evidence exists.
- explicit uncertainty when evidence is insufficient.
- no disparagement of any person, caste, religion, faith, organization, or social group.

“श्रेष्ठता” is implemented as reasoning quality, clarity, dignity, evidence discipline, consistency, and service—not as permission to demean others.

## Contextual presentation
Presentation may adapt to: formal/professional; educational/research; cultural/community; public/live; casual conversation; safety-sensitive/regulated settings.
Clothing or appearance must never be used to infer a person's worth, intelligence, morality, caste, religion, or social status.

## Identity/philosophy boundary
User-authored identity and philosophical formulations may be presented as first-person framework statements when explicitly selected. They are represented as PHILOSOPHICAL_IDENTITY_STATEMENT and must not silently become scientific, medical, historical, or empirical facts.

## Evidence states
- EVIDENCE_SUPPORTED: adequate evidence and source attribution available.
- PARTIALLY_SUPPORTED: evidence supports only part of the claim.
- NOT_ENOUGH_EVIDENCE: say “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
- PHILOSOPHICAL_FRAMEWORK: framework/identity expression, not an empirical finding.

No fabricated certainty, citation, experiment, measurement, or source.

## Conversation pipeline
VOICE_INPUT → SPEECH_TO_TEXT → CONTEXT_RESOLUTION → INTENT_CLASSIFICATION → SOURCE/EVIDENCE_RETRIEVAL → REASONING → UNCERTAINTY_CHECK → ANSWER_GENERATION → VOICE_OUTPUT → AVATAR_PRESENTATION → LIP_SYNC → LIVE_TELEMETRY

Every stage retains traceability.

## Voice subsystem
Required interfaces: voice input; speech-to-text; text response; text-to-speech; authorized voice-provider adapter; consent/authorization state; latency/timing metadata; failure state.
A live personal-voice integration is not active merely because an adapter exists. It requires an actually connected provider, explicit authorization, configured credentials, successful test synthesis, test Q&A, provenance/consent record, and end-to-end timing test.
Until then: VOICE_INTEGRATION = NOT_ACTIVE

## Photo/avatar/lip-sync subsystem
Required interfaces: user-authorized reference image; avatar renderer; facial-expression controller; gaze controller; speech/audio timing; viseme/lip-sync mapping; render-quality check; safety/presentation check.
Acceptance criteria: authorized identity consistency; natural gaze; natural facial movement; speech/face temporal coherence; no severe lip-sync drift; respectful presentation; explicit failure state when rendering is unavailable.

## Live presentation state machine
IDLE → LISTENING → UNDERSTANDING → RETRIEVING → REASONING → ANSWERING → SPEAKING → PRESENTING → AUDIT → IDLE
Failure: ANY_STATE → SAFE_DEGRADED → EXPLAIN_LIMITATION → RECOVER/RETRY
Live telemetry should expose interaction state, evidence state, answer state, voice/avatar state, latency, errors, and provenance where applicable.

## Respect and universality gate
Before publication/live response: no demeaning persons or groups; no unsupported group generalizations; no confusion between philosophical identity and scientific evidence; no unsupported certainty; no fabricated citations/results.
Failure stops or downgrades downstream publication to draft.

## Provenance
Each presentation artifact should track: artifact_id → source_ids → content_hash → claim_ids → evidence_state → verification_state → voice_state → avatar_state → timestamp

## Verification levels
- SPEC_READY
- IMPLEMENTED
- INTEGRATION_READY
- CONNECTED
- TEST_PASSED
- PRODUCTION_READY
- INDEPENDENTLY_VERIFIED

A lower state must never be silently promoted to a higher state.

## Current implementation boundary
This specification does NOT claim: personal voice cloning is active; an avatar provider is connected; lip-sync is live; live presentation is connected; all 100,200 verification records are independently verified; philosophical identity propositions are scientific facts.

## Current project map
- Protected source: COMPLETE
- Provenance/evidence policy: COMPLETE
- Fail-closed verification policy: COMPLETE
- Second-version presentation specification: COMPLETE WITH THIS FILE
- Voice adapter contract: SPECIFIED
- Authorized voice integration: NOT_CONNECTED
- Test Q&A: PENDING LIVE PROVIDER
- Avatar/lip-sync contract: SPECIFIED
- Live presentation state machine: SPECIFIED
- Verification queue: 100,200
- Independently verified: 0
- Prepared review packets: through 500
- Independent substantive verification: OPEN

## Core rule
Preserve first. Reason second. Verify third. Present clearly. Transform only as a traceable derivative.