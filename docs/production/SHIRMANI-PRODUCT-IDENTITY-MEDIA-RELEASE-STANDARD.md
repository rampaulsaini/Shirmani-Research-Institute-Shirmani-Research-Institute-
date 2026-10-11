# SHIRMANI Product Identity & Media Release Standard

Status: **Implementation specification — not a claim that every product asset is complete.**
Applies to every public-facing tool, digital product, service package, and showroom listing.

## 1. Product identity
Every product needs a stable product ID, approved English display name, one-sentence description, longer usage page, version, owner, and release status. Do not claim an AI/ML/NLP team finalized a name unless a recorded approval exists.

Suggested ID format: SRI-{CATEGORY}-{NNN}
- PRES: presentation and avatar tools
- WRITE: writing and research
- MEDIA: product media and demos
- THINK: explanation and research
- AUTO: automation and workflow tools

Name workflow: propose 3 concise names → check catalogue duplicates → check clarity and accessibility → human approval → record name, date, reviewer, and version. Names must describe real current capabilities, not aspirational capabilities.

## 2. Product cover layout
Use a responsive 16:9 cover (recommended source canvas 1920 × 1080; create a separate square crop only where required).
- Main area: product-specific title and a clear visual matching the real tool.
- Short description: one plain-language sentence, ideally 12–20 words.
- Photo/logo: use the owner's exact supplied photo unchanged as a small identity mark; do not redraw, beautify, recolour, or substitute it.
- Name line: use the owner's approved English rendering only after explicit approval.
- QR code: upper-right, high contrast, with a quiet zone and human-readable destination label. It must encode the stable public usage/demo URL, never a temporary or invented URL.
- Scaling: fit the full cover without clipping the photo, name, QR, title, or description. Test mobile and desktop views.

If the exact source photo is unavailable in the repository or current working session, mark the cover **PHOTO REQUIRED**. Do not substitute a generated face or claim the photo is identical.

## 3. Required product release bundle
Each product's release record should link to:
1. Product-specific cover image (SVG/PNG).
2. VIP screenshot captured from the real running tool (not a mock presented as a real screenshot).
3. Demo video (MP4) showing actual workflow, inputs, outputs, limitations, and version.
4. Plain-language usage guide with beginner steps and expert notes.
5. Product passport JSON: ID, name, version, owner, status, capabilities, limitations, dependencies, accessibility, security notes, demo URL, guide URL, support contact, and release date.
6. QR code pointing to the stable public demo/guide page.
7. Evidence checklist and test results.
8. Changelog and customer feedback/quality-improvement record.

A storyboard is not an MP4; a composition brief is not a screenshot; a generated cover is not proof that the tool works. Label each asset accurately.

## 4. Capability and evidence gates
- **DRAFT** — concept or incomplete.
- **BUILT** — runnable implementation exists.
- **TESTED** — specified tests passed, with dated evidence.
- **PUBLISHED** — public URL confirmed and release bundle available.
- **VERIFIED** — independent verification criteria met and evidence retained.

Do not mark a product VERIFIED from workflow completion, a generated file, or a successful build alone. A live integration is complete only after an authorised end-to-end test succeeds.

## 5. QR destination and privacy
The QR destination must be HTTPS, stable, and accessible without exposing private files or credentials. Do not encode personal contact details, secrets, access tokens, or non-public source material. Add a visible short URL label so customers can inspect the destination before scanning.

## 6. Demo-video minimum
1. Product name, version, and intended user.
2. The problem it solves.
3. Actual tool opening and input.
4. Actual output, with sensitive information removed.
5. How to use/save/export the result.
6. Evidence, known limitations, and support route.
7. Release status and version/date.

Only publish a demo when the displayed behaviour matches the current product build.

## 7. Release checklist
- [ ] Unique ID and approved distinct name
- [ ] Owner's exact photo supplied and used unchanged
- [ ] English name line approved
- [ ] Short description readable on cover
- [ ] Correct stable QR destination verified by scanning
- [ ] Cover tested at mobile and desktop sizes
- [ ] Real VIP screenshot captured
- [ ] Actual demo MP4 recorded and checked
- [ ] Usage guide and product passport published
- [ ] Accessibility, privacy, security, and limitations reviewed
- [ ] Test evidence and changelog retained
- [ ] Public listing links checked
- [ ] No unverified sales, customer, security, or capability claims

## 8. Current implementation boundary
This standard defines the required release process. It does **not** mean every catalogue item already has a real MP4, screenshot, QR, published guide, tested integration, or sale. Existing browser-local tools must be described as browser-local until server persistence, outbound messaging, payment processing, and production integrations are implemented and tested.
