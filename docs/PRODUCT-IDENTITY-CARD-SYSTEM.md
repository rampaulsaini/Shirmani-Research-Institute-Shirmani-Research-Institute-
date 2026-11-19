# Product Identity Card System — Implementation Specification

**Repository:** Shirmani Research Institute  
**Status:** UI prototype on a feature branch; not production-integrated or independently verified.  
**Branch:** `feature/product-identity-qr-demo-cards-2026-10-11`

## Required card identity
- Use the user's exact, unchanged portrait as the small brand mark on every product card, after the original image asset is supplied/confirmed. Never replace it with a generated face or retouched variant.
- English identity line: **SHIROMANI RAMPAL SAINI** with the user-requested identity statement represented as an identity/philosophical statement, not an independently verified scientific claim.
- Each product has its own unique product ID, finalized display name, hero image, concise on-image explanation, long-description page/QR, demo video, VIP screenshot, usage guide, and version/passport page.
- Responsive image scaling: product artwork uses a 16:10 frame and `object-fit: contain`; portrait logo uses `object-fit: cover`. Validate on mobile and desktop.
- QR destination must be a public product-detail URL. Do not encode secrets or private data. Prototype QR uses a third-party QR rendering service; production should preferably generate and host QR assets in the repository/build pipeline.

## Required evidence states
- `DRAFT`: incomplete metadata or media.
- `SOURCE-BASED`: sources are linked but independent verification is incomplete.
- `VERIFIED`: defined tests passed and evidence is attached.
- `INSUFFICIENT-EVIDENCE`: do not make a verification claim.
- `DEMO-MISSING` and `SCREENSHOT-MISSING` are visible gaps, not success.

## Product data contract
Every catalogue entry should contain:
`id`, `name`, `category`, `shortDescription`, `longDescriptionUrl`, `heroImage`, `brandPortrait`, `qrAsset`, `demoVideoUrl`, `vipScreenshotUrl`, `usageGuideUrl`, `passportUrl`, `version`, `evidenceState`, `testResults`, `lastUpdated`.

## Quality gates before a product is public
1. Unique ID and distinct product name approved.
2. Hero image and portrait logo paths resolve; no broken assets.
3. QR opens the correct long description.
4. Demo video and VIP screenshot load and match the product version.
5. Usage guide explains purpose, steps, limitations, and intended users in simple language.
6. Evidence state agrees with recorded tests; no invented review counts, customers, sales, or verification.
7. Mobile/desktop accessibility, readable text, contrast, and keyboard links pass.
8. Customer feedback enters a documented issue/quality-improvement loop.

## Scope and current limitation
This prototype demonstrates the card layout with one clearly marked sample only. It does **not** mean 5,000 products have been created, demoed, tested, or verified. No outbound company contact, sale, or income is claimed. Integration into the live homepage, product data migration, local QR generation, and media creation remain separate implementation tasks.
