# Shirmani Product Identity, Visual & Demo Standard

Status: **Specification draft — not a production deployment**
Owner approval: required before public release.
Source of truth: each product's verified record and approved assets.

## 1. Non-negotiable visual layout

Every product gets its own independently identifiable product card/poster, responsive and legible on mobile and desktop.

- **Top-left:** the owner's exact, authorized portrait as a small logo. Do not recreate, retouch into a different identity, or substitute a generated face. The approved original image file must be supplied/located before final rendering.
- **Top-right:** a QR code that resolves to that product's own canonical long-description page. Never use a decorative or untested QR. Validate the decoded destination and HTTP response before release.
- **Main area:** product-specific visual, not a repeated generic image.
- **Product title:** a distinct, readable finalized name.
- **Short description:** printed directly on the image; plain language, accurate and concise.
- **Owner line beneath the portrait/logo:** “Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Love; Eternal, Real, Natural, Universal Truth — Present Here.”
- **Footer:** version, product ID, status label (Prototype / Tested / Verified), and a clear demo or details URL where space permits.
- **Scaling:** preserve aspect ratio; no cropped face, clipped title, QR, or essential copy. Export a high-resolution master and responsive web renditions.

## 2. Product identity record

Each published product must have:
- stable product ID and unique product name;
- category, version, release date and status;
- problem solved, intended user, supported use cases and limitations;
- setup/how-to guide, accessibility notes and support/contact route;
- canonical long-description URL and tested QR destination;
- source/rights record for every image, voice, font, music and demo asset;
- changelog and last-reviewed date.

Never describe a product as unique, independently verified, secure, or superior by a quantified amount without evidence that supports that exact claim.

## 3. Required product asset pack

For each product, track these deliverables separately:
1. Product visual/poster (master + responsive export).
2. VIP screenshot captured from the real running product.
3. Product-specific demo video showing real steps and outputs.
4. Usage guide and limitations.
5. Product passport (identity, version, dependencies, rights, evidence, support).
6. QR destination and scan test.
7. Accessibility and mobile/desktop visual checks.
8. Review/rating intake and a documented improvement loop.

A screenshot or demo must show the real product. Do not fabricate a UI, result, customer review, rating, test outcome, or sale.

## 4. Evidence and release gates

Use one of these statuses:
- **DRAFT:** assets or documentation incomplete.
- **PROTOTYPE:** concept/UI exists but not all end-to-end tests pass.
- **TESTED:** named test suite ran and results are recorded.
- **VERIFIED:** the stated acceptance criteria passed with traceable evidence and an independent review where claimed.

Required checks before VERIFIED:
- QR scan opens the correct canonical product page.
- Text is legible at mobile and desktop sizes.
- Image has no overlap, clipping or distorted aspect ratio.
- Portrait and voice use is authorized and the source asset is preserved.
- Demo matches the actual product version.
- Usage instructions have been tested by a reviewer.
- Claims are linked to evidence; unsupported claims are removed or labelled as aspirations.
- No secrets, personal data, or unlicensed media appear in public assets.

## 5. Accessibility and plain-language rules

Write the short description so a beginner can understand it in one reading. Provide longer explanations, examples, use cases, limitations and technical detail on the QR destination. Use descriptive alt text, sufficient contrast, readable type, captions/subtitles for video, and keyboard-accessible links.

## 6. Metrics dashboard

Report actual counts only, never assumed completion:
- catalogue records total;
- products with approved portrait/logo;
- products with poster;
- products with valid QR;
- products with real demo video;
- products with VIP screenshot;
- products with tested usage guide;
- products passing all release gates;
- failed checks and blockers.

Completion percentage = passed deliverables / required deliverables × 100. Keep **prepared**, **tested**, and **independently verified** counts separate.

## 7. Automation chain

Product record → approved assets → poster generation → QR generation → QR validation → visual/accessibility tests → demo capture → usage-guide review → evidence bundle → human release approval → publish → review intake → versioned improvement.

Automation must stop and flag a human review when the portrait source is missing, rights are unclear, a QR fails, evidence is absent, or a public claim cannot be substantiated.

## 8. Current known blockers

- The exact approved portrait image must be available as a source asset in the repository or supplied for this session before it can be placed in final product artwork.
- Existing product catalogue and runtime UI must be audited to identify real products and current assets.
- No product is marked VERIFIED by this specification alone.
- No sale, external outreach, live integration, demo recording, or revenue is claimed by creating this document.

## 9. Acceptance criteria for the first product

The first product is ready for public review only when its distinct name, approved portrait, product-specific artwork, validated QR, real screenshot, real demo, tested guide, passport, rights record, and test report are all linked from one canonical product page.
