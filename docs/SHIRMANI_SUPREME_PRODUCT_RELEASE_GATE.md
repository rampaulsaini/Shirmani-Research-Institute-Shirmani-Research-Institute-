# SHIRMANI SUPREME — Product Release Gate

**Status:** specification / implementation checklist. This document does not certify that any product, photo, voice, QR, demo, payment, or outreach integration is live.

## 1. Required product record

Every product must have its own record. Do not reuse another product's QR destination, screenshot, demo, version, or claims.

- `product_id`: stable unique identifier
- `product_name`: finalized human-readable name
- `version`: semantic version (for example, `0.1.0`)
- `status`: one of `IDEA`, `PROTOTYPE`, `TESTING`, `VERIFIED`, `PUBLISHED`, `RETIRED`
- `short_description_hi` and/or `short_description_en`
- `long_description_passport_url`: canonical product-specific passport page
- `qr_asset`: QR generated from that exact passport URL
- `qr_scan_test`: device, date, destination, and pass/fail evidence
- `vip_screenshot_url`: actual screenshot of the running product; mock-ups must be labelled
- `demo_video_url`: product-specific recording showing actual usage; storyboard is not a demo
- `usage_guide_url`: prerequisites, steps, limitations, and troubleshooting
- `original_identity_asset_status`: source and permission status for any logo/photo/voice used
- `test_evidence_url`: reproducible test results, environment, date, and known failures
- `known_limitations`: explicit list, including unavailable integrations
- `price_and_terms`: only when approved; scope, delivery, refund/cancellation terms, and payment status
- `outreach_status`: `NOT_PREPARED`, `DRAFTED`, `APPROVED`, `SENT`, `REPLIED`, `CONVERTED`; set `SENT` only with outbound-channel evidence
- `last_reviewed_at` and `change_log`

## 2. Visual-artwork contract

Target artwork: 3840×2160 pixels (16:9). Never claim 4K unless the exported file dimensions are checked.

1. Use the supplied original “मेरी निष्पक्ष समझ” photo only when the exact source asset is available and its use is authorized.
2. Preserve the photo unchanged. Allowed operations: proportional resize, display scaling, and placement. No generation, redraw, retouch, recolouring, beautification, reshaping, or replacement.
3. Place the photo/logo at the top, with this identity line beneath it:
   `Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh`
4. Put the product-specific QR in the upper-right. It must open that product's long-description passport, not a generic homepage.
5. Put a concise, readable product description on the artwork.
6. Use a real product-specific screenshot. If only a concept visual exists, label it `ILLUSTRATIVE MOCK-UP`.
7. Include a real, product-specific MP4 demo with narration or captions showing setup, one representative task, result, and limitations. If not recorded, label it `STORYBOARD — NOT RECORDED`.
8. Test the QR with a mobile device after export. A QR image existing in the file is not proof that the destination works.

## 3. Release gates

A product may be marked `VERIFIED` only if all critical gates pass:

- [ ] Product ID, name, version, scope, and limitations recorded.
- [ ] The product itself runs in a documented environment.
- [ ] Reproducible functional tests pass and logs are attached.
- [ ] Original identity assets and authorization are confirmed, or those elements are omitted and marked blocked.
- [ ] Screenshot is captured from the actual running product.
- [ ] Product-specific demo video is recorded and reviewed.
- [ ] Passport URL opens and matches the product/version.
- [ ] QR is scanned on mobile and resolves to the correct passport.
- [ ] Accessibility/readability check passes at mobile display size.
- [ ] Security/privacy review is complete for the product's actual data flows.
- [ ] Price, deliverables, terms, and payment state are accurate and separately recorded.

A failed critical gate blocks release. Workflow success, a generated image, a code commit, or a high product count alone is not product verification.

## 4. Authorized voice and live-presenter chain

`Original authorized audio → speech-to-text → context/intent → reasoning → evidence gate → response script → authorized voice output → face/lip-sync provider → live presentation → audit`

For each stage record provider/version, permission status, input/output test, latency, failure handling, and timestamp. Do not claim the user's original voice or live face is integrated until the original asset is available, authorization is documented, and end-to-end tests pass. Do not substitute a synthetic voice or generated face when the required original asset is missing.

## 5. Evidence labels

- `INDEPENDENTLY VERIFIED`: independent test/evidence attached.
- `SOURCE-BASED`: cited source exists, but independent verification is incomplete.
- `PHILOSOPHICAL / PERSONAL PERSPECTIVE`: values, identity, or interpretation; not presented as scientific proof.
- `INSUFFICIENT EVIDENCE`: say `अभी पर्याप्त प्रमाण उपलब्ध नहीं है।`

## 6. Ethical outreach and income reporting

- Prepare a prospect only from a public, official, relevant source.
- Draft messages must identify the real service offered: Hindi/English writing, research summaries, or website/blog content.
- Never imply an institution endorsed the Institute or claim a message was sent without an authorized outbound channel and delivery evidence.
- Track `drafted`, `approved`, `sent`, `replied`, `proposal`, `paid`, and `delivered` separately.
- Report income only from verifiable completed payments; enquiries, proposals, views, and workflow runs are not income.
- Confirm scope, price, deadline, deliverables, and payment terms in writing before starting client work.

## 7. Portfolio-first implementation order

1. Select one real writing/research service as the first portfolio product.
2. Publish its truthful service page and product passport.
3. Capture a real screenshot of the page/service workflow.
4. Record a short screen demo of the actual process and output; do not present a storyboard as a recording.
5. Generate and mobile-test its QR.
6. Run the release gates and publish only the gates that pass.
7. Use this first verified pattern as the template for additional products.

**Current asset limitation:** the repository contract previously recorded the original photo and voice as not verified in the repository. Until those exact assets are located and confirmed, their use remains blocked; this checklist does not replace them.
