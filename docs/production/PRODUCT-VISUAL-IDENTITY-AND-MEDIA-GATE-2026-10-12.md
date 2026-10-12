# SHIRMANI SUPREME — Product Visual Identity & Media Release Gate
**Revision:** 2026-10-12  
**Branch:** supreme-product-media-gate-2026-10-12  
**Status:** implementation standard; product-by-product assets still require creation and testing.

## Purpose
Give every product a distinct, readable, evidence-backed visual identity without falsely presenting planned media as finished. This is a release contract, not proof that any particular product's photo, QR image, screenshot, or MP4 has already been updated.

## Non-negotiable identity lock
- Use only the owner's original supplied portrait as the portrait/logo source.
- Preserve the face exactly. Permitted changes: proportional scaling, crop/frame placement that does not distort facial features, and background/layout around the portrait.
- Do not generate, retouch, beautify, recolour, reshape, or replace the face.
- Use original audio only when the actual file is available and its use is authorised. Do not label synthetic/substitute audio as the owner's original voice.
- If either asset is missing, show a clearly labelled placeholder and mark the asset `NOT PROVIDED`; do not silently substitute another image or voice.
- Keep an asset ledger with filename/reference, provenance, authorisation status, and last-tested date.

## Required per-product media pack
Each product must have its own stable product ID, approved product name, version, and product-specific destination.

| Asset | Required evidence | If missing |
|---|---|---|
| Product cover image | Real image file/path; opens correctly; mobile scaling checked | `NOT CREATED` |
| Owner portrait/logo | Exact supplied source asset; no facial alteration | `SOURCE REQUIRED` |
| Short on-image description | Plain-language benefit, intended use, and honest capability boundary | `COPY REVIEW REQUIRED` |
| QR code image | Scannable QR resolving to the exact product passport/demo page | `QR NOT GENERATED` |
| Product passport | Long description, version, inputs/outputs, limitations, requirements, price/quote terms, support and privacy notes | `PASSPORT MISSING` |
| Demo video (MP4) | Actual playable recording showing a real product workflow and output | `STORYBOARD ONLY` until recorded |
| VIP screenshot | Actual screenshot captured from the real product interface | `SCREENSHOT BRIEF ONLY` until captured |
| Usage guide | Step-by-step instructions and a sample task/result | `GUIDE MISSING` |
| QC record | Dated tests, expected/actual result, defects, reviewer and release decision | `NOT VERIFIED` |
| Enquiry/order route | Tested route, written scope/price/payment terms before work begins | `ROUTE NOT TESTED` |

## Cover layout
1. Top-left: owner's original portrait/logo, used unchanged and kept legible.
2. Main area: product-specific approved name and a short description in high-contrast text.
3. Top-right: product-specific QR code with a quiet zone and a short label such as “Scan for full details”.
4. Lower area: version, product ID, and truthful readiness badge: `DEMO`, `BETA`, or `VERIFIED` only when the corresponding evidence exists.
5. Keep the full cover readable on a narrow mobile screen; avoid tiny text and prevent the QR from overlapping the portrait or description.
6. The English identity line may appear below the portrait only when it remains readable: “Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh.”

## Readiness labels
- **PLANNED:** idea or written specification only.
- **PROTOTYPE:** a usable draft exists but has not passed the full release gate.
- **DEMO-READY:** the described local workflow was run and the visible output was checked; connected services must be labelled separately.
- **VERIFIED:** specific acceptance tests passed and evidence is linked.
- **BLOCKED:** a required asset, permission, test, or integration is missing.
- **RELEASED:** the approved version is published and its live URL was checked.

Do not treat a workflow run, generated storyboard, QR preview, image brief, or catalogue record as proof of a finished MP4, QR image, screenshot, integration, sale, or independent verification.

## Minimum release tests
- [ ] Product ID/name/version match across cover, QR destination, passport, demo and catalogue.
- [ ] QR scans from the rendered cover and opens the intended public destination.
- [ ] Cover is readable at mobile size; no overlap, clipping, or distorted portrait.
- [ ] Description matches what the tool actually does today.
- [ ] Demo is a real playable file, not a storyboard, if marked as a video.
- [ ] Screenshot comes from the actual interface, not a mockup, if marked as a screenshot.
- [ ] Usage guide reproduces the sample workflow.
- [ ] Limitations, privacy, pricing and payment conditions are visible before a customer commits.
- [ ] Every claim marked VERIFIED links to a dated test result or evidence record.
- [ ] Critical failure blocks release; defect and retest are recorded.

## Suggested per-product status record
```json
{
  "product_id": "SRI-EXAMPLE-001",
  "name": "Approved product name",
  "version": "0.1.0",
  "status": "PROTOTYPE",
  "portrait_asset": {"state": "SOURCE REQUIRED", "reference": null},
  "cover": {"state": "NOT CREATED", "path": null},
  "qr": {"state": "QR NOT GENERATED", "destination": null},
  "passport": {"state": "MISSING", "path": null},
  "demo_mp4": {"state": "STORYBOARD ONLY", "path": null},
  "vip_screenshot": {"state": "SCREENSHOT BRIEF ONLY", "path": null},
  "usage_guide": {"state": "MISSING", "path": null},
  "qc": {"state": "NOT VERIFIED", "evidence": []},
  "last_checked": null
}
```

## Release rule
A product can be shown in the public showroom as a draft only with its true readiness label. It cannot be marked fully complete until its actual product-specific cover, scannable QR, passport, real demo video, actual screenshot, usage guide, and passing QC evidence are all linked and checked. Do not bulk-mark the catalogue complete.
