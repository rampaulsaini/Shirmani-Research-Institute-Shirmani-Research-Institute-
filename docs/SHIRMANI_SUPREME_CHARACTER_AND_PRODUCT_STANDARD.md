# SHIRMANI SUPREME — Character & Product Presentation Standard

**Status:** Character description approved by user on 2026-10-12; specification recorded. Implementation and production tests are not yet verified.

## 1. Approved character description

The SHIRMANI SUPREME presenter communicates in simple, warm, calm, respectful language adapted to the audience and situation. It explains ideas from first principles, uses examples when helpful, distinguishes facts from interpretations, and never humiliates or stereotypes a person or community.

Required behaviours:
- Understand the question and context before answering.
- Explain simply first; add technical depth, equations, research, or examples when useful.
- Cite reliable sources for factual claims where available.
- Label statements **Verified**, **Source-based**, **Philosophical/identity**, or **Insufficient evidence**.
- When evidence is inadequate, say: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
- Correct mistakes openly; never invent capabilities, tests, endorsements, contacts, sales, or income.
- Treat the user's philosophical/identity statements as user-authored statements, not independently verified scientific findings.

## 2. Original photo and voice rules

- Use the user's original supplied photograph unchanged except proportional resizing or layout cropping. Do not regenerate, beautify, retouch, or alter facial features.
- Use only the user's supplied voice recording or an explicitly authorized voice integration.
- If the original photo/voice is unavailable in the working repository/session, mark it **NEEDED**; never substitute an invented asset.
- Do not claim voice cloning, lip-sync, or live presentation is operational until an end-to-end test passes.

## 3. Mandatory product showroom card

Each product needs its own unique identity and must not reuse another product's product-specific artwork or QR destination.

Required per product:
1. Unique product ID and finalized name.
2. Distinct product image/card.
3. Short, readable description printed on the image.
4. Original approved portrait as a small logo only if the original asset is available; resize only.
5. Product-specific QR code linking to that product's long description, version, limitations, usage guide, and evidence.
6. Real demo video, or a clearly marked **Demo pending** placeholder.
7. Usage guide and product passport/version history.
8. Test status, limitations, last-tested date, and evidence links.
9. Customer feedback and a documented improvement loop.
10. Price, licence, refund/support terms, and purchase/contact path only where actually configured.

Layout rules:
- Product name and short description must remain readable on mobile.
- Put the portrait/logo consistently without obscuring the product.
- Put the QR in the top-right when dimensions permit; preserve quiet-zone/margins.
- Test each QR and confirm it opens the matching product page before publication.
- Do not use unsupported claims or unverified performance figures.

## 4. Demo and quality loop

Define use case → build prototype → record a real demo → publish guide/passport → run acceptance tests → publish evidence/status → collect feedback → review changes → version and retest.

A demo must show the actual product or a clearly labelled prototype. Concept art is not a working demo. If no real video exists, show **Demo pending**.

## 5. Human-presentation pipeline

Voice input → authorized speech recognition → intent/context → reasoning → evidence gate → response → authorized voice output → original-photo presentation → lip-sync → audit.

This is the target architecture, not proof of integration. Each component must be separately tested before the complete pipeline is called production-ready.

## 6. Acceptance gates

- [ ] Original portrait verified; only proportional resizing/cropping applied.
- [ ] Voice source and authorization documented.
- [ ] Speech recognition and context tests pass.
- [ ] Q&A tests cover simple, ambiguous, and complex prompts.
- [ ] Evidence labels and insufficient-evidence response pass.
- [ ] Voice output and timing tests pass.
- [ ] Face/presentation and lip-sync tests pass with the approved asset.
- [ ] Mobile readability and accessibility checks pass.
- [ ] Every QR resolves to the correct product page.
- [ ] Every demo is genuine and matches the published version.
- [ ] No unsupported claims or fabricated sales/contact/test results.
- [ ] Audit record and version/rollback path exist.

A failed critical gate blocks a **VERIFIED** or **production-ready** label.

## 7. Status vocabulary

- **PLANNED:** described but not built.
- **IN PROGRESS:** implementation started.
- **BUILT — UNTESTED:** code/asset exists but acceptance tests have not passed.
- **TESTED:** a named test passed and evidence is linked.
- **VERIFIED:** all required gates passed with reviewable evidence.
- **BLOCKED / NEEDED:** an asset, permission, service, or dependency is missing.

## 8. Next steps

1. Inventory existing repository assets and showroom implementation.
2. Map existing products to unique IDs/pages; do not invent products or mark them complete without evidence.
3. Locate the original portrait and voice files; request re-upload if absent.
4. Implement the card template and product-specific QR destinations in the existing showroom stack.
5. Add automated link/QR and metadata checks.
6. Create a real demo for the currently available Hindi/English writing and research service before scaling the template.
7. Report links to commits, deployed pages, test output, and blockers.

## Integrity commitment

A repository file, workflow run, mockup, or planned integration is not proof of a working live service. Report only observed commits, deployed output, test results, verified QR destinations, and real customer activity. No sale, outreach, revenue, or independent verification may be claimed without evidence.
