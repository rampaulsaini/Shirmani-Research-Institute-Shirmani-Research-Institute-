# SHIRMANI Public Interface & Revenue Execution Roadmap
**Date:** 2026-10-18
**Branch:** feat/public-interface-revenue-evidence-roadmap
**Status:** Proposed implementation contract; not proof of deployment, live integrations, sales, or revenue.

## Purpose
Replace the confusing everything-on-one-page experience with a clear public journey while preserving every submitted project, product, research asset, and future module. Make the first practical revenue path visible without pretending unconnected forms are order, email, payment, or AI backends.

## 1. Public navigation: one clear route from top to bottom
1. Home — Shirmani स्वरूप दृष्टिकोण: concise mission, plain-language introduction, primary calls to action.
2. Explore the Showroom: searchable/filterable catalogue; product cards show name, stable ID, version, purpose, status, approved price only, and product-page link.
3. Writing & Research Services: Hindi/English writing, editing, source-linked summaries, website/blog content; sample work and limitations.
4. Live demos & test drives: each product has its own passport; real demo, screenshots, QR, test evidence and usage guide are individually labelled real, pending, or concept.
5. Heart-View / Human Presentation: explain the character and evidence chain in plain language; never imply live avatar, original voice or lip-sync has passed without recorded tests.
6. Research Library: curated collections by subject, language, format, date and evidence status; distinguish public-domain, licensed, user-supplied and link-only resources.
7. Labs & Tools: group prototypes and verified tools separately; show requirements, limitations, versions and support route.
8. Community / Social: present only working features; label planned social functions as planned until account creation, posting, moderation, privacy and security tests pass.
9. Sign in / Create account: show only when a functioning authentication provider and secure account flow are deployed; a visual mock-up is not working login.
10. Contact / Enquiry / Terms / Privacy / Accessibility: always findable from the footer.

## 2. Product card and passport contract
Every product keeps its own stable identity: product ID, title, category, version, lifecycle status, purpose, intended user, example use, prerequisites, limitations, approved current price, real demo status, screenshot authenticity label, QR destination test, evidence status, usage guide, version history, feedback route, privacy and support details. Only generate a QR after its canonical HTTPS page exists. Never invent a demo URL or reuse one generic QR for every product.

## 3. Safe catalogue cleanup — no destructive blind filtering
1. Inventory and tag before moving anything: active, duplicate-candidate, obsolete-candidate, blocked, archive-candidate.
2. Compare exact content, links, stable IDs, inbound references, workflow use and product dependencies before calling anything a duplicate.
3. Move confirmed obsolete items to a dated archive/quarantine with a manifest and restoration path before deletion.
4. Do not delete a file or product merely because it is hidden, incomplete, old, or not yet shown publicly.
5. Never remove source research, original media, user-provided material, product records or automation dependencies without evidence that it is redundant and safe to retire.
6. Every cleanup batch records files considered, rationale, dependency checks, before/after counts and rollback instructions.

## 4. First income lane: small, truthful, deliverable-first
Available scope: Hindi/English writing and editing; source-linked research summaries with limitations; website/blog content.

Use existing repository assets first:
- writing-research-enquiry.html
- writing-research-sales.html
- products/concrete/SRI-WR-001-writing-research-enquiry-studio.html
- showroom/first-client-deliverable-studio.html
- showroom/writing-research-enquiry-builder.html
- docs/income/VERIFIED-WRITING-RESEARCH-LAUNCH-SPRINT-2026-10-16.md

The existing launch sprint suggests discussion-only pilot references of ₹499 (up to 800-word source-based summary), ₹999 (up to 800-word website/blog draft), and ₹1,499 (short bilingual pack up to 1,000 words total). These are not guaranteed quotes. Confirm scope, deadline, revisions, final price and payment terms in writing before accepting work.

Operational chain: verify enquiry page on mobile and desktop; prepare two source-labelled samples with human QC checklist; research relevant organisations using official contact pages; send tailored outreach only through an authorised working channel; track prospect researched → message actually sent → reply received → quote sent → written acceptance → payment received → deliverable delivered → customer acceptance. Count income only from real payment evidence. A draft, prospect, quote, workflow success or enquiry form is not revenue.

## 5. Human-presentation evidence chain
Voice/input → authorised voice integration → content/Q&A → photo/avatar → lip-sync → live presentation → audit.

Record separate results for video playback, original photo identity/crop, voice source and authorization, intelligibility and content accuracy, lip-sync timing, Q&A correctness/citations/insufficient-evidence fallback, latency, mobile compatibility, privacy and failure handling.

The owner already supplied this HeyGen reference: https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7. Its existence alone does not prove video, original voice, lip-sync or live Q&A passed independent end-to-end testing. Do not ask the owner to re-upload the same URL; inspect accessible project assets and provider state first.

## 6. Security and automation gates
- Least-privilege workflow permissions; no broad tokens or secrets in files/logs.
- Validate form input, escape rendered user text, protect against injection/spam, and keep customer data minimal.
- Authentication and payment must use secure supported providers; never store raw passwords or card details in a static site.
- Automated outreach must not send until sender identity, contact source, relevance, opt-out handling and human approval are configured.
- Scheduled checks produce actionable, deduplicated reports; do not rerun successful jobs without a reason or delete records to hide failures.
- Every automated task records input, output, exit status, evidence artifact and next action.

## 7. Measurable acceptance criteria
- A first-time visitor can identify the service, see examples and find the enquiry route within 30 seconds in a moderated usability check.
- Top navigation and footer links have no broken internal links in automated checks.
- Mobile layout works at 360 px and desktop at 1280 px without horizontal overflow.
- Product cards link to matching passports; no generic/reused QR or fabricated screenshots.
- Every item has honest lifecycle/evidence status.
- Enquiry generation works locally and clearly says it has not sent an order/email/payment.
- Login, live demo, voice, lip-sync, payment and outbound email remain pending until their own tests pass.
- Cleanup changes have a manifest and rollback path.
- Revenue dashboard counts only evidenced messages, accepted jobs, delivered work and received payments.

## 8. Execution order
P0 protect source materials; inspect main branch and current entry points; record failures/status.
P1 revenue: test existing writing/research page and workbench, create two samples, prepare official-contact prospect list, begin authorised manual outreach.
P2 navigation: build a compact landing page linking to existing sections rather than duplicating every feature.
P3 catalogue: normalize product metadata and show lifecycle/evidence labels; archive only after dependency review.
P4 human presentation: test each stage independently, then end-to-end Q&A and lip-sync.
P5 scale only after pilot usability, security, conversion and reliability evidence supports expansion.

## 9. Release and rollback
This roadmap is documentation only; it does not implement UI, change hosting, configure external services, send outreach, or generate revenue. Split implementation into small PRs with targeted tests. Keep the production entry point until replacement passes acceptance criteria; release reversibly and verify the live URL.
