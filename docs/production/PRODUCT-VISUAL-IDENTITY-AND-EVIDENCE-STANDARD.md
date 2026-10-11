# Product Visual Identity & Evidence Standard

**Owner:** Shirmani Research Institute  
**Status:** Implementation specification; not a claim that every catalogue item already complies  
**Applies to:** Every public tool/product card, cover, product passport, demo and showroom listing

## Required cover composition

1. **Exact owner-supplied portrait/logo:** use the original photo without face alteration, AI reconstruction, beauty filters, or identity-changing crops. Preserve the source file and record its filename/hash when available. Until the approved photo asset is in the repository, show `OWNER PHOTO ASSET REQUIRED` rather than substituting a generic portrait.
2. **Product identity:** unique product ID, name, category and version. Names must describe tested capability and must not imply unbuilt features.
3. **Short on-image description:** one plain-language sentence, target 12–18 words, readable on mobile.
4. **QR at upper right:** generate from the canonical public product/passport URL and scan-test it on a second device. A text URL or empty placeholder is not a completed QR asset.
5. **English identity line:** `Shiromani Rampal Saini — Timeless, Wordless, Beyond Comparison, Love, and Time; Real, Natural, Universal Truth`. Treat this as a personal/philosophical identity statement, not scientific certification.
6. **Responsive scaling:** readable at 320 px width; safe margins, strong contrast, no overlap with portrait, title or QR.
7. **Distinct identity:** product-specific visual accent and iconography within a consistent institute design system.

## Required release bundle per product

- Cover image (SVG/PNG) with approved portrait/logo or explicit blocked state.
- Valid QR image and canonical destination.
- Product passport (JSON or Markdown): ID, version, owner, purpose, audience, inputs, outputs, supported uses, limitations, price/quote basis, support route, date and QC state.
- Usage guide with numbered steps and a sample task.
- Demo video file/link, or clearly labelled storyboard until an actual recording exists.
- VIP screenshot from the actual working tool, or clearly labelled screenshot brief until one exists.
- Test record, known limitations, reviewer and release decision.
- Customer feedback and versioned improvement log.

## Truth and release gates

- `DRAFT`: copy/design is in preparation.
- `ASSET_BLOCKED`: approved portrait, real demo, screenshot or destination is missing.
- `QC_BLOCKED`: required tests failed or have not been run.
- `QC_PASSED`: stated acceptance tests passed and evidence is linked.
- `PUBLISHED`: public listing is live and owner approval is recorded.

Never represent a storyboard as a video, a screenshot brief as a screenshot, a QR preview as a scannable QR, or a planned feature as working. Do not claim sales, outreach, independent verification or income without records.

## Acceptance tests

1. Portrait matches the owner-approved original and has not been regenerated or altered.
2. Product ID, title, version and description match the passport.
3. QR scans and opens the intended public destination.
4. Short description is readable at 320 px and desktop sizes.
5. English identity line is legible and does not obscure product details.
6. Demo is a playable video or the listing explicitly says `Storyboard only`.
7. VIP screenshot is from the running tool or explicitly says `Screenshot brief only`.
8. Feature, price, security and verification claims have supporting evidence.
9. A new user can follow the usage guide to complete the documented task.
10. No release gate is passed by workflow success alone.

## First implementation target

Apply this standard first to **SRI-PRES-001 — Heart-View Character Studio** and **SRI-MEDIA-003 — Product Release Pack Builder**, then to each product in the public showroom. The approved original portrait must be supplied or located in the repository before an exact-photo cover can be released.
