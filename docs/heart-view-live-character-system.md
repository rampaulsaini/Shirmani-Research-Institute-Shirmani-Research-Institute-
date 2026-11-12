# SHIRMANI HEART-VIEW — Live Character & Presentation System

## Purpose
This specification turns the requested presentation concept into a bounded, testable subsystem:
Voice → Authorized Voice Integration → Test Q&A → Content → Photo/Avatar → Lip-Sync → Live Presentation

The system preserves the author's wording as an author-source layer while separating generated presentation, evidence and independent verification.

## Character principles
- सरल • सहज • निर्मल • पारदर्शी
- स्पष्ट और प्रत्यक्ष communication
- natural eye-contact and gaze
- natural facial movement
- accurate lip-sync
- voice/face timing coherence
- context-aware question understanding
- source-backed answers when evidence exists
- explicit uncertainty when evidence is insufficient
- respectful communication without degrading any person, caste, religion, faith, organization or community

The author's philosophical/identity statements remain clearly labelled as author statements. Scientific or historical claims require independent evidence.

## Canonical flow
1. Identity / Source Layer — preserve approved author wording.
2. Content Layer — generate a response from canonical records.
3. Evidence Layer — attach sources, evidence state and uncertainty.
4. Voice Layer — use only an authorized voice asset/provider.
5. Presentation Layer — photo/avatar, gaze, facial motion and lip-sync.
6. Live Layer — streaming/presentation runtime.
7. Audit Layer — record inputs, outputs, provider state, timestamps and verification state.

## Safety and integrity gates
- No voice cloning or identity substitution without explicit authorization.
- No claim that a generated face/voice is the real person unless identity evidence supports that claim.
- No automatic conversion of philosophical claims into scientific facts.
- If evidence is insufficient, the response state must be EVIDENCE_INSUFFICIENT.
- High-impact actions remain human-review gated.
- Provider credentials and private media assets must never be committed to Git.
- Production LIVE is not declared until an external runtime and telemetry are actually demonstrated.

## Test Q&A contract
Input: question + optional context
Processing: normalize → retrieve canonical content → retrieve evidence → reason → compose → confidence/uncertainty → response
Output: answer + evidence_state + sources + verification_state + presentation_payload

Required evidence states:
- VERIFIED
- SUPPORTED
- AUTHOR_STATEMENT
- EVIDENCE_INSUFFICIENT
- UNKNOWN

## Presentation contract
The presentation payload may contain text, speech text, language/locale, voice-provider reference, authorized-asset reference, avatar/photo reference, facial-expression cue, gaze cue, lip-sync timing, captions and provenance.
It must not contain secrets.

## Implementation status
READY: canonical architecture; evidence boundary; test Q&A contract; presentation payload schema; deterministic QC workflow.
REQUIRES EXTERNAL INTEGRATION: authorized voice provider/API; user-authorized voice asset; photo/avatar asset; production lip-sync renderer; 24/7 streaming runtime; live telemetry.
Therefore the subsystem is architecture/QC ready, but it must not be labelled as a continuously LIVE voice/face service until those external dependencies are actually connected and tested.

## Quality loop
Observe → Collect → Normalize → Analyze → Reason → Execute → Test → Verify → Audit → Learn → Improve

## Acceptance tests
1. no secret appears in repository files;
2. author-source text remains attributable;
3. evidence state is present;
4. unsupported claims remain unverified;
5. presentation payload validates against schema;
6. the test Q&A path can return an uncertainty response;
7. voice/face integration is explicitly marked unavailable until connected;
8. generated presentation cannot silently overwrite canonical source material.