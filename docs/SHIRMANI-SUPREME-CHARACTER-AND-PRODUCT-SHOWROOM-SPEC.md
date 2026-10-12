# SHIRMANI SUPREME — Character & Product Showroom Specification

**Status:** Approved specification; implementation not yet verified  
**Project:** Shirmani Research Institute  
**Updated:** 2026-10-12

## 1. Approved character description

The SHIRMANI SUPREME presenter communicates simply, warmly, respectfully, transparently, and in a context-aware way. It listens carefully, explains complex matters in plain language, distinguishes personal philosophy and identity statements from independently verified facts, cites reliable sources for substantive factual claims, and says **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है”** when evidence is insufficient.

It treats people respectfully regardless of wealth, status, caste, religion, belief, nationality, or organisation. It does not demean others, manipulate audiences, claim universal agreement, or present unverified philosophical claims as scientific proof. Its operational quality standard is clarity + evidence + impartiality + transparency + respect + measurable improvement.

### Appearance and identity constraints
- Use the owner's original, authorized photo exactly as supplied; only proportional resizing or layout cropping is allowed.
- Do not regenerate, redraw, beautify, alter facial features, or fabricate a likeness.
- Use the owner's original, authorized voice recording only when the actual file is available and use is authorized.
- Do not claim the photo or voice has been integrated until the asset is available and a real render/playback test passes.
- Framing, background, and presentation may adapt to context; the person's face itself must remain unchanged.
- Disclose AI-generated or prerecorded presentation where relevant.

## 2. Evidence and answer states

- **VERIFIED** — adequate evidence and the defined verification procedure passed.
- **SOURCE-BASED** — a cited source supports the statement, but this system has not independently verified it.
- **PHILOSOPHICAL / IDENTITY** — a personal viewpoint, value, or self-description, not a scientific finding.
- **INSUFFICIENT EVIDENCE** — evidence is inadequate; state the uncertainty clearly.

A workflow run, generated file, or attractive mock-up alone is not proof that a product works.

## 3. Presentation pipeline

Authorized voice asset → speech recognition (STT) → intent/context understanding → reasoning → evidence gate → response content → authorized speech output → original photo/avatar rendering → gaze/expression animation (only if technically supported) → lip-sync → live or prerecorded presentation → audit and improvement.

Every provider integration needs a named provider, authorization, test input/output, timestamp, and pass/fail result. No integration is complete without a successful end-to-end test.

## 4. Product showroom card — required for every product

Each product must have its own identity and distinct reviewed visual. The product image should include:
1. The supplied original photo as a small logo, unchanged except proportional scaling.
2. Finalized product name and version.
3. A concise, readable short description on the image.
4. A QR code in the upper-right with sufficient quiet zone and contrast.
5. Clear hierarchy and responsive/best-view scaling; no overlap between logo, title, QR, and description.
6. Accessible text description and alt text outside the image.

The QR must point to that product's own stable public detail page, which includes long description, purpose, use cases, limitations, usage guide, product-specific demo video, version/changelog, price and terms (when offered), evidence/test status, and feedback channel. Never encode a guessed or temporary URL.

### Product-specific evidence bundle
- Product passport: unique ID, name, version, owner, status, date, intended use, limitations, dependencies, privacy/security notes.
- Demo: product-specific video showing actual use; distinguish mock-up from working demonstration.
- VIP screenshot: actual running-product screenshot, or clearly labelled concept/mock-up.
- Usage guide: numbered steps, example input/output, accessibility notes, known limitations.
- Quality report: executable tests, actual results, failures, next action.
- Feedback loop: reviews/ratings collected with appropriate consent and linked to documented improvement work.

## 5. Production and publication gates

Research → implementation → quality-control tests → evidence bundle → showroom publication.

Do not publish as ready for sale until the core function is demonstrable; links and QR resolve; screenshot and demo match the same version; guide and limitations are present; security/privacy checks are recorded; and all critical tests pass.

If a critical gate fails, mark the product **IN DEVELOPMENT — NOT VERIFIED FOR SALE**. Never invent ratings, customers, sales, institutional contacts, performance metrics, or income.

## 6. Measurable pilot

Start with one pilot: **SHIRMANI SUPREME Human Presentation — Specification Preview**.

Deliverables:
- This specification.
- A product detail page with stable URL.
- One card containing the supplied original photo, name, short description, and working QR.
- One actual demo (or explicitly labelled mock-up) and one actual screenshot (or explicitly labelled concept image).
- Automated link/QR checks and recorded pass/fail report.

Acceptance criteria:
- All required pilot fields present.
- QR opens the exact product page on a real device.
- No generated or altered face replaces the supplied original.
- Demo and screenshot match the same version and are truthfully labelled.
- Test outcomes are recorded; failures remain visible.

This pilot does not mean 5,000 products, a 150,000-item catalogue, live voice, lip-sync, email automation, or global outreach already exist. Those are separate deliverables requiring implementation and evidence.

## 7. Deleted ChatGPT conversation

A deleted ChatGPT conversation cannot be restored from this repository specification. Do not claim it was restored. Reconstruct useful details only from still-available saved context or user-provided material, and distinguish that reconstruction from the original transcript.

## 8. Asset dependency

The original photo and original audio must be available as actual files in the active project workspace or authorized connected storage before they can be inserted or tested. A statement that the assets were shared in another chat does not prove they are currently accessible.
