# SHIRMANI SUPREME — Product Description & Visual Identity Standard

**Status:** Specification and acceptance criteria. This document does not claim that every product image, QR code, demo video, voice integration, or live avatar has already been generated or published.

## 1. Public product description

Every product listing must answer in plain language:
1. **What it is:** one sentence with the product's actual purpose.
2. **Who it helps:** intended user or use case.
3. **What it does today:** only functions demonstrated in the current build.
4. **How to use it:** a short numbered path.
5. **What it does not do yet:** disclose missing integrations and manual steps.
6. **Evidence/readiness:** Prototype, Tested, or Verified, with dated test records and links.
7. **Next action:** Try demo, view guide, or submit an enquiry. Never imply checkout works unless it does.

### Plain-language template

**[Product name]** helps **[intended user]** do **[specific task]**. Enter **[required input]**, review **[actual output]**, then **[next step]**. This version currently supports **[tested features]**. **[Limitations]** are not yet automated. See the usage guide and test record before relying on results.

## 2. Product visual cover

Each product must have its own identity; do not reuse another product's title, QR destination, or demo as if it were its own.

Required cover elements:
- Product-specific name, readable at mobile size.
- One short, truthful benefit statement (preferably 8–16 words).
- Institute branding and a reserved portrait/logo slot.
- Product-specific QR pointing to its own stable detail page, guide, or demo.
- Visible readiness label: **Prototype**, **Tested**, or **Verified**.
- Good contrast, safe margins, responsive scaling, and readable text.
- Version/date when practical.

**Portrait fidelity:** When the owner's original portrait is available as an asset, place that exact file unchanged in the logo slot. Do not regenerate, retouch, stylise, or substitute a synthetic likeness. Keep the requested English identity line beneath it when space permits:

“Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Love; Eternal, Real, Natural, Universal Truth, Present Before Us.”

If the source portrait is not available to the build process, use a clearly marked placeholder and do not claim that the exact portrait has been applied.

## 3. Product-specific QR and long description

The QR destination must be unique to the product and resolve to a stable public page containing:
- Full description and intended users
- Step-by-step usage guide
- Demo video, or a clearly labelled storyboard if no video exists
- Product passport and version history
- Test status, known limitations, and evidence
- Feedback route and change log

A QR preview, destination text, or QR generator is not the same as a generated and tested QR image. Scan it on a second device before marking it tested.

## 4. Demo video and VIP screenshot

Track each item separately:
- Demo status: Not started / Storyboard ready / Recording ready / MP4 created / Playback checked / Published
- Screenshot status: Not captured / Captured / Reviewed / Published
- Actual asset URL or repository path
- Capture/render date and version
- Reviewer and pass/fail notes

Do not mark a storyboard as a video, a visual brief as a screenshot, or a cover as proof that the product itself works. For browser-only prototypes, capture the actual working UI and narrate only demonstrated behaviour.

## 5. Product passport fields

Minimum machine-readable passport:
- product_id, product_name, version, status
- purpose, intended_users, prerequisites
- tested_features, known_limitations
- demo_url, screenshot_url, guide_url, qr_target
- source_path, release_date, last_tested
- test_cases, results, reviewer
- pricing_model and terms, if approved
- feedback_url and change_log

Use empty values or “not available” for missing evidence. Never fabricate links, prices, reviews, test results, certifications, customer counts, sales, or revenue.

## 6. Voice, photo, and live presentation consent

Use the owner's supplied voice recording and portrait only when the actual files are available and use is authorised. Keep original assets unchanged. Before publishing cloned/synthesised speech or a lip-synchronised avatar, record provider, scope of consent, intended channels, and a revocation/contact route. Label synthetic presentation where viewers could mistake it for a live recording.

Pipeline: authorised source asset → transcript/content review → evidence gate → voice generation or recording → face/lip-sync → preview → human approval → publish → audit. A failed critical gate blocks release.

## 7. Evidence and readiness labels

- **Prototype:** interface or concept exists; production behaviour may be incomplete.
- **Tested:** listed test cases were run and results recorded.
- **Verified:** defined acceptance tests passed with reproducible evidence and independent review where appropriate.
- **Blocked:** a critical test, permission, asset, or integration is missing.

Use “insufficient evidence” when a claim cannot be supported. Philosophical or identity statements must be labelled as the author's viewpoint, not independently verified scientific findings.

## 8. Release checklist

- [ ] Product name and short benefit are accurate
- [ ] Original portrait asset availability checked; no synthetic replacement
- [ ] Product-specific QR destination opens correctly
- [ ] Full guide and passport are reachable
- [ ] Real demo video is present, or storyboard is explicitly labelled
- [ ] Real VIP screenshot is present, or absence is disclosed
- [ ] Mobile scaling, contrast, and legibility checked
- [ ] Known limitations and evidence state are visible
- [ ] Feedback route works
- [ ] No unverified claim of uniqueness, security, live AI, certification, sale, or revenue
- [ ] Human release approval recorded

## 9. Measurable reporting

Report counts from actual catalogue records only:
- products with complete plain-language descriptions / total listed
- products with working QR targets / total listed
- products with published MP4 demos / total listed
- products with reviewed screenshots / total listed
- products with complete passports and usage guides / total listed
- tests passed / tests run
- enquiries received, proposals sent, paid orders, and revenue—each a separate evidence-backed metric

Do not infer 100% completion from workflow runs, generated files, or planned tasks.
