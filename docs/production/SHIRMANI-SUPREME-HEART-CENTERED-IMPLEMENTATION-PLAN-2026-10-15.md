# SHIRMANI SUPREME — Heart-Centered Character Implementation Plan
**Date:** 2026-10-15  
**Product ID:** SRI-PRES-001  
**Status:** IMPLEMENTATION PLAN — not a claim of live or production readiness  
**Owner/identity wording:** Shiromani Rampal Saini (user-provided identity and philosophy)

## 1. Product promise
Create a respectful, context-aware presentation assistant that listens carefully, identifies what is being asked, distinguishes evidence from interpretation, explains in plain language first, and can optionally present an approved answer through an authorized voice and avatar. It should help people think clearly, not pressure them to agree, disclose, buy, or become dependent.

The user's philosophical vocabulary—“निष्पक्ष समझ”, “हृदय का दृष्टिकोण”, “यथार्थ सिद्धांत”, “संपूर्ण संतुष्टि की निरंतरता”, “शिरोमणि स्वरूप”—is preserved as the product's declared philosophy and identity language. These expressions must not silently be presented as independently proven scientific claims.

## 2. Character constitution
- **Simple:** begin with a short, everyday-language answer.
- **Attentive:** reflect the user's actual question before expanding; ask only for missing information that changes the answer.
- **Gentle and respectful:** do not shame, flatter manipulatively, threaten, or demean a person or group.
- **Transparent:** state what is known, inferred, untested, unavailable, or outside the system's abilities.
- **Impartial in method:** apply the same evidence standard regardless of wealth, status, caste, religion, gender, nationality, institution, or viewpoint.
- **Useful:** end with a concrete next step, decision aid, or testable action where appropriate.
- **Non-coercive:** never claim that every person will love the character, that it is infallible, or that it knows every living and non-living thing.
- **Privacy-aware:** collect only the information needed; do not expose private conversations or source media in public pages without explicit permission.

## 3. Explanation ladder: one answer, five levels
1. **One-sentence answer:** the direct point.
2. **Very simple explanation:** everyday words, no jargon.
3. **Example or short story:** a concrete case and, when useful, a counterexample.
4. **Reasoning and evidence:** assumptions, sources, calculation/test method, uncertainty and limitations.
5. **Technical/research layer:** formal definitions, equations, data, reproducible steps, failure cases and citations.

The user can choose a level; the assistant should adapt to audience understanding rather than assume intelligence, education or background.

## 4. Claim and evidence labels
- **VERIFIED:** a defined test or independent check passed; attach its result, date, version and provenance.
- **SOURCE-BASED:** a source exists and is cited, but independent verification is not claimed.
- **PHILOSOPHICAL / IDENTITY:** personal philosophy, values, identity statement or interpretation.
- **INSUFFICIENT EVIDENCE:** evidence is missing, conflicting or too weak; say “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
- **NOT RUN / NOT VERIFIED / BLOCKED:** a required test has not run, has no result, or a critical prerequisite is missing.

Never use a label as decoration. A label must map to a specific claim and its evidence record.

## 5. End-to-end architecture
User audio/text → consent and input handling → speech-to-text (if audio) → language/context/intent → retrieval of approved sources → answer draft → claim segmentation → evidence gate → plain-language explanation ladder → user review where needed → authorized TTS/voice → approved portrait/avatar → lip-sync/render → playback/live session → quality audit → correction and versioned improvement.

Keep components replaceable. Provider-specific code belongs behind adapters; local prototype must remain clearly marked when adapters are disconnected.

## 6. Release versions
### V1 — Transparent response workbench
- Text input, language/context handling, five-level explanation, source and uncertainty labels.
- Manual evidence/source fields and downloadable response record.
- No claim of external model, voice clone, avatar or live streaming unless actually connected.

### V2 — Authorized voice and media
- Import the user's own original photo/audio only through an authorized route.
- Record consent/authorization, file provenance, SHA-256, duration, MIME type and provider asset IDs.
- Preserve the portrait unchanged except proportional scaling/cropping required by the approved layout.
- Test speech recognition, voice playback, pronunciation and audio quality against approved samples.

### V3 — Avatar and interactive presentation
- Connect a real provider project and capture provider job/video IDs and final output URLs.
- Test face/voice timing, lip-sync, gaze, facial motion, captions and failure recovery on real generated outputs.
- Clearly disclose that the presenter is AI-generated or AI-assisted.
- Do not call it live until a real interactive session has been tested.

### V4 — Production operations
- Authentication, role-based access, secret management, rate limits, abuse prevention, privacy controls, observability, backups and incident response.
- Scheduled tests, regression suite, rollback and versioned releases.
- Operational on-call/hosting and provider quotas are explicit dependencies; a static GitHub Pages site alone cannot guarantee 24/7 processing.

## 7. Acceptance gates and measurable metrics
| Gate | Evidence required | Release condition |
|---|---|---|
| Original photo | Exact original file, SHA-256 and authorization record | Hash/authorization match |
| Authorized voice | Exact audio file, SHA-256 and consent record | Hash/authorization match |
| Speech recognition | At least 20 agreed Hindi/English utterances with transcripts | Report word/error rates; threshold approved before test |
| Q&A reasoning | 20 representative questions with expected answer criteria | Human review record; critical factual errors = 0 in the acceptance set |
| Evidence handling | Supported, conflicting and missing-source cases | Correctly separates all four evidence states |
| Lip-sync | Actual rendered samples and frame/audio inspection | Measured sync result meets declared threshold |
| Timing/latency | Timestamped input, first response audio, render and playback | P50/P95 measured; limits declared before release |
| Respect/regression | Cross-context test set with human rubric | No unresolved critical disrespect or coercion defect |
| Privacy/security | Access tests, secret scan, retention and deletion checks | Critical security findings = 0 |
| Live session | Actual connected session log and successful end-to-end run | Session proven; no inference from workflow status alone |

A threshold must be declared before testing; do not retrofit a threshold after seeing results. Store run ID, commit SHA, provider/model version, test-set version, timestamps, failures and reviewer.

## 8. Four-version product packaging
- **Primer / V1:** response workbench and sample explanations.
- **Creator / V2:** approved voice and media asset handling.
- **Presenter / V3:** generated avatar videos and interaction tests.
- **Studio / V4:** governed production deployment, monitoring and integrations.

These are proposed tiers, not currently available paid plans. Do not publish prices, availability, performance guarantees or sales claims until cost, scope and support terms are confirmed.

## 9. Public showroom card
**Name:** SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM  
**Tagline:** “Listen carefully. Explain simply. Show the evidence.”  
**Description:** A staged Hindi/English communication and presentation system designed around respectful listening, clear explanations, source transparency and optional authorized voice/avatar output.  
**Demo:** Link only to a successfully generated and checked video.  
**Photo:** Use the approved original portrait without identity-altering edits; keep a placeholder until the original file and hash are verified.  
**QR:** Do not represent a placeholder as a working QR. Add only after its final destination is published and tested.  
**Current status:** Prototype and specification exist; original media hash match, authorized voice match, live provider integration, end-to-end tests and release gates remain separately tracked.

## 10. Operational improvement loop
Collect opt-in feedback → classify defect → reproduce with a test case → update prompt/code/data with provenance → run regression tests → human review for consequential changes → publish version notes → monitor rollback signals. Feedback is not proof of correctness; usage data must be minimized and handled with consent.

## 11. Immediate next actions
1. Inspect existing character studio and current HeyGen video records.
2. Preserve successful output IDs and mark failed renders as failed rather than retrying silently.
3. Match the actual original photo and voice files to their expected hashes.
4. Run 20 Hindi/English Q&A cases and the evidence/insufficient-evidence suite.
5. Perform face, lip-sync, timing and latency review on actual generated outputs.
6. Publish only a preview/demo whose media URL and permission are confirmed.
7. Make the release decision from recorded evidence; otherwise keep status BLOCKED.

## 12. Explicit limitations
This plan does not itself restore a deleted HeyGen or ChatGPT conversation, clone a voice, authenticate a pasted identifier, create a live stream, send outreach, prove an identity claim, or guarantee permanent uptime. Such outcomes require real provider operations, permissions, deployed infrastructure and test evidence.
