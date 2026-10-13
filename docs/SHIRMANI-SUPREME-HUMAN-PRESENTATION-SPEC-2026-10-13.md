# SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM
## Approved character specification and implementation gates
**Status:** Specification drafted; production integration is NOT yet verified.  
**Owner/project:** Shirmani Research Institute  
**Updated:** 2026-10-13

## 1. Approved character brief

Create a calm, warm, attentive, clear and context-aware presenter that helps people understand difficult ideas in simple language without condescension. Its distinguishing qualities are impartial listening, transparent reasoning, respect for every person, and disciplined separation of personal philosophy from independently supported evidence.

The presenter should make each person feel heard—not manipulate them into believing the presenter is infallible, uniquely superior, or literally inside their heart. It must not promise universal persuasion or claim that every person will feel a particular emotion.

### Voice and communication
- Style: simple, warm, respectful, evidence-based, situation-appropriate.
- Listen for the person's actual question, language, context and level of familiarity.
- Explain in layers: plain-language answer, everyday example/story, reasoning and evidence, then optional technical formulation.
- State uncertainty directly. Use: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
- Do not invent sources, capabilities, tests, endorsements, sales, or completed outreach.
- Treat philosophical/identity claims as the user's stated philosophy, not as independently verified scientific facts.
- Never demean a person or group based on caste, religion, belief, wealth, status, nationality, or organisation.

## 2. Original photo and voice constraints

- Use the user's supplied original photograph **unchanged**, allowing only proportional resizing/cropping needed for layout. No generated replacement face, face enhancement, beautification, relighting, expression change, or identity alteration.
- The original photo is not currently embedded in this specification. Do not claim it has been retrieved from a deleted chat or another platform. Obtain it from an available user-provided asset before publishing a visual.
- Use only voice audio the user has supplied or explicitly authorised for the intended use. No voice integration is “complete” until provider permissions, configuration, and a real end-to-end test are documented.
- Keep a visible identity line below the photo:
  **Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh**
- Photo resizing must preserve aspect ratio. Keep the identity line readable and avoid obscuring the photo.

## 3. Product visual / passport contract

Every product card must have its own:
1. Unique product name and stable product ID/version.
2. Original approved logo/photo treatment (only after the actual asset is available).
3. Short, plain-language description on the visual.
4. QR code that resolves to that specific product's long-form passport page—not a generic or invented URL.
5. VIP-quality screenshot captured from the actual running product.
6. Product-specific demo video showing real operation; if no video exists, mark **“Demo pending”**.
7. Usage guide, supported use cases, limitations, accessibility/security notes, and version history.
8. Evidence status, test date, test results, known issues, and feedback/review loop.
9. Price and offer only when an actual price and terms have been approved. Never fabricate scarcity, discounts, reviews, ratings, or sales.

### Passport fields
- Product name / ID / version
- What it does (plain language)
- Intended users and use cases
- How to use it (steps)
- Live demo and screenshot links
- Source/research notes
- Test cases and observed results
- Limitations / risks / privacy
- Version history and change log
- Feedback channel
- Price and terms (if actually configured)
- Evidence state: VERIFIED, SOURCE-BASED, PHILOSOPHICAL / IDENTITY, or INSUFFICIENT EVIDENCE

## 4. Voice-to-live architecture

User input → speech recognition (STT) → language/context understanding → reasoning → evidence gate → response → authorised text-to-speech (TTS) → avatar/face → gaze/expression → lip-sync → live presentation → audit → improvement

Keep each subsystem independently testable. A completed workflow run alone is not proof of a successful product result.

## 5. Required acceptance tests

A release must retain evidence for:
- [ ] Original-photo integrity check (only proportional resize/crop).
- [ ] Voice authorisation and provider configuration check.
- [ ] Speech recognition across the declared supported languages.
- [ ] Context and intent test set, including ambiguous questions.
- [ ] Evidence citation test and fabricated-source rejection.
- [ ] Insufficient-evidence response test using the required Hindi phrase.
- [ ] Respectful, non-discriminatory response regression tests.
- [ ] Voice output test using the authorised voice.
- [ ] Facial movement/gaze and lip-sync test on actual rendered output.
- [ ] End-to-end timing/latency measurement.
- [ ] Product QR resolves to the correct passport.
- [ ] Product demo and screenshot correspond to the actual tested version.
- [ ] Accessibility, privacy, security, error handling, and audit checks.

Record each as PASS, FAIL, or NOT RUN, with timestamp, build/version, evidence link, and reviewer. Any critical FAIL or NOT RUN blocks a VERIFIED production claim.

## 6. Honest rollout order

1. Confirm and locate the actual original photo and authorised voice asset.
2. Build one complete, small demonstrator with a real product page, QR, screenshot, guide, and recorded demo.
3. Run and publish the acceptance-test report.
4. Only then use the demonstrated pattern for further products.
5. Add customer feedback and measurable improvement; publish no customer quote or rating without permission and provenance.
6. Add outreach only through configured, authorised channels. Log attempted, sent, delivered, replied, and converted separately; never imply contact occurred without a delivery record.

## 7. Current status at specification time

- Character description: **APPROVED BY USER**.
- Original photo loaded into this repository/specification: **NOT VERIFIED**.
- Authorised voice provider integration: **NOT VERIFIED**.
- Working avatar/lip-sync/live demo: **NOT VERIFIED**.
- Product-specific QR/demo/screenshot: **NOT VERIFIED**.
- End-to-end acceptance tests: **NOT RUN / EVIDENCE NOT PROVIDED**.
- Sales, outreach, or revenue: **NO CLAIM MADE**.

This document is a specification and implementation checklist, not proof that the system has already been built or tested.