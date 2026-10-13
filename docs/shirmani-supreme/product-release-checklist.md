# SHIRMANI SUPREME — Product Release Checklist

**Status: specification / release gate.** This checklist does not assert that any product media, QR destination, voice provider, or live presentation has already been integrated.

## Product identity
- [ ] Unique product name, immutable product ID, version, owner, and release date recorded.
- [ ] One product-specific passport page exists at a stable HTTPS URL.
- [ ] Passport states purpose, intended users, prerequisites, limitations, price/offer (only if approved), support route, version history, and evidence state.

## Original identity media
- [ ] Owner-supplied original photo asset is present and provenance is recorded.
- [ ] Image comparison confirms no alteration other than proportional resize, display scaling, and layout placement.
- [ ] Authorized original voice recording/provider permission is documented before voice use.
- [ ] If either asset is missing, mark the corresponding capability **BLOCKED**; do not substitute generated media.

## Product artwork
- [ ] Product-specific artwork is 3840 × 2160 before claiming 4K.
- [ ] Original photo/logo appears unaltered except proportional scaling.
- [ ] Exact English identity line appears beneath the photo: `Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Satya Pratyaksh Samaksh`.
- [ ] Product-specific QR appears in the upper-right and resolves to this product's passport.
- [ ] Short description is legible on the artwork at mobile size.
- [ ] Screenshot is a real capture of the actual product; otherwise label it **ILLUSTRATIVE MOCK-UP**.

## Demo and QR verification
- [ ] Product-specific demo video is actually recorded; otherwise label the asset **STORYBOARD — NOT RECORDED**.
- [ ] Demo shows the real product, the intended task, expected inputs/outputs, limitations, and version.
- [ ] QR code scanned successfully on at least one mobile device; resolved URL and destination product ID match.
- [ ] Screenshot, video, QR destination, and passport all identify the same product ID/version.

## Function and evidence gates
- [ ] Setup/use instructions tested by a person other than the author where practical.
- [ ] Claims are labelled `INDEPENDENTLY VERIFIED`, `SOURCE-BASED`, `PHILOSOPHICAL / PERSONAL PERSPECTIVE`, or `INSUFFICIENT EVIDENCE` as appropriate.
- [ ] For insufficient evidence, show: `अभी पर्याप्त प्रमाण उपलब्ध नहीं है।`
- [ ] Voice, avatar, lip-sync, and live capabilities are marked verified only after a successful end-to-end test with a saved test record.
- [ ] Critical test failures block public release.

## Commercial and outreach gates
- [ ] Scope, deliverables, deadline, price, payment terms, and refund/revision conditions are agreed in writing before work starts.
- [ ] Customer contact is made only through an authorized channel and recorded truthfully.
- [ ] Never report an enquiry as a sale, a sent message as a reply, or a workflow run as verified product quality.
- [ ] Record measurable outcomes: qualified enquiries, replies, demos completed, paid orders, delivery acceptance, refunds, and repeat requests.

## Release record
| Field | Value |
|---|---|
| Product ID / version | Pending |
| Passport URL | Pending |
| Original photo check | BLOCKED until source asset is available |
| Authorized voice check | BLOCKED until source asset and authorization are available |
| QR mobile scan | NOT TESTED |
| Demo video | STORYBOARD — NOT RECORDED until a real video exists |
| Real product screenshot | ILLUSTRATIVE MOCK-UP until captured from a working build |
| End-to-end test evidence | NOT TESTED |
| Release decision | BLOCKED until required gates pass |

This checklist is an operational control, not proof that any checkbox has passed. Update each field only from observed evidence.