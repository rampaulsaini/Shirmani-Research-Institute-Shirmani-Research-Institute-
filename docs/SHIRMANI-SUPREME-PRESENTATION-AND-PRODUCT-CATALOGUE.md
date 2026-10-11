# SHIRMANI SUPREME — Human Presentation & Product Catalogue Specification

Status: SPECIFICATION DRAFT — implementation and production tests not yet verified.
Owner: Shirmani Research Institute
Last updated: 2026-10-11

## 1. Product objective
Build a respectful, evidence-aware presentation system and a catalogue where every digital tool has a distinct identity, usage instructions, a demonstration, and a measurable quality-improvement path. Do not claim production readiness, sales, external contact, or verified performance without evidence.

## 2. Human presentation requirements
- Communication: simple, सहज, निर्मल, transparent, direct, respectful, adapted to audience language and context.
- Use the owner's photo and voice only from user-provided assets and for authorized uses. Record asset provenance and authorization before synthesis or publication.
- Pipeline: voice input → speech recognition → context/intent → reasoning → evidence gate → answer/content → authorized voice output → face/avatar → lip-sync → live presentation → audit.
- Keep gaze and facial motion natural; synchronize speech and mouth movement; measure end-to-end latency.
- Do not imply an avatar is the real human currently live. Label generated or prerecorded presentation when relevant.
- Respect people and communities; never demean or rank users by caste, religion, gender, wealth, or organization.
- Distinguish personal/philosophical statements from independently verified scientific claims.

## 3. Evidence states
1. VERIFIED — evidence and verification procedure are recorded.
2. SOURCE-BASED — source cited but independent verification is incomplete.
3. PHILOSOPHICAL / IDENTITY — opinion, framework, self-description, or philosophical statement.
4. INSUFFICIENT EVIDENCE — say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है。”
Store source references, timestamp, uncertainty notes, and audit status for substantive answers where appropriate. Never fabricate sources.

## 4. Product catalogue card
Each product needs a unique product ID, approved name, version, category, status, short description, audience, use cases, prerequisites, limitations, approved price/offer, support route, and update history.
- Give every product a distinct visual identity; never use one image as if it represented every product.
- The owner's photo may appear as a small logo only when the actual approved image asset is available.
- English tagline exactly as supplied: “Shirmani Rampal Saini Tulnatit Kalatit Shabdatit Prematit Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh”.
- Put a QR code at upper-right, linked to the canonical long-description/product page URL. Never use an untested decorative QR.
- Put a readable short description on the image; place long description, instructions, limitations, version history, and support details on the linked page.
- Check responsive scaling and contrast on mobile and desktop.
- Do not claim the tagline or QR is present until the actual image and QR scan test pass.

## 5. Required deliverables for every sellable tool
- Product page and unique product image.
- Demonstration video showing real supported behavior; label mock-ups clearly.
- VIP/feature screenshot from the working product.
- Quick-start guide and full usage guide.
- Test report, known limitations, version and update log.
- Customer feedback/rating form linked to a documented improvement loop.
- Approved price, licence, refund/support terms, and payment method.
- QR destination tested on mobile and desktop.

## 6. Product-specific demo-video factory
Input: product ID + current build + approved script + demo environment.
Steps: validate build → capture real screen → narrate supported use → add captions → redact secrets/personal data → render video → check playback/accessibility → publish → store evidence.
A promo video must not imply functionality the product does not have. Failed checks block publication.

## 7. Catalogue scale and global directory
For a future 150,000-item catalogue, use sharded storage, stable IDs, search indexes, pagination, deduplication, versioned schemas, observability, backups, and access controls. Do not claim this scale is operational until load, recovery, and benchmark tests are recorded.
For organizations, record official website/source URL, public contact page, relevant department, source-check date, outreach permission/status, and outcome. Do not scrape private contact data or send unsolicited bulk messages. External outreach needs approved content, an authorized channel, rate limits, opt-out handling, and a real delivery log.

## 8. Revenue-first service workflow
Initial offer: Hindi/English writing, research summaries, and website/blog content.
Enquiry fields: customer objective; topic; language; word count; deadline; source links/material; budget.
Before work starts, confirm scope, deliverables, timeline, price, revisions, payment terms, and acceptance criteria in writing. Do not claim income or customer acquisition without payment/CRM evidence.
Suggested first target: publish one transparent service page, prepare three sample deliverables marked as samples, and send five individually researched relevant proposals through permitted channels. This is a target, not a claim that outreach has occurred.

## 9. Test gates
Block production release unless applicable tests pass:
- Speech recognition and language handling
- Context/intent test set
- Source citation and unsupported-claim tests
- Insufficient-evidence response
- Respectful communication regression tests
- Authorized voice asset check
- Face/voice synchronization and lip-sync
- Latency and playback
- QR scan and destination
- Demo matches actual product behavior
- Mobile/desktop image readability
- Security/privacy review and secret redaction
- Feedback capture, rollback, and audit logs

Record test name, build/version, environment, result, evidence link, reviewer, timestamp, and failure details. “Workflow completed” is not “independently verified.”

## 10. Implementation order
1. Inventory the repository and identify the actual public catalogue entry point.
2. Add one pilot product card for a real existing tool with verified screenshot.
3. Add its real demo video and usage guide.
4. Add QR only after its canonical destination is live and tested.
5. Run mobile/desktop, accessibility, security, and evidence checks.
6. Publish the pilot after review; then expand the template.
7. In parallel, publish the writing/research enquiry page and measure genuine leads and paid conversions.

## 11. Honest status
This file defines requirements only. It does not establish that the avatar, voice provider, lip-sync, QR catalogue, 5,000 products, 150,000-item directory, email system, payments, external outreach, or sales are implemented or verified. Each status needs repository artifacts and test evidence.
