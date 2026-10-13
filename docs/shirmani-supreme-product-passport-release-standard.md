# SHIRMANI SUPREME — Product Passport, Visual & Demo Release Standard

**Status:** specification only; not proof of implementation or product readiness.

## Purpose
Every showroom product must be identifiable, understandable, testable, and honestly described. A product is not `VERIFIED` until its release gates have test evidence.

## Required product record
- `product_id`, `name`, `version`
- `status`: `DRAFT`, `IN_TEST`, `VERIFIED`, `SOURCE_BASED`, or `BLOCKED`
- `short_description`, `long_description_url`, `intended_use`, `limitations`
- `usage_guide_url`, `demo_video_url`, `vip_screenshot_url`, `test_report_url`
- `price` (amount/currency or `QUOTE_REQUIRED`), `support_contact` (verified or `NOT_CONFIGURED`)
- `last_verified_at`

## Original identity visual
1. Use the user's supplied “मेरी निष्पक्ष समझ” original photo unchanged; resizing only as needed. Do not generate a substitute face or alter facial features.
2. If the original photo is absent from repository/build assets, block publication with `BLOCKED_MISSING_ORIGINAL_IMAGE`; do not claim it was applied.
3. Place the photo/logo prominently at the top of every product visual.
4. Show this identity line beneath it: “Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh”.
5. Put product name, version, and a short plain-language description on the visual.
6. Put a QR code at upper-right. It must resolve to that product's own canonical long-form passport—not a generic homepage.
7. Keep the visual responsive, readable, and accessible with suitable alt text.

## Product-specific demo and screenshot
- Every product needs its own demo video showing the real workflow, inputs, outputs, and limitations.
- Every product needs its own VIP screenshot captured from the actual running product/version.
- Mockups, storyboards, and placeholders must be labelled and do not satisfy these gates.
- A dated test report must include product/version, environment, steps, expected and observed results, pass/fail, and evidence links.

## Release gates
Only mark `VERIFIED` when the product runs reproducibly, executable tests pass, screenshot and demo match the tested version, QR resolves to the correct passport, usage guide and limitations are present, and no critical security/privacy issue remains open. Record failures honestly. Workflow count alone is not product-quality evidence.

## Feedback loop
Tie consent-based customer feedback to product ID/version. Triage and reproduce issues, record fixes, rerun regression tests, and publish a dated changelog. Never fabricate reviews, ratings, sales, or usage metrics.

## Ethical outreach and commercial terms
Use verified official contacts and an authorised outbound channel. Log the source, purpose, date, and delivery result. A drafted email is not a sent email; delivery is not proof of a reply or sale. Respect opt-outs, law, and platform rules.
Before paid writing/research work begins, agree in writing on scope, deliverables, deadline, revisions, price, and payment terms.

## Current confirmed service scope
Hindi/English writing, research summaries, and website/blog content. Confirm topic, language, word limit, source links, deadline, budget, deliverables, and payment terms for each enquiry. This specification makes no revenue or customer-acquisition claim.

## Suggested acceptance tests
1. Metadata validator rejects missing product ID/version/description/passport/demo/screenshot/test report.
2. QR test confirms it encodes the canonical passport URL and the URL resolves successfully.
3. Asset test blocks publication when the approved original photo is unavailable.
4. Demo and screenshot records match product ID and version.
5. Release validator rejects `VERIFIED` if any required gate is missing or failed.
6. Pricing/outreach checks reject unapproved claims or unverified contact destinations.
7. Accessibility check verifies alt text, readable description, and responsive layout.

## Evidence boundary
This document defines requirements only. It does not prove any product, photo/voice integration, QR, demo, screenshot, live presentation, outreach, or revenue is already implemented or tested.
