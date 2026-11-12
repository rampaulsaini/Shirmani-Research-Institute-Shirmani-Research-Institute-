# SHIRMANI Product Identity, Demo & Passport Standard

**Status: SPECIFICATION / NOT YET PRODUCTION-VERIFIED**

## Purpose
Give each digital tool/product a distinct, honest, testable showroom identity. Never reuse another product's name, screenshot, demo, QR destination or claims.

## 1. Required product card
- Distinctive name + stable ID, version, release date and status (Concept / Prototype / Testable / Verified / Retired).
- Owner-authorized Shirmani identity photo/logo at upper-left. Preserve the supplied photo exactly; do not redraw, beautify, crop the face or synthesize a replacement without permission.
- English identity line beneath it: “Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Love; Eternal, Real, Natural, Universal Truth — Present and Direct.”
- QR at upper-right, generated only after a real product-passport URL exists and has been tested.
- Short, readable description on the image; full description, usage guide, limitations, sources, changelog and demo on the passport page.
- Product-specific VIP screenshot. Label illustrative artwork “Concept Preview”; never pass it off as a live screenshot.
- Product-specific MP4 demo showing purpose, setup, steps, expected output, limits and version/date.
- High contrast, accessible text, mobile-safe scaling and a 7% safe margin.

## 2. Image and video standards
- Main card: 16:9, 3840×2160 master where supported; responsive 1920×1080 and mobile crops.
- Keep photo/logo and QR clear of text overlays. QR should be at least 300×300 px in the 4K master.
- Test QR scanning from the published image and phone screen.
- Keep original assets separately; export PNG/WebP preview and MP4 thumbnail.
- Do not say “updated live” until the published page is checked.

## 3. Product passport schema
```json
{
  "schema_version": "1.0",
  "product_id": "SRI-WR-001",
  "name": "Shirmani ClearWrite",
  "category": "Writing & Research",
  "version": "0.1.0",
  "status": "prototype",
  "short_description": "Hindi/English writing and research support with scope agreed before work starts.",
  "intended_use": ["drafting", "editing", "research summaries", "website/blog content"],
  "inputs_required": ["customer goal", "topic", "language", "word limit", "deadline", "sources", "budget"],
  "deliverables": ["agreed writing/research output", "source list where applicable"],
  "limitations": ["No guaranteed sales, income, scientific truth, or third-party acceptance."],
  "demo_video_url": null,
  "vip_screenshot_url": null,
  "qr_destination_url": null,
  "test_report_url": null,
  "last_verified_at": null
}
```
Null URLs mean the asset does not yet exist. Do not generate a fake QR or claim a demo was recorded.

## 4. Four presentation tiers
1. **Clear Script** — text/script and branded card; no synthetic-voice claim.
2. **Voice Presenter** — authorized voice output after rights and pronunciation tests.
3. **Avatar Presenter** — authorized photo/avatar, facial animation and lip-sync; label synthetic presentation where appropriate.
4. **Live Interactive Presenter** — live Q&A only after latency, evidence, safety, voice, face and audit gates pass.

These are planned tiers, not proof that any provider integration is active. Use only authorized assets; do not clone a third party's face or voice.

## 5. Evidence and publishing gates
- **VERIFIED:** reproducible test plus evidence attached.
- **SOURCE-BASED:** source linked, but not independently reproduced.
- **CONCEPT PREVIEW:** illustrative visual, not a working product.
- **INSUFFICIENT EVIDENCE:** say “Not enough evidence is available yet.”
Keep philosophical/identity statements distinct from independently verified scientific claims.

Before publishing: check name/ID uniqueness within the catalogue; describe function and intended users plainly; confirm screenshot authenticity/label; play the MP4; scan the QR; review usage, limits and privacy notes; attach test results; check accessibility/mobile layout; record release URL and commit. Check trademark/domain conflicts before claiming a name is globally unique. Do not claim AI/ML teams finalized a name unless a review record exists.

## 6. First known offer
**Shirmani ClearWrite — Hindi/English Writing & Research**
Services: writing, research summaries, website/blog content.
Enquiry fields: customer goal, topic, language, word limit, deadline, sources/links, budget.
Workflow: confirm scope and price in writing → agree deliverables, deadline and payment terms → start after agreement → deliver → record acceptance and feedback.
No sale, customer contact, payment or income is claimed without an actual record.

## 7. Quality and income dashboard
For each product record: required assets complete/total; demo playability; QR scan success; passport completeness; test pass rate; accessibility checks; enquiries; quotes; accepted scopes; paid orders; refunds/complaints; feedback; verified revenue. Report only counts supported by actual records.

## 8. Rollout
1. Audit repository/catalogue first to avoid duplicate names or overwrites.
2. Catalogue existing products; preserve unknown fields as null.
3. Complete one pilot card + passport + MP4 demo before scaling to 5,000 products.
4. Test desktop/mobile and publish only after gates pass.
5. Scale in batches with evidence and rollback capability.

**Current blockers:** the exact owner-authorized photo and voice must be available to the implementation workspace. Real product URLs, screenshots and MP4 files must exist before final branded cards and QR codes can be published.
