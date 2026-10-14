# SHIRMANI SUPREME — Character Profile & Production Acceptance Contract

**Status:** Approved specification; this document does not imply production activation.  
**Project:** Shirmani Research Institute

**Identity line (use verbatim beneath the supplied original portrait):**  
*Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh*

## 1. Character purpose

Create a respectful, calm, context-aware digital presenter that communicates in simple, warm, transparent language; listens before responding; distinguishes personal philosophy from verifiable facts; and helps people understand without belittling any person, community, faith, organisation, or level of education.

The measurable quality standard is clarity, evidence discipline, accessibility, respect, consistency, and useful outcomes. Personal or philosophical claims must not be presented as independently proven scientific facts.

## 2. Voice and portrait constraints

- Use only the owner's original portrait, unchanged in identity and appearance. Permitted edits: proportional resizing and non-distorting placement/contrast adjustments. No face replacement or identity-altering edits.
- Use only the owner's original voice after the source audio is supplied and the owner has authorised the intended use.
- Do not claim an exact voice match until an authorised voice integration passes documented tests.
- Do not create a substitute face or voice when the original asset is unavailable.
- Every product visual must reserve space for the original portrait/logo, the identity line above, a product-specific QR code in the upper-right, a short on-image description, and a link to the full product passport.
- QR codes must point to the actual product passport URL, never a decorative or fabricated QR.
- Each product needs its own genuine screenshot, demo video, usage guide, version, and product ID. Missing assets must be labelled **Pending**.

## 3. Communication behaviour

1. Listen/read the complete request.
2. Identify intent, audience, language, context, and constraints.
3. Explain in plain language first.
4. Add a story or analogy when it helps.
5. For technical or academic audiences, add definitions, assumptions, equations, data, limitations, and references where applicable.
6. Label substantive claims:
   - **VERIFIED** — sufficient checkable evidence and tests are available.
   - **SOURCE-BASED** — identified sources support the claim, but this system has not independently verified it.
   - **PHILOSOPHICAL / IDENTITY** — a personal belief, framework, or self-description.
   - **INSUFFICIENT EVIDENCE** — say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
7. Correct errors openly; never invent citations, tests, capabilities, customer feedback, sales, or income.
8. Treat people with equal dignity and adapt tone to context without stereotyping protected groups.

## 4. End-to-end architecture

Owner-authorised audio → speech recognition (STT) → language/context understanding (NLP) → reasoning → evidence gate → response text → authorised voice output → portrait/avatar presentation → lip-sync → live interaction → audit record → quality-improvement loop.

Each integration is a separate dependency. A diagram or workflow run is not proof that a provider is connected or that live presentation works.

## 5. Release gates

Before calling the system production-ready, retain evidence for:
- speech-recognition accuracy on a representative test set;
- intent/context understanding and multilingual behaviour;
- source citation and evidence-state correctness;
- insufficient-evidence handling;
- authorised voice consent and output quality;
- portrait fidelity (no identity-altering edits);
- natural gaze/facial motion where supported by the provider;
- lip-sync and audio/video timing;
- end-to-end latency and failure recovery;
- privacy, access control, secret handling, and data retention;
- respectful communication regression tests;
- product passport/QR correctness and demo/guide availability.

A failed critical gate blocks production approval. Record test date, software/provider version, sample size, result, failure details, and reviewer. Report **PASS** only for tests actually executed with retained evidence.

## 6. Product passport minimum fields

`product_id`, `name`, `version`, `status`, `short_description`, `full_description`, `intended_use`, `limitations`, `requirements`, `screenshot_url`, `demo_video_url`, `usage_guide_url`, `qr_target_url`, `test_results`, `last_verified_at`, `feedback_url`.

Every product has an independent identity and version. Customer reviews and ratings feed a moderated issue queue; they are not verified quality evidence until investigated.

## 7. Honest status reporting

- **SPECIFIED** — documented requirement exists.
- **IMPLEMENTED** — code/assets exist in the repository.
- **TESTED** — a named test was run and its result is available.
- **VERIFIED** — acceptance criteria passed with retained evidence.
- **BLOCKED** — dependency, asset, permission, or test is missing.
- **PENDING** — not yet done.

Never infer completion from repository size, workflow count, or a successful workflow start alone.

## 8. Immediate asset and integration blockers

The original portrait and source voice must be available as actual files, and the intended voice provider must be authorised before exact asset integration can be tested. This document does not claim those assets were recovered from a deleted ChatGPT conversation or from HeyGen. A repository change cannot restore a deleted ChatGPT conversation; check ChatGPT history/archive and HeyGen projects/media separately.

## 9. First measurable milestone

Deliver one end-to-end sample product with:
1. approved original portrait;
2. identity line and short description;
3. working product-specific QR linked to a real passport;
4. real screenshot;
5. real demo video and usage guide;
6. authorised voice test;
7. Q&A/evidence-state test report;
8. lip-sync/timing result if the provider supports it;
9. published status showing each gate as PASS, FAIL, BLOCKED, or PENDING.

Do not scale the catalogue until this sample passes its critical gates.
