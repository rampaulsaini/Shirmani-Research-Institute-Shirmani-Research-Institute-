# ꙰ SHIRMANI Live Presentation Subsystem

Status: implementation scaffold — fail-closed until each real adapter is connected and tested.

## Flow
**Voice → Authorized Voice Integration → Test Q&A → Content → Photo/Avatar → Lip-sync → Live Presentation → Evidence/Verification Gate**

## Implemented / represented by this contract
- Static live-presentation interface.
- User-selectable portrait and audio for local preview.
- Browser speech-synthesis fallback for Q&A testing.
- Evidence-gated response rule with the exact insufficient-evidence phrase: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है”**.
- Audio-reactive mouth timing demo.
- Explicit boundary between user-authored identity/philosophy and independently verified factual/scientific claims.
- Provider adapter boundary: no external voice cloning is enabled merely by opening the page.
- Production lip-sync is not claimed complete until phoneme/viseme timing is available and tested.

## Required presentation behavior
- सरल • सहज • निर्मल • पारदर्शी communication.
- स्पष्ट और प्रत्यक्ष उत्तर.
- Natural eye-contact/gaze where the selected visual system supports it.
- Natural facial movement rather than exaggerated animation.
- Voice and face timing must remain coherent.
- Questions must be interpreted in context before answering.
- Evidence-backed factual answers should expose their source.
- Insufficient evidence must fail closed with: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है”**.
- Philosophical/identity statements must remain visibly distinguishable from independently verified scientific evidence.
- No person, caste, religion, faith, organization, or socioeconomic group is to be demeaned.

## Authorization model
External voice-provider integration requires explicit authorization and provider credentials. The repository must not manufacture consent, credentials, provider connection state, or verification.

## Adapter contract
Logical adapter operations: `healthcheck`, `synthesize(text)`, `render_avatar(audio, visual_asset)`, `validate_lipsync(audio, rendered_media)`, `answer(question, context)`, `evidence_status(answer)`, `publish_live(payload)`.

Provider-specific implementations remain outside the core contract. Credentials belong only in GitHub Actions secrets or an approved secret store.

## Fail-closed gates
### Voice
- Authorization confirmed.
- Provider healthcheck passes.
- Synthesis succeeds.
- Logs contain no credentials.

### Q&A
- Context is preserved.
- Evidence-backed claims include source metadata when available.
- Unsupported factual claims fail closed.

### Visual
- Approved portrait/avatar asset exists.
- Facial animation meets acceptance criteria.
- No unintended identity substitution.

### Lip-sync
- Audio/render durations are coherent.
- Phoneme/viseme timing passes configured tolerance.
- Failure blocks live promotion.

### Live
- All upstream gates pass.
- Respect/safety checks pass.
- Evidence status is visible.
- A failed gate can never be reported as `LIVE_READY`.

## User-provided source asset fingerprints
- Photo SHA-256: `562f03564d1c1f5f90b9aaab5ecc9fecce471345d9dbfbdd8c34ba18e2110631`
- Audio SHA-256: `2d7bbdee9338dcc87217ba40aecf72a2a2abd455f4a4bd9cdee8e084730dc0ba`
- Audio: mono, 48 kHz, 176.485 seconds.

These fingerprints identify files supplied in the work session; binary assets are not silently uploaded by this change.

## Source preservation
The original user source record is authoritative and immutable. Derived implementation may structure and test it but must not silently rewrite, normalize, translate, shorten, or replace it.

## Completion definition
`SOURCE → CONTENT → VOICE → VISUAL → LIP-SYNC → LIVE → INDEPENDENT TEST → VERIFIED`.

Every promoted capability requires a reproducible verification record.

## Current production boundary
The repository can implement contracts, test harnesses, readiness telemetry, and fail-closed orchestration without external credentials. Actual same-voice synthesis, avatar rendering, and live streaming require an explicitly authorized external provider and approved assets; these must not be fabricated.