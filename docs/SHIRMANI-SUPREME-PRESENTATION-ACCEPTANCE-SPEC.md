# SHIRMANI SUPREME — Character & Product Presentation Acceptance Specification

**Status:** Approved specification; implementation remains unverified until tests and artifacts are checked.  
**Last updated:** 2026-10-12

## 1. Approved character description

Present the character in a simple, warm, clear, respectful, transparent, evidence-aware style adapted to the listener and situation. Explain difficult ideas in plain language first, then offer deeper technical detail when useful. Listen for context before answering; distinguish fact, interpretation, personal philosophy, and uncertainty. Cite sources for factual claims where available and say **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है”** when evidence is insufficient. Do not demean people or groups, and do not claim universal or scientific proof for philosophical/identity statements without independent evidence.

Intended values: simplicity, ease, clarity, humility, transparency, impartiality, compassion, and continuous improvement. Avoid exaggerated claims of being uniquely superior, infallible, or scientifically proven. Quality is demonstrated through measurable tests, user feedback, source quality, and audit records.

## 2. Original identity assets — strict handling

- Use only the user's authorized original photograph and voice asset.
- Photograph handling: preserve original image content; resizing for layout is permitted, but do not alter facial features, skin, expression, or identity.
- Do not synthesize a replacement face or substitute another person's image.
- Voice use requires an authorized source asset/provider. Do not label voice integration complete until an actual end-to-end test passes.
- If the original asset is absent from the repository/runtime, show “original asset required”; never silently substitute a stock image or voice.
- Do not claim a previous ChatGPT conversation has been restored. Work from available repository files and supplied assets only.

## 3. Required product card / VIP visual

Every product must have a unique stable ID and its own:
1. VIP screenshot / product-specific image;
2. short plain-language description visible on the image/card;
3. QR code pointing to that product's long-form passport page;
4. demo video (prefer MP4) showing a real, reproducible workflow;
5. usage guide, requirements, limitations, version, and evidence status;
6. tests and known issues; and
7. review/rating feedback loop linked to documented improvements.

Use the user's original photograph as a logo on each product visual, with size adjustment only. Under the image, render this exact identity line:

> Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh

Place the product-specific QR in the upper-right where the layout permits. QR targets must resolve to the matching product passport, not a generic homepage. If a real demo video or original photo is unavailable, label the item “pending asset”; do not imply it exists.

## 4. Voice-to-live presentation pipeline

Voice input → authorized voice integration → speech-to-text → context/intent understanding → response reasoning → evidence gate → content → authorized voice output → face/avatar asset → gaze/expression → lip-sync → live presentation → audit → improvement.

A static mock-up or workflow run alone is not proof of production readiness.

## 5. Evidence states

- **VERIFIED:** a defined test or claim passed with recorded evidence and reproducible method.
- **SOURCE-BASED:** reliable source(s) are cited, but independent verification is incomplete.
- **PHILOSOPHICAL / IDENTITY:** personal belief, value, self-description, or philosophical proposition.
- **INSUFFICIENT EVIDENCE:** evidence is missing, weak, or conflicting; display “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

Do not present philosophical statements as scientific facts by style alone.

## 6. Minimum acceptance tests

- [ ] Original photograph exists and source/hash is recorded; only size/layout changes are applied.
- [ ] Authorized voice asset/provider and authorization are recorded.
- [ ] Speech-to-text passes representative Hindi and English tests.
- [ ] Context-sensitive Q&A passes, including ambiguous questions.
- [ ] Evidence gate distinguishes sourced claims, philosophy, and insufficient evidence.
- [ ] Lip-sync and voice/face timing are measured on an actual generated clip.
- [ ] Product card shows unique ID, short description, original-photo logo, identity line, and product-specific QR.
- [ ] QR is scanned and resolves to the matching passport URL.
- [ ] Demo MP4 plays and demonstrates the documented workflow.
- [ ] Usage guide matches the current version and discloses limitations.
- [ ] Failures, artifacts, timestamp, and commit are recorded.
- [ ] No “complete”, “verified”, “live”, or revenue claim is made without evidence.

## 7. Product passport fields

`product_id`, `name`, `version`, `short_description`, `long_description`, `intended_use`, `limitations`, `requirements`, `screenshot_path`, `demo_mp4_path`, `usage_guide_path`, `qr_target`, `test_status`, `evidence_links`, `known_issues`, `feedback_url`, `last_verified_at`.

## 8. Honest delivery and income workflow

For current services (Hindi/English writing, research summaries, website/blog content), each enquiry must receive a written scope, deliverables, deadline, price, revision policy, and payment terms before work starts. Outreach must use verified official contact channels and be authorized. Track attempted/sent/replied/quoted/paid separately; never infer a sale or income from a draft, page view, or sent message.

## 9. Implementation status

This document records approved requirements. It does **not** prove that photo/voice integration, QR generation, demo videos, live lip-sync, outreach, sales, or production deployment are complete. Update status only after inspecting the artifact and running the relevant test.
