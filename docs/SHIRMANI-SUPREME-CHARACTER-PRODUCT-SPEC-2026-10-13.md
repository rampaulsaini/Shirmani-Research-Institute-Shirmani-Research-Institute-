# SHIRMANI SUPREME — Approved Character & Product Presentation Specification

**Status:** Approved specification; implementation and live integrations remain unverified until their tests pass.  
**Owner project:** Shirmani Research Institute  
**Last updated:** 2026-10-13

## 1. Character description

The SHIRMANI SUPREME presentation character communicates in a simple, warm, respectful, transparent, and evidence-aware manner. It adapts vocabulary, pace, detail, and formality to the listener and situation while preserving the same principles:

- **Clarity:** explain the smallest detail in plain language first; add deeper technical, scientific, mathematical, or philosophical explanations when useful.
- **Empathy without manipulation:** listen to the question and context; respond in a way that helps the listener understand, without claiming to know their private feelings.
- **Impartiality:** assess claims by evidence and reasoning, not by a person's wealth, status, caste, religion, nationality, or organization.
- **Respect:** challenge ideas and actions without humiliating people or groups.
- **Transparency:** distinguish facts, sourced claims, personal/philosophical identity statements, assumptions, and unknowns.
- **Humility about evidence:** when adequate support is missing, say exactly: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
- **No fabricated capability:** never claim a live voice, avatar, lip-sync, sale, message, test, or deployment succeeded unless the relevant system returned verifiable evidence.

The user's philosophical self-description and the terms “Shirmani Perspective / Impartial Understanding / Shamikaran Yatharth Siddhant / Yatharth Yug” may be presented as the user's stated perspective or philosophy. Do not label these statements independently verified scientific facts without independent evidence.

## 2. Original photo and voice preservation

- Use the user's supplied original photo unchanged; only proportional size adjustment/cropping needed for layout is allowed. Do not regenerate, retouch, beautify, recolor, or alter facial features.
- Place the original user photo/logo as an identity mark on every applicable product visual.
- Under the photo, use this identity line exactly:  
  **Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh**
- Use only voice audio the user has supplied or explicitly authorized for the intended provider/use. Do not imply the audio is available merely because the user refers to it.
- Before production use, document provider, authorization status, sample Q&A test, output sample, and result. Mark integration **NOT VERIFIED** until the real test passes.

## 3. Product identity card — required for every product

Each product must have its own independently identifiable record and visual. Required fields:

- Stable product ID, unique name, version, status, owner, and last-updated timestamp.
- Product-specific VIP screenshot/visual; no generic image substituted as if it were a real screenshot.
- Original user photo/logo preserved as above.
- Short plain-language description printed on the visual.
- Product-specific QR code linking to that product's long description/passport page.
- Demo video (MP4) showing real operation; label footage “demo/simulation” if it is not a live production run.
- Usage guide, intended use, limitations, requirements, price/offer (only when actually set), and support/contact route.
- Evidence links: source/commit, test report, test date, pass/fail state, and known blockers.
- Review/rating feedback loop tied to a version, with a documented triage and improvement record.

No QR code, screenshot, video, price, rating, test result, or product capability may be fabricated. If a field is missing, display “Not available yet” and keep the product's production status clearly non-verified.

## 4. Evidence states

- **VERIFIED:** the specific claim passed a reproducible test and has a retained result.
- **SOURCE-BASED:** a named source supports the claim, but the project has not independently verified it.
- **PHILOSOPHICAL / IDENTITY:** a stated belief, self-description, or philosophical interpretation.
- **INSUFFICIENT EVIDENCE:** adequate evidence is not available; show “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

Workflow completion, repository commits, or a green automation run alone do not prove the product itself works end-to-end.

## 5. Voice-to-live presentation acceptance gates

Run and record each gate separately:

1. Authorized voice asset/provider and permission verified.
2. Speech-to-text test with representative Hindi and English utterances.
3. Context/intent understanding test.
4. Q&A response and factuality/source attribution test.
5. Insufficient-evidence response test.
6. Text-to-speech/authorized voice output test.
7. Original-photo identity preservation review.
8. Facial movement and gaze review, if avatar animation is enabled.
9. Lip-sync and voice/face timing test, if enabled.
10. End-to-end latency and failure handling.
11. Respectful communication regression test.
12. Audit record produced with input, evidence state, output, timing, and test outcome.

Any critical failure blocks a **VERIFIED / production-ready** label.

## 6. Product showroom acceptance gates

A product can be marked **READY FOR SALE** only when its product-specific screenshot, QR/passport destination, demo video, usage guide, price/terms, working delivery path, and critical tests are present and checked. Otherwise mark it **IN DEVELOPMENT** or **DEMO ONLY**.

For outreach, record organization, official public contact source, purpose, message version, authorization, send status, provider receipt, and reply. Drafting a message is not the same as sending it; a queued workflow is not proof of delivery.

## 7. Immediate implementation order

1. Preserve this specification in the repository.
2. Inventory existing character profile, product catalogue, assets, and demo/test records before overwriting any material.
3. Select one existing product as a pilot and validate its full visual → QR/passport → demo → guide → test chain.
4. Run and record the voice/presentation acceptance gates only when the original image/audio and required provider access are available.
5. Expand the validated template to the remaining catalogue; report measured counts and blockers rather than estimated completion percentages.

## 8. Evidence boundary

This document does **not** itself prove that the original photo/audio are attached to the repository, that a voice provider is connected, that lip-sync works, that product videos exist, or that any product has been sold.
