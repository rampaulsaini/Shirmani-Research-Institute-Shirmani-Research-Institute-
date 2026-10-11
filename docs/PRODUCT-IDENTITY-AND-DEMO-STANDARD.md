# SHIRMANI Product Identity, Demo & Verification Standard

**Status:** Specification added on a working branch. This does not claim that product assets, videos, QR codes, integrations, sales, or production tests already exist.

## Public product-card standard

Every published tool/product must have its own identity and its own asset set. Never reuse another product's image, demo, passport, QR destination, or test results.

Each card must include:
- A distinct product name and version, marked approved only after owner approval and a uniqueness/trademark check.
- A product-specific image/screenshot with responsive scaling.
- The owner's exact approved portrait as a small logo only when the original source image is available and authorized. Never approximate or silently substitute a face.
- This requested English identity line: “Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Love; Eternal, Real, Natural, Universal Truth, Present and Direct.”
- A short, readable description on the image.
- A QR code to that product's canonical long description / Product Passport.
- A working demo video, or an honest “Demo pending” label.
- VIP screenshot/gallery, usage guide, supported uses, limitations, version, update date and test status.
- An enquiry/purchase action with scope, price/quote terms, delivery expectations and support/refund terms where applicable.

## First proposed pilot product

**Working name:** Nishpaksh Lens  
**Category:** Context-aware explanation and evidence-status assistant  
**Short description:** “Understand the question. Explain it simply. Show sources. Admit uncertainty.”  
**Use:** Turn a question or dense passage into a plain-language explanation, source-aware summary and explicit evidence status.

Evidence states:
- **VERIFIED:** documented verification has passed.
- **SOURCE-BASED:** source(s) are shown, but independent verification is not claimed.
- **PHILOSOPHICAL / IDENTITY:** personal philosophy or self-description, not presented as scientific proof.
- **INSUFFICIENT EVIDENCE:** say “Insufficient evidence is currently available.” / “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

This is a working name, not a claim that a naming team has approved it. Do not claim universal truth as a measured scientific result or invent citations, tests, capabilities, customers or income.

## Canonical Product Passport fields

`product_id, name, version, category, status, short_description, long_description, intended_users, use_cases, limitations, image_url, screenshot_urls, qr_destination, demo_video_url, demo_status, usage_guide_url, owner_portrait_asset, portrait_authorization_status, evidence_policy, test_plan, test_results, last_verified_at, release_commit, pricing_model, enquiry_url, delivery_terms, review_summary, issue_log, improvement_history`

Use explicit null or “pending” values for missing assets/verification. Never fabricate URLs or results.

## Demo and screenshot release gate

A product cannot be labelled READY or VERIFIED until applicable checks pass:
1. Page loads on mobile and desktop.
2. Product-specific image is readable and correctly scaled.
3. Portrait/logo is the exact approved source asset, if used.
4. QR scans and resolves to the matching Product Passport.
5. Demo video plays and demonstrates the described workflow.
6. Usage guide matches the current product version.
7. Core positive, negative and insufficient-evidence tests pass.
8. Enquiry route works and does not imply a sale before confirmation.
9. Accessibility, privacy, consent and security checks pass.
10. Release record links test results to the exact commit/version.

Allowed states: `DRAFT, ASSET_PENDING, DEMO_PENDING, TESTING, VERIFIED, RELEASED, BLOCKED`. A successful workflow alone is not product verification.

## Asset production pipeline

Product specification → owner/name approval → product-specific UI/screenshot → approved portrait/logo placement → short on-image description → canonical passport page → QR generation and scan test → demo recording → usage guide → automated checks → human review → publish → feedback and versioned improvement.

A QR code must encode the actual canonical URL for that product and must be decoded/tested before publication.

## Feedback and quality loop

Capture voluntary customer feedback with consent. Separate star rating, issue report, feature request and verified defect. Never fabricate testimonials or inflate ratings. Give each accepted issue an ID, severity, status, target version and regression test. Publish only privacy-safe aggregate feedback.

## First measurable pilot acceptance criteria

Before scaling:
- One pilot product has a unique product ID and owner-approved name.
- One distinct image and screenshot are available and visually checked.
- One canonical passport opens successfully.
- One QR scan resolves to that passport.
- One real demo video plays and matches the feature list.
- One usage guide matches the tested version.
- Critical tests pass; failures remain visible.
- Enquiry route is tested end-to-end.
- No sales, external outreach, production-readiness or independent-verification claims without evidence.

After the pilot passes, reuse the pipeline, not the product assets, to scale the catalogue.
