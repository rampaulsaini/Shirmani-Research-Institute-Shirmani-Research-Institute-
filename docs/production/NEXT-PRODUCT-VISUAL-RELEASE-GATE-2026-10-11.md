# Product Visual Release Gate — 2026-10-11

## Purpose
Make the next showroom release verifiable at the individual-product level. This is an implementation contract, not evidence that all media has been generated or deployed.

## Canonical product identity
Every product record must have a stable unique product ID; a customer-readable unique product name and version; a one-sentence short description (target: 12–22 words); category, intended user, problem solved, usage steps, limitations and support route; a public passport URL that resolves before a QR is published; and media records with asset path/URL, source, dimensions, version, timestamp and QC result.

### Name governance
1. Prefer a plain-language name that states the actual job the product performs.
2. Do not use “AI”, “live”, “verified”, “4K”, “quantum”, “secure”, “automatic” or “supreme” as a capability claim unless that capability is implemented and tested.
3. Keep stable product IDs when display names change; record old names in version history.
4. Reject duplicate or misleading names during QC.

## Visual composition contract
- Master canvas: 3840 × 2160, 16:9. Verify actual dimensions before calling it 4K-ready.
- Main area: product-specific title and distinct artwork/screenshot.
- Upper-left: author-approved “निष्पक्ष समझ” photo/logo. Do not substitute an unrelated face or imply institutional certification.
- Beneath the logo, approved English identity line: “Shiromani Rampal Saini — Impartial Understanding · Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present”.
- Upper-right: QR only after the exact public passport URL resolves and the QR payload is scanned successfully.
- On-image: short description, stable product ID and version; price/offer only when backed by the current catalogue.
- Passport page: full description, intended users, use cases, steps, prerequisites, limitations, privacy notes, version history, support, price terms, demo and actual screenshot links.
- Each product needs its own asset identity. A shared generic video must not be represented as a unique product-specific recording.

## Required evidence per product
Track independently:
- visual_state: MISSING / DRAFT / QC_PASS / PUBLISHED
- qr_state: MISSING / URL_CHECKED / SCAN_PASS
- screenshot_state: MISSING / CAPTURED / QC_PASS
- demo_state: SCRIPT_ONLY / RECORDING_PENDING / RENDERED / PUBLISHED
- guide_state: MISSING / DRAFT / QC_PASS / PUBLISHED
- passport_state: MISSING / URL_CHECKED / PUBLISHED
- commercial_state: DEMO_ONLY / AVAILABLE_FOR_SCOPED_WORK / ORDER_CONFIRMED / PAID / DELIVERED

A storyboard is not an MP4. An SVG cover is not a captured browser screenshot. A generated QR image is not proof of a successful scan. A successful workflow run is not proof that every product asset exists.

## Release gates
1. Validate catalogue uniqueness and stable IDs.
2. Check each linked asset exists at its declared path/URL.
3. Validate dimensions, text overflow, mobile readability and contrast.
4. Resolve and scan every QR destination.
5. Open the demo, follow the guide and record observed results.
6. Verify a screenshot is a real capture of the named product; label illustrations as illustrations.
7. Mark unconnected voice/avatar/AI/payment/outreach capabilities NOT_CONNECTED.
8. Block unsupported claims; keep sales, payment, dispatch and independent verification separate.
9. Record failures as actionable tickets and rerun regression checks after fixes.

## First production batch
Start with one end-to-end product, not a blanket “100% complete” declaration:
1. SRI-PRES-001 — Heart-View Character Studio
2. SRI-MEDIA-003 — Product Release Pack Builder
3. SRI-WRITE-006 — First Client Deliverable Studio

For each, publish the visual, QR/passport, actual screenshot, demo status and usage guide only when each gate passes. Then expand in bounded batches.

## Metrics
Report from the actual manifest: catalog identities; concrete assets; valid passport links; QR scan passes; real screenshots captured; MP4 files rendered and playable; usage guides published; QC-passed products; products available for scoped work; confirmed orders, paid orders and delivered orders.

Never infer one metric from another. Catalog size, workflow runs and visual coverage do not prove sales or income.
