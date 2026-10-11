# Product Media Quality Gate — 2026-10-11

## Purpose
Make every public product listing visually distinct, understandable before purchase, and honest about what is implemented. This is an implementation specification and release checklist; it is not proof that every product already has finished media.

## Public product-card standard
Every product card should include:
1. **Unique identity:** approved product name, stable product ID, category, version, and readiness state.
2. **Product-specific cover image:** preferably 3840×2160 (16:9) source artwork, with responsive crops and a legible 1280×720 minimum web rendition. Use a unique composition tied to the product's actual purpose.
3. **Institute mark:** use the approved “निष्पक्ष समझ” logo asset in a consistent, non-obstructive position. Do not invent a personal photograph or imply endorsement from an image that was not supplied/authorized.
4. **English identity line where requested:** use only an approved spelling/wording record; preserve the user's chosen wording and do not turn personal/philosophical identity statements into independently verified scientific claims.
5. **Short on-image description:** one plain-language sentence that states what the product actually does. Keep text inside safe margins and readable on mobile.
6. **QR code:** generated from the canonical product detail URL or a stable institute-owned redirect. The QR must be machine-readable, tested after export, and never a decorative or placeholder pattern.
7. **Demo media:** product-specific demo video or, until rendered, a clearly labelled storyboard/preview. Never label a storyboard as an MP4 or a planned demo as live.
8. **VIP screenshot:** a real screenshot captured from the actual running product, with viewport/device context. A mock-up must be labelled “concept preview.”
9. **Long description:** separate accessible detail page containing purpose, use cases, limitations, requirements, version history, price/quote terms, support and evidence links.
10. **Usage guide and passport:** steps, inputs/outputs, known limitations, version, owner, date, media URLs and test status.

## Product release state machine
Use these states consistently across the factory board and public showroom:
- DISCOVERED — product idea recorded; no implementation claim.
- BUILDING — implementation is in progress.
- DEMO_READY — the actual runnable demo works; evidence is linked.
- MEDIA_PENDING — product may work but required image, real screenshot, QR validation, or demo video is missing.
- QC_PENDING — product and media are assembled; acceptance tests are not complete.
- PUBLISHED — all required release gates passed and public links resolve.
- MAINTENANCE — published product has a known issue or update in progress.
- RETIRED — no longer offered; retain a clear status page where practical.

A product must not become PUBLISHED solely because its card or generated cover exists.

## Media acceptance gates
Record pass/fail and evidence URL for each gate:
- G1_IDENTITY: ID, title, version and category are unique and consistent.
- G2_IMAGE: product-specific image loads, has alt text, scales responsively and has no clipped text.
- G3_LOGO: approved institute logo is used without obscuring product details.
- G4_COPY: short description accurately matches the running product.
- G5_QR: QR decodes to the canonical detail page on at least two independent readers; destination returns successfully.
- G6_SCREENSHOT: screenshot comes from the running product or is explicitly marked concept preview.
- G7_DEMO: playable product-specific MP4 is available, or listing clearly says “demo video pending” and remains unreleased.
- G8_GUIDE: usage guide covers prerequisites, steps, outputs and limitations.
- G9_PASSPORT: machine-readable product passport matches the public listing.
- G10_ACCESSIBILITY: contrast, text alternatives, keyboard navigation and mobile layout are checked.
- G11_SECURITY: no exposed credentials, unsafe embedded content or unreviewed external script is introduced.
- G12_EVIDENCE: test log, build/run result and reviewer/date are recorded.

Critical failure in G1, G2, G4, G5, G7, G9 or G11 blocks PUBLISHED. If MP4 is not yet rendered, keep the product in a pre-publication state unless the listing is explicitly an early-access offer and says so.

## Product passport fields
Recommended JSON fields:
- product_id
- name
- version
- category
- readiness
- summary
- detail_url
- cover_image_url
- logo_asset_url
- qr_destination_url
- demo_video_url
- screenshot_url
- usage_guide_url
- limitations
- price_or_quote_policy
- gates (each with status, evidence_url, checked_at, reviewer)
- updated_at

Use null for missing media rather than fake URLs or invented evidence. Keep private/customer data out of public passports.

## Demo video minimum
A product-specific demo should show, in order:
1. Product name, ID and current version.
2. The real interface and intended user.
3. One representative input or task.
4. The actual output/result, including failure or uncertainty where relevant.
5. Where and how to use it; prerequisites and limitations.
6. A clear call to action that leads to the product's own detail/enquiry page.

The storyboard is not a rendered video. Mark the media status STORYBOARD_ONLY until an actual playable file is uploaded and checked.

## Metrics for the production board
Track counts from actual catalogue records, not targets presented as achievements:
- total registered products;
- products with unique cover images;
- products with validated QR codes;
- products with real screenshots;
- products with playable demo videos;
- products with complete passports and usage guides;
- products passing all critical gates;
- broken media/detail links;
- customer feedback items reviewed;
- issues fixed and re-tested.

For every metric show numerator, denominator, measurement timestamp and query/source. Do not claim “5,000 products complete” or “100% quality” without a reproducible inventory and gate evidence.

## Safe customer feedback loop
Review received → privacy/moderation check → issue classified → reproducible test → fix → regression test → release note.
Do not publish private customer information without permission. Ratings are customer opinions, not scientific verification. Never fabricate testimonials, reviews, client logos or purchase counts.

## Immediate execution order
1. Audit existing catalogue records and current media links.
2. Reuse existing showroom/product-media tools; avoid parallel duplicate dashboards.
3. Generate or source product-specific artwork only after the product's actual purpose is confirmed.
4. Produce a real screenshot from the running demo.
5. Generate and independently decode the QR from the canonical detail URL.
6. Record a real MP4 demo, or leave demo_video_url null and mark video pending.
7. Run all gates and publish only products that pass.
8. Add outreach or payment integration only as separate, authorized work with logged results.

## Acceptance criteria for this specification
- A maintainer can tell real media from a concept preview.
- A listing cannot be marked fully published while critical evidence is missing.
- Missing media is visible as pending, not silently treated as complete.
- Product identity, QR destination, passport and listing remain consistent.
- Production metrics can be reproduced from records.
- No claim of external outreach, sales, revenue, independent verification or production readiness is made without supporting evidence.
