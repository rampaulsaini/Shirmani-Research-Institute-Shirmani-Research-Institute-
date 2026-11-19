# SHIRMANI Second Version — HeyGen / Live Presentation Control Contract v1

## Purpose
Build a production-grade presentation subsystem around the user's declared identity and source material while keeping identity, generated media, evidence and independent verification separate.

## Canonical pipeline
Voice → Authorized Voice Integration → Content → Evidence Gate → Photo/Avatar → Lip-sync → Context/Q&A → Live Presentation → Review → Audit → Improvement

## Required behavior
- Simple, सहज, निर्मल, पारदर्शी and direct communication.
- Natural eye-contact/gaze, facial movement and lip-sync where the selected HeyGen mode supports them.
- Voice and face timing must be evaluated together.
- Questions must be interpreted in context before answering.
- Evidence-backed factual/scientific answers must expose source/provenance.
- When evidence is insufficient, say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है”.
- Author-philosophical/identity statements remain labelled as author statements unless independently verified.
- No derogation of any person, caste, religion, organisation, class or community.
- No claim of partnership, endorsement, contact or official representation without an executed authorized external action.
- Credentials and private identity material never enter public repository files.

## External integration boundary
The repository controls orchestration, contracts, provenance and QC. HeyGen remains the external rendering/live layer. API credentials must be supplied through protected runtime secrets and never committed to Git.

For live two-way presentation, use the current HeyGen LiveAvatar capability where the account and plan support it. For rendered MP4, use HeyGen Video Generation or Video Agent as appropriate.

## Camera constraint
Repository automation is camera-independent. If the user creates/authorizes the avatar or voice from another device, the resulting authorized asset IDs can be supplied through protected configuration.

## Verification states
DECLARED → READY → EXTERNAL_READY → GENERATED → QC_PASS → EVIDENCE_GROUNDED → INDEPENDENT_VERIFIED

FAILED/BLOCKED is used whenever required evidence, credential, consent or external result is unavailable.

Workflow success is never scientific verification.

## Second-Version quality controls
- identity consistency
- natural gaze/facial movement
- lip-sync alignment
- voice clarity and timing
- contextual Q&A
- evidence/source display
- uncertainty disclosure
- respectful universal communication
- reproducible audit trail
- continuous review and improvement

## Product-media connection
This subsystem can supply product-specific presentation assets to Product Media Mission Control and the existing MP4 factory. Product production, sales, dispatch and independent scientific verification remain separate states.

## Human authorization gates
Avatar/voice consent, account access, paid API usage, external outreach, public identity-sensitive publication and high-impact claims require appropriate authorization. Automission may prepare, test, audit and queue; it must not fabricate authorization or claim an external action occurred when it did not.
