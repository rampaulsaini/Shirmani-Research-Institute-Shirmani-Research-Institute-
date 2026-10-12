# ꙰ SHIRMANI SUPREME — Product Identity & Showroom Standard
**Revision:** 2026-10-12  
**Status:** Specification and release checklist; not proof that product assets or integrations already exist.

## Purpose
Give every Shirmani Research Institute tool a distinct, understandable identity. Product pages must be attractive, mobile-readable, accessible, and truthful about what is built and tested.

## Product card requirements
1. **Unique product name and catalogue ID.**
2. **Original portrait mark:** use only the user's supplied/authorized original Nishpaksh Samajh portrait. Do not redraw, stylize, AI-recreate, or alter the face. Scaling and non-distorting crop/placement are allowed.
3. **Short description on the card image:** one plain-language sentence explaining what it does and who it helps; use strong contrast and mobile-safe margins.
4. **QR code at upper-right:** encode the canonical public product-passport URL. Never guess a URL. Test the QR with a phone camera before release.
5. **VIP screenshot:** use a real screenshot of the working product UI. Label a concept/mock-up explicitly; never pass it off as a real screenshot.
6. **Product-specific demo video:** show the actual workflow and result. If missing, display “Demo pending” and do not mark the product published.
7. **Actions:** “Open demo”, “Read full details”, and “Request / buy” only when the destination and process work.

## QR-linked product passport
Each passport records:
- Product ID, name, version, release state, and updated date.
- Purpose, intended users, use cases, and step-by-step instructions.
- Implemented capabilities and explicit limitations.
- Real screenshots and demo link, or a clear pending state.
- Requirements, privacy/security notes, support route, pricing, and licence.
- Acceptance tests, test date/results, known issues, and change history.
- Feedback/rating form only when a functioning collection process exists.

## Release states
- **DISCOVERY:** idea/research only.
- **BUILD:** implementation underway; not production-ready.
- **QC:** candidate under test; limitations visible.
- **PUBLISHED:** mandatory assets, canonical passport, demo, accessibility checks, and acceptance tests all pass.

A workflow run, generated mock-up, or written specification is not proof of a working product.

## Demo video standard
Every published demo shows the actual product/version, a simple input, real steps, actual output, one limitation, and a link to instructions/support. Track status as **RECORDED**, **PENDING**, or **FAILED**.

## Original photo and voice safeguards
Use only the user's supplied and authorized portrait/audio. Do not reconstruct a missing photo from memory or substitute a similar face. Do not claim voice cloning, provider integration, or lip-sync is active until an authorized integration passes an end-to-end test. Do not publish private source media without approval.

## Pre-publication quality gates
- [ ] Unique product name and ID.
- [ ] Accurate short description; no unsupported superiority claims.
- [ ] Original portrait asset verified and face unchanged.
- [ ] Responsive card image, no distortion, legible on mobile.
- [ ] QR opens the correct canonical passport and scans successfully.
- [ ] Screenshot is genuine or labelled concept.
- [ ] Product-specific demo matches the current version, or remains visibly pending and unpublished.
- [ ] Pricing, request/purchase action, and support route are tested.
- [ ] Keyboard navigation, contrast, alt text, and error states checked.
- [ ] Release state and evidence recorded.

## Measurable progress
Report observed counts only: catalogue entries with unique IDs; verified portrait assets; working passports/QR scans; recorded product-specific demos; real screenshots; products passing mobile/accessibility checks; published products passing every gate. Count enquiries, paid orders, and revenue only from real recorded events.

## Implementation order
1. Audit the existing catalogue; do not invent missing product records.
2. Select one existing product as the pilot and confirm its canonical URL.
3. Build one complete card and passport using real assets.
4. Test QR, mobile layout, links, and demo end-to-end.
5. Review the pilot before applying the pattern to other products.
6. Produce cards and demos in batches only after each product's working state is verified.

**Completion rule:** a product is complete only when its mandatory evidence and tests are recorded—not merely because a specification exists.
