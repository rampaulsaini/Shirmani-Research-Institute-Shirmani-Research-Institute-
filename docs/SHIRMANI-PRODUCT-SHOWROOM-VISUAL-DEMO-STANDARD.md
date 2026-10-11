# SHIRMANI Product Showroom: Visual, QR, Demo and Verification Standard

**Status:** Specification only. This file does not claim that product images, QR destinations, demo videos, screenshots, or deployment are already complete.

## Per-product visual identity
- Every real product/tool has its own stable product ID, distinct name, version, and recognizable visual identity.
- Use the owner's exact supplied photo as the logo, without AI-redrawing, face replacement, or unapproved alteration. Preserve the original asset.
- Identity line under the logo: “Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Love; Eternal, Real, Natural, Universal Truth — Present and Direct.”
- Put a QR code in the upper-right with a proper quiet zone and strong contrast. It must point to that product's real, published HTTPS detail page; never use a placeholder or untested link.
- Put a short, legible description on the image. Put full description, use cases, limitations, setup, version history, and evidence on the QR landing page.
- Include a VIP screenshot from the actual UI. If it is only a mockup, label it “Concept Preview”.
- Include a product-specific MP4 demo showing real input, operation, output, use case, and limitations. Until checked, status is “Demo pending”.
- Export a 1600×1000 master plus responsive web sizes; maintain safe margins, readable text, high contrast, accessible alt text, and never stretch or cover the face/QR.

## Product passport fields
product_id; name; category; version; status; short_description; full_description; intended_users; use_cases; limitations; image_url; owner_logo_asset; vip_screenshot_url; demo_video_url; qr_target_url; documentation_url; pricing/currency; purchase_url; test_status; last_tested_at; evidence_links; changelog; accessibility_alt; authorization status for voice/face/likeness.

## Required release gates
A product is READY only after:
1. Its HTTPS detail page is publicly reachable.
2. QR scans to the correct page on at least two phone scanners.
3. Image layout is legible on mobile and desktop and uses the approved original photo.
4. Demo video plays and depicts the current version.
5. Screenshot is genuine or clearly marked concept.
6. Price, deliverables, usage rights, limits, and refund terms are visible.
7. Link, asset, accessibility, and smoke tests pass.
Otherwise use DRAFT, ASSET NEEDED, DEMO PENDING, or TEST FAILED. Keep “prepared” distinct from independently VERIFIED.

## Continuous quality loop
Customer feedback → triage → reproducible issue → prioritized change → regression test → changelog/version → refreshed screenshot/demo → re-publish QR target. Obtain consent before publishing identifiable customer information or testimonials.

## Ethical automation and outreach
Automate catalog checks, QR/link checks, demo reminders, and draft follow-ups. Do not send bulk messages or claim that any institution was contacted unless a real authorized channel was used and an auditable send result exists. Respect consent and unsubscribe requests.

## Measurable metrics
Track per product: required-asset completeness, QR success rate, demo playback success, test pass rate, page visits, demo starts/completions, enquiries, conversion, complaints/refunds, and time-to-fix. Report actual observed values only.

## First implementation checklist
- [ ] Receive/preserve exact owner photo asset
- [ ] Select first product and publish its real detail URL
- [ ] Produce product-specific visual using the approved template
- [ ] Test QR on mobile
- [ ] Capture actual UI screenshot or label concept preview
- [ ] Record and playback-test product-specific MP4
- [ ] Deploy page/assets and pass smoke test
- [ ] Only then mark product VERIFIED/READY
