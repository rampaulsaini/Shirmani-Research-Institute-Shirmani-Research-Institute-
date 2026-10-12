# SHIRMANI SUPREME — Product Presentation Standard
Version: 1.0  
Status: Specification drafted; visual deployment and end-to-end verification are not yet confirmed.

## Purpose
Every SHIRMANI tool or digital product must have a distinct, honest, accessible product identity that explains what it does, who it helps, how to use it, what has actually been tested, and how to request or purchase it.

## Product-card composition
1. **Product-specific visual:** one unique 16:9 hero image or screenshot per product; no duplicated generic image presented as a real product interface.
2. **Owner-provided portrait/logo:** use only the exact original portrait supplied/authorized by Shiromani Rampal Saini. Preserve facial features and proportions. Permitted processing: proportional resizing, cropping only with approval, and placement in a logo frame. Do not synthesize, redraw, beautify, or replace the portrait.
3. **Identity line:** “SHIROMANI RAMPAL SAINI — TULANATEET, KAALATEET, SHABDAATEET, PREMATEET, SHAASHVAT, VAASTAVIK, SWABHAVIK SATYA, PRATYAKSH SAMAKSH.” Keep legible and do not cover the product UI.
4. **Product name:** unique, readable, reviewed name; do not claim an AI team finalized a name unless that review is recorded.
5. **Short on-image description:** one plain-language sentence, ideally 8–16 words, describing the real function rather than superlative claims.
6. **QR code:** upper-right, high contrast, with quiet zone and label “SCAN FOR DETAILS”. It must encode a stable, product-specific public URL or product passport. Never use a decorative/fake QR. Test it on at least two devices before release.
7. **VIP screenshot:** a real screenshot from the current working product, clearly labelled “Preview” if not production-ready. Never fabricate usage results or customer screens.
8. **Version/status marker:** e.g. Prototype, Beta, Tested, or Verified. Use “Verified” only when the named test suite passed and evidence is linked.
9. **Demo video:** product-specific MP4 or hosted demo showing purpose, setup, a representative workflow, output, limitations, and next step. If no actual demo exists, show “Demo pending” instead of a placeholder presented as completed.
10. **Actions:** Details, Try demo, Read guide, Request a quote / Buy. Payment and order status must be real; no sale or revenue is claimed without transaction evidence.

## Product passport (QR destination)
Each passport should include:
- Product ID, canonical name, version, owner/team, last-updated date
- Purpose, target users, supported inputs/outputs, step-by-step usage
- Real screenshot, demo link, downloadable guide where available
- Dependencies, privacy/data handling, accessibility, known limitations
- Test cases, dated results, evidence links, changelog
- Price and offer only when configured and approved
- Contact / enquiry form and support expectations
- Review/rating controls with moderation and a documented improvement loop

## Short-description formula
“[Product name] helps [intended user] do [specific task] using [actual capability].”
Avoid “world’s best”, “unmatchable”, “guaranteed”, scientific claims, or performance numbers unless independently substantiated.

## Voice and human-presentation products
Pipeline: consented source voice/photo → authorized provider integration → speech recognition → context and intent → evidence gate → response/content → voice output → face/lip-sync → preview → audit.
- Use only the owner’s original supplied/authorized voice recording; do not imply that a provider is connected until its integration and a live test succeed.
- Label generated media as AI-assisted where relevant.
- Separate philosophical/identity statements from scientific claims.
- Evidence states: VERIFIED, SOURCE-BASED, PHILOSOPHICAL / IDENTITY, INSUFFICIENT EVIDENCE.
- When evidence is inadequate, say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
- Never claim continuous live operation, autonomous permanent work, or production readiness without uptime, safety, permission, and end-to-end test evidence.

## Release gates
A product card may be published as **Ready for Sale** only when:
- Product URL and owner-approved product name resolve.
- Product-specific screenshot matches the current build.
- QR opens the correct passport and has been scan-tested.
- Demo plays and matches the advertised workflow.
- Usage guide and limitations are present.
- Price, terms, contact path, and payment destination are checked.
- Accessibility and mobile scaling are checked.
- Product tests and evidence are linked.
- Customer reviews are real and moderated.
Otherwise show the exact state: Draft, Prototype, Demo Pending, Test Failed, or Evidence Pending.

## Measurement
Track per product: unique product cards, valid QR destinations, QR scan-test pass rate, demo availability, guide completeness, test pass rate, qualified enquiries, quote acceptance, paid orders, refunds, customer ratings, and issues resolved. Report actual counts and dates; never infer sales from page views or workflow runs.

## Asset dependency
The exact original portrait and voice assets must be available in the repository or explicitly provided to the authorized workflow before asset-specific output can be built. If unavailable, preserve the existing asset reference and mark the asset-dependent gate as blocked; do not substitute a generated likeness or invented voice.
