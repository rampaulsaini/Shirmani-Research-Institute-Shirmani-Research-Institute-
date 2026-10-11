# Product Media Release Gates — 2026-10-11

## First target
**SRI-PRES-001 — Heart-View Character Studio**

Repository references:
- Tool: `showroom/heart-view-character-studio.html`
- Existing cover asset: `assets/products/SRI-PRES-001-heart-view-character-studio.svg`
- Passport/spec: `docs/products/SRI-PRES-001-product-passport.md`
- Character spec: `docs/production/HEART-VIEW-CHARACTER-SPEC.md`
- Product release pack builder: `showroom/product-release-pack-builder.html`
- Public catalogue: `showroom/public-product-showroom.html`

## Release rule
A product is **not production-complete** merely because a page, cover, storyboard, QR destination, or workflow exists. Use the following per-product states:
- `NOT_CREATED`: artifact does not exist yet.
- `DRAFT`: generated but not reviewed.
- `QC_FAILED`: one or more critical gates failed.
- `READY_FOR_REVIEW`: all required artifacts exist and automated checks pass.
- `PUBLISHED`: a human approved the exact version and the public page points to it.
- `LIVE_VERIFIED`: only when a real end-to-end test record supports the claim.

## Required media pack
For each product, record:
1. Stable product ID and canonical showroom URL.
2. Product-specific cover image (target 3840×2160 source; responsive display; no stretched aspect ratio).
3. Short, legible on-image description and product name.
4. Institute/Impartial Understanding logo mark at the top. Use an approved supplied logo; if unavailable, label any temporary mark as a draft rather than inventing an official logo.
5. English identity line below the product: “Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Attachment; Eternal, Real, Natural Truth, Present and Direct.” Mark it as the owner's chosen identity wording, not independent scientific proof.
6. A real QR code that resolves to the product passport/long description. Scan-test the encoded URL on mobile before publication; never publish a decorative fake QR.
7. A real demo video (MP4 or hosted video URL), or an explicitly labelled storyboard while video is not yet recorded.
8. A real VIP/product screenshot, or an explicitly labelled screenshot brief while no screenshot exists.
9. Usage guide, supported inputs/outputs, limitations, price/quote basis, enquiry/order path, and version number.
10. QC record, test date, reviewer, defects, and customer feedback/improvement history.

## First product acceptance tests
- Cover matches the actual product, not a generic unrelated illustration.
- All text remains readable at phone width and at 200% zoom.
- QR decodes to the correct stable passport URL and the destination loads without login.
- Demo is labelled accurately: recorded demo versus storyboard.
- Screenshot is labelled accurately: captured screenshot versus composition brief.
- Product page clearly states this is a browser-local brief/checklist generator; it is not an integrated live avatar, voice-cloning, lip-sync, or MP4-rendering service unless those integrations are implemented and end-to-end tested.
- No fabricated ratings, customer reviews, sales, income, partner integrations, or verification claims.
- Feedback can be tied to a product ID/version and converted into a tracked improvement item.

## Catalogue rollout
Do not mark all 5,000 products complete until each product has the required artifacts and passing gates. Track counts separately:
- catalogued
- tool executable
- cover reviewed
- QR scan-tested
- demo video recorded
- screenshot captured
- usage guide complete
- QC passed
- published
- live end-to-end verified

The 150,000-scale directory should use stable IDs, paginated/sharded data, schema validation, and incremental loading; do not load or claim to have verified the entire catalogue from one browser page.

## Immediate next execution sequence
1. Review and improve the existing SRI-PRES-001 cover rather than create duplicate identity assets.
2. Verify its passport URL and build/scan-test a genuine QR.
3. Capture a screenshot from the running tool.
4. Record a truthful demo; until then, show the storyboard with a visible “Storyboard — video not recorded” label.
5. Run mobile/desktop accessibility and link checks.
6. Update the public showroom only with real artifact URLs and their actual statuses.
7. Repeat per product; do not bulk-mark products as complete.

## Security and privacy
- Use only portrait, voice, and likeness assets with documented authorisation.
- Keep API keys and provider secrets out of browser code and repository content.
- Require human approval for external outreach, public releases, payments, and irreversible actions.
- Keep personal data collection minimal; never infer emotion, identity, caste, religion, or trustworthiness from gaze/face.
