# SHIRMANI RESEARCH INSTITUTE — Product Identity & Demo Publishing System

Status: **Specification created; deployment and product-by-product verification pending.**

## Purpose
Give every real tool/product its own identifiable, polished public showroom card. Never claim a product exists, works, or is independently verified until its implementation and tests support that claim.

## Product card artwork
Each product gets its own 16:9 landscape artwork (recommended 1600×900 source; responsive crop tested on mobile and desktop).

Required composition:
- Distinct product name, finalized only after checking for duplicates and misleading claims.
- Short plain-language description on the image (ideally 8–18 words).
- The supplied “निष्पक्ष समझ” portrait as a small, consistent logo, preserving the photo unchanged. Do not recreate, retouch, or synthesize the user's likeness.
- English identity line: “Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Love; Eternal, Real, Natural, Universal Truth, Present and Direct.”
- QR code in the upper-right corner, with clear margin and high contrast.
- QR points to a stable product passport/long-description page, not a fabricated URL. Test scan on common phones before publishing.
- Avoid overlap between portrait, product title, QR code, and key product imagery.

## Product passport (long description)
Each product passport should include:
1. Product ID and version
2. Product name and category
3. Problem it addresses and intended users
4. What it does / does not do
5. Supported inputs, outputs, languages, devices, and limitations
6. Step-by-step usage guide
7. Live demo or clearly labelled sample demo
8. Demo video URL and date checked
9. VIP screenshot / interface preview
10. Test cases, results, known issues, and evidence links
11. Version history, update/upgrade log, and changelog
12. Pricing, licence, refund/support terms, and purchase/enquiry link (only when configured)
13. Privacy, security, accessibility, and responsible-use notes
14. Customer feedback/rating, moderation, and improvement log

## Publication states
- DRAFT: incomplete, internal only
- PREVIEW: sample/mock-up; labelled “Preview — not a live product”
- DEMO: usable demo exists; limitations disclosed
- TESTED: defined tests passed with dated evidence
- VERIFIED: independent verification evidence is attached and reviewable
- AVAILABLE: purchase/enquiry route, price/terms, support contact, and fulfilment process are configured and tested

A workflow run or generated screenshot alone never qualifies a product as VERIFIED or AVAILABLE.

## Demo-video standard
Every published product must have a short demo video showing the task, actual interface, a real input and output, usage steps, limitations, and current version. Distinguish live functionality from simulated/mock content. Provide captions and a text transcript. Do not use synthetic endorsements or imply a real customer review without permission and evidence.

## Product registry schema
Use one record per product:
- product_id (stable unique ID)
- slug (unique)
- name
- category
- version
- status
- short_description
- long_description_url
- artwork_url
- logo_asset_url
- qr_target_url
- demo_video_url
- vip_screenshot_url
- usage_guide_url
- test_report_url
- price_and_currency
- licence_terms_url
- support_contact
- last_reviewed_at
- changelog_url

Missing values remain explicitly “Not configured”; do not fabricate them.

## Quality gates before public release
- [ ] Product name and slug are unique
- [ ] Image readable at mobile and desktop sizes
- [ ] Supplied portrait is used unchanged and with permission
- [ ] Identity line spelling reviewed
- [ ] QR scans and opens the correct passport
- [ ] Short description is understandable to a beginner
- [ ] Demo video shows real, accurately labelled behaviour
- [ ] VIP screenshot corresponds to the current version
- [ ] Usage guide and known limitations are present
- [ ] Price, licence, enquiry/purchase route and support are tested if selling
- [ ] Accessibility, privacy, security and link checks pass
- [ ] Evidence and review date are recorded

## Phased rollout
1. Audit current repository and identify genuinely implemented products.
2. Select one real product as the pilot; create its passport, artwork, QR target, demo, and screenshot.
3. Run the quality gates and publish the pilot.
4. Reuse the tested template for remaining products.
5. Add automated link, schema, image, QR-target, and evidence checks to CI.
6. Scale catalogue storage only after the pilot is reliable.

## Honest current status
This document defines the implementation contract. It does **not** prove that any product artwork has been updated, that QR codes or demo videos exist, that a live product is deployed, or that sales have occurred. Those require actual assets, working links, tests, and dated evidence.
