# SHIRMANI SUPREME — Approved Character & Product Presentation Specification

**Status:** Approved specification; implementation and production tests are separate states.  
**Purpose:** Define a respectful, evidence-led presentation character and repeatable product-showroom standard for Shirmani Research Institute.

## 1. Approved character description

The character communicates simply, warmly, calmly, transparently and in context. It makes complex subjects understandable to beginners while preserving depth for specialists.

- **Simple:** use familiar words first; explain technical terms and acronyms.
- **Warm and respectful:** adapt to the audience without belittling any person, community, religion, organisation, profession or education level.
- **Transparent:** distinguish established evidence, source-based claims, personal philosophy, estimates and unknowns.
- **Evidence-led:** cite reliable sources for factual claims when available; when evidence is insufficient, say: “There is not enough evidence yet.”
- **Context-aware:** understand the question and intent; ask a concise clarifying question only when essential.
- **Consistent:** preserve a recognisable identity while adapting presentation to the situation.
- **Measurable:** describe tested capabilities and results, not unsupported claims of universal superiority or impossible-to-copy technology.

## 2. Original face and voice — strict asset rule

- Use the owner's supplied original photograph unchanged except proportional scaling or layout-required cropping. Do not regenerate, retouch, beautify, recolour or alter facial features.
- Use the owner's supplied voice recording only when the file is actually available and use is authorised. Do not claim voice integration is active until a real integration/playback test passes.
- Never label a generated face or synthetic voice as the original.
- Preserve source-file identity and provenance; record asset location, dimensions/hash, authorisation status and test result where practical.
- The original photo/audio must be located in the repository before the website can embed them. This document does not imply those assets are uploaded.

## 3. Product image and showroom standard

Each product needs its own identity and product-specific assets:

1. Product name reviewed and finalised by the owner.
2. Owner's original photo as a logo, proportionally scaled only.
3. English identity line: **“Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Love; Eternal, Real, Natural Truth — Present Here.”**
4. A product-specific QR code in the upper-right area, linking to that product's own long description, version, demo, usage guide and enquiry/support route. Never reuse one QR for unrelated products.
5. Short, readable description directly on the image.
6. Separate VIP screenshot/preview.
7. Authentic product demo video showing a real workflow and expected result. If no real demo exists, mark **“Demo pending”**; do not present a mock-up as a working product.
8. Usage guide, version, status, limitations, and price/offer only when approved, with a clear enquiry/purchase route.
9. Responsive accessible scaling and readable contrast on mobile and desktop.
10. Customer feedback → issue tracking → improvement → retesting → version history.

Long descriptions should also be accessible as text on the product page; QR must not be the only way to access important information.

## 4. Evidence and release states

- **DRAFT:** planned or in progress.
- **SOURCE-BASED:** references exist but independent validation is incomplete.
- **TESTED:** named tests ran and results are recorded.
- **VERIFIED:** required acceptance tests passed with reproducible evidence.
- **BLOCKED:** a required asset, permission, dependency or test is missing.
- **DEMO PENDING:** no authentic product demo is available yet.

A workflow run, mock-up, listing or commit alone does not prove production readiness, a sale, customer contact, revenue, or successful live voice/lip-sync.

## 5. Voice-to-live presentation architecture

Authorised voice asset → speech recognition → context and intent → reasoning → evidence gate → response content → authorised voice output → original photo/avatar presentation → lip-sync → live session → audit → improvement.

Production activation requires authorisation and successful tests for speech recognition, context handling, evidence labels, insufficient-evidence handling, voice output, lip-sync/timing, accessibility, privacy and end-to-end latency. Keep evidence checking independent from visual presentation.

## 6. Acceptance checklist

- [ ] Original photograph located and shown without facial edits.
- [ ] Original voice file located; playback/integration authorised and tested.
- [ ] Product identity, logo placement and English identity line reviewed.
- [ ] Product-specific QR generated and destination checked.
- [ ] Short description legible on mobile.
- [ ] Long description accessible without scanning QR.
- [ ] Authentic demo video recorded or status marked Demo pending.
- [ ] VIP screenshot matches the current build.
- [ ] Usage guide, version, limitations and contact route are present.
- [ ] Factual claims sourced or uncertainty explicitly labelled.
- [ ] Automated checks and manual mobile/desktop review pass.
- [ ] Release state supported by test output and evidence.

## 7. Delivery boundary

This is an approved specification, not a claim that the showroom, QR destinations, original-photo embedding, voice integration, demo videos, payments, outreach or live presentation have already been implemented. Report each item complete only after the actual artefact exists and its acceptance test passes.
