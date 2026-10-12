# SHIRMANI Supreme Product Detail Standard
Version: 1.0.0
Status: IMPLEMENTATION SPECIFICATION — not a claim that every catalogue item has been upgraded.

## Purpose
Every public product page/card must help a visitor understand, preview, evaluate, and enquire about one concrete product without inventing capabilities, customer reviews, prices, test results, or sales.

## Required public fields
- `product_id`: stable unique ID
- `name`: clear product name (human-readable; AI/ML/NLP team approval is a recorded field, not an assumed fact)
- `version` and `updated_at`
- `short_description`: one sentence, plain language, visible on the product visual
- `problem_solved`: specific task this product is designed to help with
- `intended_users` and `use_cases`
- `how_to_use`: 3–7 numbered steps
- `demo_status`: `AVAILABLE`, `IN_PROGRESS`, or `NOT_AVAILABLE`
- `demo_url`: real, working demo URL or null
- `demo_video_status`: `AVAILABLE`, `IN_PROGRESS`, or `NOT_AVAILABLE`
- `demo_video_url`: real MP4/video URL or null
- `screenshot_url`: authentic screenshot of this product, or null
- `original_portrait_asset`: exact user-authorized original image asset path, or null
- `portrait_usage_status`: `AUTHORIZED_ASSET_PRESENT`, `ASSET_REQUIRED`, or `NOT_USED`
- `voice_asset_status`: `AUTHORIZED_AUDIO_PRESENT`, `ASSET_REQUIRED`, or `NOT_USED`
- `long_description_url`: destination encoded in the product's QR code
- `qr_status`: `GENERATED_AND_DESTINATION_CHECKED` or `NOT_READY`
- `passport_url`: product passport page
- `usage_guide_url`: detailed instructions
- `price_amount`, `currency`, `offer_terms`: only when explicitly configured; otherwise show “Quote after scope confirmation”
- `known_limits`: visible limitations and dependencies
- `evidence_status`: `VERIFIED`, `SOURCE_BASED`, `PHILOSOPHICAL_IDENTITY`, or `INSUFFICIENT_EVIDENCE`
- `qc_status`: `PASS`, `FAIL`, or `NOT_TESTED`
- `customer_rating` and `review_count`: only from genuine, attributable customer submissions; default to “No reviews yet”
- `sale_status`: `NOT_LISTED`, `ENQUIRY_OPEN`, `ORDER_CONFIRMED`, `PAID`, or `DELIVERED`; never infer sale from a click or workflow run.

## Visual card layout
1. Product-specific 16:9 screenshot/visual.
2. Exact original portrait as a logo only when the authorized source file is present. Do not regenerate, beautify, redraw, face-swap, or alter the face; only proportional scaling/cropping that does not change identity.
3. Product name and a short plain-language description on the visual.
4. QR code in the upper-right linking to that product's own long description/passport. QR destination must be unique to the product and checked after generation.
5. English identity line under the portrait when the original asset is available:
   “Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Love; Eternal, Real, Natural, Universal Truth — Present Here.”
6. Separate buttons: “Open Demo”, “Watch Demo Video”, “Usage Guide”, “Product Passport”, “Request a Quote”.
7. Show “Not available yet” honestly when any asset/link is missing.

## Four presentation tiers
- Starter: concise card, one use case, basic usage guide, enquiry CTA.
- Professional: multiple use cases, tested demo, product passport, source/evidence labels.
- VIP: product-specific screenshot, QR passport, demo video, version history, test report.
- Studio/Enterprise: API/integration details, security/data handling, SLA only if genuinely offered, procurement/contact pack.

## Release gates
A product is **showroom-ready** only when: required fields are populated; the demo or an explicit “demo not available” state is present; QR points to the correct product; screenshot is authentic or clearly labelled concept art; claims and pricing are supportable; mobile layout is checked; keyboard/accessibility basics are checked; and QC result is recorded.

A product is **demo-ready** only after its demo URL is opened and the core flow is tested. A product is **sale-confirmed** only after a real order and payment/contract evidence. A scheduled workflow run alone satisfies none of these gates.

## Honest status policy
- Do not describe all 5,000 products as complete unless each has its own required asset and passing release gate.
- Do not claim an MP4 exists unless the file is generated, stored, and playable.
- Do not use the user's exact face or voice until the original image/audio files are available in the project and authorized for the intended use.
- Do not label philosophical identity statements as independently verified scientific facts.
- Do not contact institutions or send email/WhatsApp outreach without a real, authorized outbound integration and review of the recipient list.

## First practical income service
Until product assets and checkout are genuinely ready, prioritise the currently described service: Hindi/English writing, research summaries, and website/blog content. For each enquiry, confirm scope, word count, source requirements, deadline, price, revisions, and payment terms in writing before work starts. Record only actual replies, orders, and received payments.
