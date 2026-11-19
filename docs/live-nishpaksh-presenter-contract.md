# निष्पक्ष समझ — Live Presenter System Contract

## उद्देश्य
यह subsystem user-authored निष्पक्ष समझ / शिरोमणि framework को evidence-bound live presenter experience में बदलने के लिए है:
Voice → authorized voice integration → Question/Answer → Evidence retrieval → Answer policy → Voice → Face/Lip-sync → Live presentation

यह किसी व्यक्ति की scientific superiority, universal truth, identity authenticity, या permanent digital consciousness को अपने-आप सिद्ध नहीं करता। Philosophical/identity statements और independently verified evidence अलग states में रहते हैं।

## Presenter experience
- सरल • सहज • निर्मल • पारदर्शी
- स्पष्ट और प्रत्यक्ष communication
- natural eye-contact / gaze when the selected presenter engine supports it
- natural facial movement
- accurate lip-sync
- voice/face timing coherence
- question context retrieval before answer generation
- evidence available → source-linked answer
- evidence insufficient → “अभी पर्याप्त प्रमाण उपलब्ध नहीं है”
- no denigration of any person, caste, religion, faith, community, organization, or group
- author-source statements remain labelled as author-source
- independently verified scientific claims require independent evidence

## State machine
1. INPUT_RECEIVED
2. CONTEXT_RETRIEVED
3. EVIDENCE_CLASSIFIED
4. ANSWER_COMPOSED
5. VOICE_AUTHORIZED
6. PRESENTER_AUTHORIZED
7. LIPSYNC_RENDERED
8. LIVE_READY
9. LIVE_PRESENTING
10. ARCHIVED

Fail-closed states:
- EVIDENCE_INSUFFICIENT
- VOICE_UNAUTHORIZED
- PRESENTER_UNAUTHORIZED
- LIPSYNC_UNAVAILABLE
- SOURCE_UNAVAILABLE
- VERIFICATION_REQUIRED

A failure must never be converted into a successful verification state.

## Evidence policy
Every substantive answer should carry:
- claim text
- claim class
- source references
- evidence state
- verification state
- provenance
- uncertainty / limitation

Recommended claim classes:
- AUTHOR_PHILOSOPHICAL
- AUTHOR_IDENTITY_STATEMENT
- EMPIRICAL_CLAIM
- HISTORICAL_CLAIM
- SCIENTIFIC_CLAIM
- SYSTEM_STATUS

AUTHOR_PHILOSOPHICAL and AUTHOR_IDENTITY_STATEMENT may be presented faithfully as the author's statements, but must not be labelled independently verified merely because they are stored in the repository.

## Voice / avatar authorization
The live subsystem must not invent or silently substitute a voice, avatar, face, photo, or digital twin.
Required before live presentation:
- explicit authorization/consent record
- exact selected voice or voice asset
- exact selected presenter/avatar look
- provenance for the selected photo/media where applicable
- engine compatibility
- successful test render
- audit record

## Privacy and safety
The public layer must never expose credentials, API keys, private voice identifiers, private asset URLs, or unnecessary personal data.
Public status may expose readiness states and provenance references without exposing secrets.

## Acceptance tests
### A. Evidence
- Answer with traceable source when evidence exists.
- Answer with the exact insufficiency state when evidence is inadequate.
- Never manufacture a citation.
### B. Identity
- Preserve author wording as author-source.
- Never claim biometric identity match without an independent verification record.
- Never convert a generated avatar into proof of real-person identity.
### C. Voice
- Unauthorized voice → blocked.
- Authorized voice → test Q&A permitted.
- Voice failure → no live presentation.
### D. Lip-sync
- Audio/script and presenter timing must share one render job.
- Failed render → LIPSYNC_UNAVAILABLE.
- No claim of real-time lip-sync until observed runtime telemetry exists.
### E. Respectful communication
- Do not demean groups or individuals.
- Separate disagreement from dehumanization.
- Preserve the user's philosophical framework without turning it into unsupported universal fact.

## Current status semantics
DESIGN_READY means the contract exists.
TEST_READY means required test assets and integration wiring exist.
LIVE_READY means an authorized presenter + voice + successful render + runtime checks are evidenced.
LIVE requires actual external runtime evidence. GitHub workflow success alone is not sufficient.