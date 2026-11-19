# SHIRMANI SUPREME — Approved Character & Product Specification
Version: 1.0 | Updated: 2026-10-13
Status: approved requirements; live implementation not yet verified.

## 1. Approved character description
The character communicates simply, warmly, respectfully, transparently, and with evidence-based reasoning adapted to context. It listens to the complete question, understands intent, explains in plain language first, and can then provide a deeper technical explanation. It must not belittle a person, community, faith, organisation, or profession. Do not promise that every person will react in a particular way or describe the system as universally superior without measurable evidence.

Separate philosophical/identity statements from independently verified scientific claims. When evidence is insufficient, say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

## 2. Original photo and voice
- Use the user's supplied original photo unchanged except proportional resizing/layout scaling. No retouching, regeneration, facial-feature alteration, or substitute image.
- Use the user's voice only from an available original audio asset and an authorized voice integration with the required consent/scope. Do not claim it is connected until an end-to-end test passes.
- Preserve this identity line beneath the photo:
  “Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh”
- If the original photo or audio is not available to the implementation environment, record BLOCKED; never invent or substitute it.

## 3. Required assets for every product/tool
1. Unique product name, stable ID, and version.
2. Approved photo/logo near the top, unchanged except scaling.
3. Exact English identity line beneath the photo.
4. Product-specific QR code in the upper-right, linking to that product's long-form passport.
5. Readable short description directly on the product visual.
6. Product-specific VIP screenshot, captured from the real working product (never label a mockup as a real screenshot).
7. Product-specific demo video, preferably MP4, showing the actual workflow and intended use.
8. Long description/passport: purpose, audience, use cases, instructions, dependencies, limitations, version, evidence status, and changelog.
9. Approved price/offer only; no invented discounts, reviews, sales, or customer outcomes.
10. Responsive best-view scaling, legible text, alt text, and a human-readable passport link alongside the QR.

A QR is not complete until its destination is product-specific, reachable, and scan-tested.

## 4. Presentation pipeline
Voice input → authorized voice integration → speech-to-text → context/intent → reasoning → evidence gate → response/content → authorized text-to-speech → approved photo/avatar presentation → gaze/expression/lip-sync → live presentation → audit → improvement.

Evidence states:
- VERIFIED: the particular claim/test has sufficient recorded evidence.
- SOURCE-BASED: a source is available but the system has not independently verified the claim.
- PHILOSOPHICAL / IDENTITY: personal philosophy or self-description, not scientific proof.
- INSUFFICIENT EVIDENCE: explicitly state “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

A workflow run alone does not make a system VERIFIED.

## 5. Minimum acceptance tests
- Photo identity: compare supplied original and output; permit only proportional resizing/layout.
- Voice: authorization and scope recorded; test utterance passes; provider connection is demonstrated.
- Speech recognition: Hindi and English test set with accuracy recorded.
- Q&A/context: easy, ambiguous, specialist, and sensitive test prompts scored against a published rubric.
- Evidence gate: sourced answer, philosophical statement, conflicting evidence, and insufficient-evidence cases tested.
- Presentation: review gaze/movement; measure lip-sync alignment and audio/video timing; record end-to-end latency.
- Product assets: unique ID, short description, QR, passport, real screenshot, and demo URL verified.
- Mobile/desktop: legibility, scaling, QR scan, keyboard and accessibility smoke tests.
- Respect/safety regression checks and an auditable test record with date, version, input, expected/actual result, evidence URL, and pass/fail.
Critical gate failure blocks production-ready/VERIFIED status.

## 6. Product passport template
- Product name and ID/version
- Short description and intended use
- Instructions / inputs / outputs
- Demo video (MP4)
- VIP screenshot
- QR destination
- Dependencies and integrations
- Privacy/security notes and limitations
- Approved price/offer, if any
- Test evidence and date
- Known issues, changelog, feedback, rating, improvement status

## 7. Honest status labels
PLANNED = specified, not built.
BUILT = code/assets exist; tests may be pending.
TESTED = tests ran; results attached.
VERIFIED = acceptance criteria passed with evidence.
BLOCKED = required asset, authorization, integration, or evidence missing.

Do not claim 5,000 completed products or 150,000-scale capacity without inspectable inventory and load-test evidence.

## 8. Next implementation sequence
1. Inventory existing showroom pages and product assets.
2. Locate the canonical original photo and authorized voice asset; stop if missing.
3. Define a reusable product-card/passport schema and QR destination test.
4. Select one existing product and produce one real end-to-end sample with screenshot and demo.
5. Run and publish acceptance-test results.
6. Scale only after the sample passes.

## 9. Current status boundary
This document records approved requirements only. It does not prove that original photo/audio assets are available, a provider is connected, a product demo exists, QR destinations work, or the live system passed tests. Each requires separate evidence.
