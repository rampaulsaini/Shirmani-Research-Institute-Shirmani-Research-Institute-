# Shirmani Product Showroom — Product Passport & Release Standard

Status: proposed implementation contract; not evidence that products, demos, sales, integrations, or revenue already exist.

## Purpose
Give every published digital tool a distinct, understandable identity and a consistent, testable path from preview to purchase and support. The public showroom must explain what exists today, what is a prototype, and what remains planned.

## Product states
- `IDEA`: concept only; not purchasable.
- `PROTOTYPE`: demonstrable build with known limitations.
- `TESTED`: documented tests passed in a stated environment.
- `PUBLISHED`: release checklist passed; public listing is available.
- `PAUSED`: temporarily unavailable or under review.
- `RETIRED`: not for new purchases; support/transition policy shown.

Never label a product VERIFIED, production-ready, live, integrated, or revenue-generating without dated evidence supporting that exact claim.

## Required product passport
Each product record must include:
- Stable product ID, final public name, category, version, owner, status and last-updated date.
- Plain-language one-sentence purpose; intended audience; use cases; limitations; accessibility and language support.
- Feature list, requirements, supported devices/formats, privacy/data handling, security notes and support route.
- Pricing currency, one-time/subscription/service distinction, what is included, refund/cancellation terms, and any introductory offer with expiry.
- Test evidence: test ID, environment, date, result, known failures and reviewer.
- Demo URL and duration, quick-start guide, full documentation URL, screenshots, changelog and QR destination.
- Contact/feedback channel and review moderation policy.

## Public product card
1. Product-specific image/thumbnail with consistent safe margins and legible typography.
2. Institute mark at the top; product name and version; concise benefit statement on the image.
3. QR code in the top-right only when a tested destination URL exists. Encode a stable HTTPS product-passport URL, not raw private data. Test QR scan on mobile before publication.
4. Visible status badge and price/“request a quote” label. Never imply a free trial, offer, or purchase flow exists unless it works.
5. Separate links for demo, guide, details, and purchase/enquiry. Do not make a static image pretend to be an interactive demo.
6. Text alternative and a mobile-first layout; image compression and responsive scaling.

## Demo and screenshot requirements
- A real screen recording or clearly labelled prototype walkthrough, showing setup, a representative task, output, limitations, and next steps.
- VIP/feature screenshots must come from the actual product or be explicitly marked as concept mockups.
- Do not fabricate customer logos, reviews, ratings, certifications, performance claims, or UI screenshots.
- For each release, run a QR scan test, link test, mobile viewport check, image/text legibility check, and demo-to-documentation consistency check.

## Voice and live-presentation chain
Voice input → permission/consent check → speech recognition → intent/context → reasoning → evidence gate → response → authorized voice output → face/avatar → lip-sync → presentation → audit.
- Use only the user's own voice/likeness or a voice/likeness for which documented authorization exists.
- Provide disclosure when an avatar or synthetic voice is used; do not imply a generated presentation is a real live person.
- Keep evidence states distinct: `VERIFIED`, `SOURCE-BASED`, `PHILOSOPHICAL / IDENTITY`, `INSUFFICIENT EVIDENCE`.
- If evidence is insufficient, say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
- Record test results and errors without retaining unnecessary sensitive voice, face, or conversation data.

## Ethical outreach and sales
- Contact only official, verified business addresses or opted-in contacts relevant to the offer.
- Respect applicable law, provider terms, consent, opt-outs, rate limits and suppression lists. No bulk unsolicited messaging, address harvesting, or deceptive personalization.
- Use a human-reviewed first-contact message, accurate product claims, a working demo, transparent pricing and a clear opt-out.
- Log only authorized outbound events and provider confirmations. A prepared draft is not a sent email; a sent email is not a sale.
- Payment collection must use a legitimate payment provider and show terms before checkout. Never store card credentials directly.

## Measurable release gates
A product may move to `PUBLISHED` only when all applicable checks pass:
- [ ] Product identity and plain-language description reviewed.
- [ ] Actual build/demo available, or listing explicitly says “concept/prototype”.
- [ ] Product passport and guide accessible.
- [ ] Image is genuine or clearly labelled mockup; alt text present.
- [ ] QR destination exists and scans correctly on mobile.
- [ ] Price, deliverables, timing, support and refund terms are explicit.
- [ ] Privacy/security review completed for data collected.
- [ ] Functional tests and known limitations published.
- [ ] Enquiry/purchase path tested end-to-end, including failure states.
- [ ] Analytics distinguish impressions, clicks, qualified enquiries, proposals, paid orders, refunds and net revenue.

## Rollout: do not claim 5,000 products are complete until audited
1. Establish a catalogue schema and import only real, identifiable assets.
2. Pilot 10 products; require complete passports, demos, screenshots and release evidence.
3. Review usability, correctness, accessibility and conversion funnel.
4. Expand in batches (for example 50, then 250, then 1,000); block publication of incomplete records.
5. Scale toward 5,000 only as records pass the same gates. Sharding and search indexing are engineering tasks, not proof that 5,000 concrete products exist.

## Near-term income experiment: Hindi/English writing and research
Offer only services that can currently be delivered:
- Hindi/English article, blog or website copy.
- Research summary with linked sources and a clear evidence/uncertainty section.
- Editing, translation or plain-language explanation, scoped before work begins.

Every enquiry should capture: customer objective, topic, language, word count, deadline, source links, budget and preferred contact. Reply with a written scope, price, delivery date, revision count and payment terms. Start only after customer approval. Track enquiries → qualified leads → proposals → accepted proposals → paid orders → delivered work → feedback. Do not report revenue until payment is confirmed.

## Initial dashboard metrics
- Catalogue completeness = records passing all required passport fields / published records.
- Demo coverage = published records with tested demos / published records.
- QR pass rate = successfully scanned tested QR codes / QR codes tested.
- Enquiry conversion = qualified enquiries / relevant listing visits.
- Proposal win rate = accepted proposals / proposals sent.
- Paid conversion = paid orders / qualified enquiries.
- Net revenue = confirmed receipts minus refunds and applicable fees.
- Verification rate = independently evidenced passing checks / checks due.

Report numerator, denominator, date range and evidence source for every percentage. Missing telemetry must be shown as “not measured”, not zero or 100%.

## Security and change control
Keep credentials in approved secret storage, use least privilege, review dependency/workflow permissions, validate user input, rate-limit public endpoints, maintain backups and audit logs, and test rollback. Never place API keys, private customer data, or private QR destinations in public repository files.
