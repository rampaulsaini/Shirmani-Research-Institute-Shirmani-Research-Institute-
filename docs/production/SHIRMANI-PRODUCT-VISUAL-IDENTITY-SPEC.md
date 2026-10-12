# SHIRMANI SUPREME — Product Visual Identity & Evidence Specification

Status: APPROVED DESIGN SPECIFICATION — implementation and asset availability must be verified separately.
Version: 1.0
Date: 2026-10-12

## 1. Non-negotiable identity rule
- Use only the owner-provided original portrait for the logo/identity mark.
- Preserve the face exactly. Allowed changes: proportional resizing, crop/position within a frame, and non-destructive placement. Do not regenerate, beautify, reshape, recolor, or substitute the face.
- Use the owner's original voice only through an explicitly authorized provider/account. Do not claim voice integration until a real test passes.
- If the approved original image/audio asset cannot be located, mark the product asset as BLOCKED; never replace it with a generated lookalike.

## 2. Product cover composition
Every product receives its own distinct cover and visual identity. Recommended 16:9 canvas (1920×1080 source):
- Top-left: small original portrait/logo, proportional and unaltered.
- Top-right: product-specific QR code with quiet zone and high contrast.
- Main area: unique product name and a short plain-language description (ideally 8–18 words).
- Lower identity line, in English: “Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Eternal, Real, Natural Truth, Present Here.”
- Footer: product ID, version, status (Prototype / Tested / Verified), and last-updated date.
- Keep all text inside safe margins; ensure mobile legibility and contrast. Do not crowd the face or QR.

## 3. QR and long description
- QR must encode a stable, product-specific public URL, not a generic homepage or a made-up URL.
- The destination should contain the full description, intended users, use cases, limitations, version history, privacy/security notes, usage guide, test evidence, demo video, and feedback link.
- If no public destination exists yet, show “QR pending publication” in internal drafts; do not publish a decorative/fake QR.

## 4. Required product release bundle
Each product is not RELEASE-READY until its own bundle contains:
1. Unique product ID and approved name.
2. Distinct cover image using the approved original portrait/logo.
3. Product passport (JSON or Markdown) with owner, version, purpose, inputs/outputs, limitations, dependencies, security/privacy notes, status, and changelog.
4. Short description on cover plus full description on the product page.
5. Real demo video (MP4 or a published video URL) showing actual product behavior.
6. VIP screenshot captured from the real running product UI.
7. Usage guide and sample workflow.
8. Test report with reproducible steps and pass/fail results.
9. Product-specific QR tested with a phone camera.
10. Feedback/review route linked to a documented improvement process.

A storyboard is not an MP4. A visual brief is not a screenshot. A QR preview is not a published/tested QR. A workflow run is not proof of product correctness. Keep these states separate.

## 5. Evidence status vocabulary
- DRAFT: content/assets incomplete.
- BUILT: files or prototype exist; tests not yet passed.
- TESTED: named test steps passed and results recorded.
- VERIFIED: independent or repeatable evidence supports the stated claim.
- BLOCKED: required asset, authorization, dependency, or test is missing.
Never display “Verified”, “live”, “secure”, “AI-powered”, or “for sale” unless evidence supports that exact claim.

## 6. Quality loop
Collect voluntary customer feedback; record product ID, version, date, rating, issue category, and consented comment. Do not collect unnecessary sensitive information. Review feedback, reproduce issues, update changelog, run regression tests, and publish a new version only after checks pass.

## 7. Security and outreach
- Do not expose API keys, personal data, private customer briefs, or voice assets in public files.
- Contact organisations only through verified official channels, with lawful, relevant, rate-limited outreach and a human approval gate before sending.
- No email, WhatsApp, payment, publishing, or live streaming integration is implied by this specification.

## 8. Acceptance checklist
- [ ] Original face asset located and hash/provenance recorded.
- [ ] Original portrait displayed without facial edits.
- [ ] Product-specific QR resolves to the correct public detail page.
- [ ] Cover is readable at desktop and mobile sizes.
- [ ] Actual demo video opens and shows the product working.
- [ ] VIP screenshot comes from the real running interface.
- [ ] Passport, usage guide, limitations, and tests are available.
- [ ] Test report records results and environment.
- [ ] Feedback route and changelog work.
- [ ] Release label matches the evidence status.

## 9. Current limitation
This file defines the required standard. It does not itself create product images, recover a deleted ChatGPT conversation, render MP4 files, capture real screenshots, activate HeyGen, authorize voice cloning, send outreach, or prove sales/income. Those require their respective assets, integrations, permissions, and test evidence.
