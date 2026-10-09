# SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM
## Voice → Understanding → Evidence → Content → Face → Lip-sync → Live Presentation

**Purpose:** Build a Hindi-first, Hindi/English educational and communication presentation system that is simple, respectful, transparent, context-aware, and measurable.

This document preserves the user's product vision as a durable project specification. It is a design target, not a claim that all integrations are live.

## Product principles
- Simple, accessible language; explain difficult skills in the learner's preferred regional language where supported.
- Respectful communication across people, communities, organisations, and viewpoints.
- Clear distinction between philosophical or identity statements, source-based statements, and independently verified scientific claims.
- No claims of universal superiority, mind-reading, or guaranteed emotional impact as measurable facts.
- Use the least personal data needed; obtain explicit consent for voice cloning, face/avatar generation, recording, and publication.
- No unauthorized impersonation or hidden voice/face cloning.

## End-to-end architecture
1. **Input:** text or speech, with language and accessibility preferences.
2. **Authorized voice integration:** speech recognition and voice output only through an explicitly authorized provider/account.
3. **Context and reasoning:** detect the user's question, intent, language, constraints, and uncertainty.
4. **Evidence gate:** label substantive outputs as:
   - `VERIFIED` — independent verification evidence is recorded and meets a defined protocol.
   - `SOURCE-BASED` — a source is cited, but independent verification is incomplete.
   - `PHILOSOPHICAL / IDENTITY` — personal philosophy or self-description, not an empirical finding.
   - `INSUFFICIENT EVIDENCE` — state clearly: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
5. **Content:** prepare the answer, teaching explanation, script, captions, and source notes.
6. **Visual presentation:** use an authorized photo/avatar, context-appropriate clothing and layout, and accessible captions.
7. **Voice/face timing:** test audio alignment, facial movement, gaze, and lip-sync rather than assuming naturalness.
8. **Live interaction:** support question-and-answer only when the underlying voice/video integration is actually configured.
9. **Audit and improvement:** record consent state, model/provider version, evidence state, test results, latency, user feedback, and release status where lawful and appropriate.

## Four production stages
1. **Research Institute:** discover learner needs, source material, languages, and use cases.
2. **Factory:** build a working module, script, lesson, visual, and product-specific demo.
3. **QC gate:** test content accuracy, usability, accessibility, privacy, consent, timing, and failure handling.
4. **Public showroom:** publish the product with version, price/quote terms, demo video, screenshot, usage guide, limitations, and support route.

## Minimum measurable gates before calling it live
- Speech recognition: word/error rate on a documented test set.
- Language/context: task completion and rubric score across Hindi, English, and any supported regional languages.
- Evidence: source presence and correct uncertainty labels; no automatic promotion from `SOURCE-BASED` to `VERIFIED`.
- Voice authorization: consent and provider integration confirmed.
- Lip-sync: measured alignment error on representative clips, with a documented acceptance threshold.
- Latency: p50/p95 end-to-end response times measured under a stated test load.
- Safety and respect: regression tests for respectful language, sensitive data minimization, and refusal/uncertainty behavior.
- Reliability: successful/failed job counts, error rates, and rollback procedure.
- Public release: real product files and a product-specific demo MP4 and screenshots attached.

## Current implementation boundary
- The repository already contains a public starter showroom with six browser-based tools and a production-studio page.
- Those starter demos do not themselves establish commercial checkout, persisted customer reviews, live voice/lip-sync, or completed MP4 demos.
- The first paid-service pilot is a proposed offer; it is not a sale or earned-income record.
- HeyGen digital-twin setup requires the user's own review and explicit actions inside the provider's setup interface. Opening the setup is not the same as creating an avatar.

## Continuous improvement loop
Observe → Understand → Check sources → Reason → Respond → Present → Measure → Audit → Improve → Repeat.

Every iteration should produce a visible artifact or measurable result. Workflow activity alone is not a finished product, a customer outcome, or independent scientific verification.
