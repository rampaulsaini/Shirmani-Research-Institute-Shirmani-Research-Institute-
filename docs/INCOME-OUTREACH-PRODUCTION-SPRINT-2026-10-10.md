# SHIRMANI RESEARCH INSTITUTE — Income & Product-Production Sprint
**Date:** 2026-10-10  
**Status:** Operational plan and reusable outreach assets; no outreach or sale is claimed by this document.

## 1. What exists now (repository evidence)
- Public-facing service offer: `writing-research-service-offer.html`
- Customer brief builder: `writing-research-enquiry.html`
- Public product catalogue/showroom shell: `supreme-showroom.html`
- Browser demonstration: `voice-to-presentation-studio.html`
- Production-first operating principles: `CONTINUATION-AUTO-STATE.md`

A page, configured product record, or workflow run is not by itself a finished product, an independently verified result, an outbound contact, or revenue. Track those separately.

## 2. Immediate paid service: start with the deliverables that can be supplied today
1. Hindi/English proofreading and clarity editing.
2. Short article, product copy, and website/blog content.
3. Source-organized research summaries with links and uncertainty notes.
4. Research-to-presentation outline (outline only unless slide design is explicitly included).

The existing service page lists **proposed pilot rates**: ₹299, ₹599+, ₹999+, and ₹799. They are not evidence of market validation or sales. Confirm the actual file, word count, sources, deadline, revisions, taxes (if applicable), and payment terms before accepting an order.

## 3. Lead qualification and outreach chain
`Candidate → official source checked → relevant need identified → tailored message approved → sent through an authorized channel → reply logged → scope/quote agreed → payment confirmed → production → QC → delivery → feedback`

Allowed statuses:
- `DISCOVERED`: organization/contact page found.
- `OFFICIAL_SOURCE_CHECKED`: official domain and contact route checked.
- `DRAFT_READY`: tailored message prepared but not sent.
- `SENT`: outbound message actually sent; record date and channel.
- `REPLIED`, `QUALIFIED`, `QUOTE_SENT`, `WON`, `LOST`, `FOLLOW_UP`.
- `PAID`: payment evidence recorded.
- `DELIVERED`: agreed files delivered.
- `REVIEW_RECEIVED`: genuine customer feedback captured with permission.

Never mark `SENT`, `PAID`, `VERIFIED`, or `DELIVERED` from a workflow run alone. Do not scrape private contact details, bypass access controls, or mass-spam. Use publicly listed official business contacts, follow the recipient's contact policy, send relevant low-volume messages, and honor opt-outs. WhatsApp messages require an available authorized account and must not be represented as sent automatically by this static website.

## 4. Priority lead segments (first pilot)
Begin with 20 carefully selected prospects, not a blanket claim of contacting 195 countries:
- 5 small businesses / web agencies that visibly publish Hindi or English content.
- 5 research, education, or science communication groups with a public editorial/contact route.
- 5 nonprofits or nature-conservation organizations needing accessible bilingual explainers.
- 5 creators, podcasts, or digital-product sellers who publicly invite business enquiries.

For each prospect, record: organization, official website, exact official contact-page URL, fit/reason, requested service, source-check date, contact policy, message status, next action, and evidence link. Only add a contact after its official source is checked.

## 5. Reusable outreach messages

### Email — concise, personalized
**Subject:** Hindi/English content support for [Organization]

Hello [Name/Team],

I’m contacting you from SHIRMANI RESEARCH INSTITUTE. We offer Hindi/English writing and editing, source-organized research summaries, and website/blog content.

I noticed [specific, verifiable reason this service may be relevant]. If useful, I can propose a small, clearly scoped pilot: [one deliverable] with agreed word count, source requirements, deadline, revision limit, and fixed price before work begins.

Would this be relevant to your current needs? If not, no follow-up is needed.

Regards,  
SHIRMANI RESEARCH INSTITUTE  
Service details: https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/writing-research-service-offer.html

### WhatsApp — only where business enquiries are invited
Hello. I’m reaching out from SHIRMANI RESEARCH INSTITUTE. We provide Hindi/English writing, editing, source-organized research summaries, and website/blog content. If your team needs this, I can send a short enquiry brief and agree the deliverables, deadline, and price before starting. Service details: https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/writing-research-service-offer.html. If this is not relevant, I won’t follow up.

### Follow-up
Hello [Name/Team], I’m following up once on my note about [specific deliverable]. If it is not a current need, please disregard and I will not send further follow-ups. Thank you.

## 6. Product factory: production before promotion
Use this four-stage release chain for every product:
1. **Institute / discovery:** user problem, intended audience, alternatives, requirements, and evidence.
2. **Factory / production:** a working module or downloadable deliverable, versioned source, usage guide, and a reproducible demo.
3. **QC / release gate:** functional tests, security/privacy review, license and asset checks, limitations, support scope, and rollback path.
4. **Showroom / sale:** accurate description, price, demo video or honest demo status, product-specific screenshots, passport/QR, support and refund terms where applicable.

A product must not be advertised as production-ready merely because a catalogue entry or screenshot exists. Use statuses such as `CONCEPT`, `PROTOTYPE`, `DEMO_READY`, `QC_PENDING`, `RELEASED`, and `RETIRED`. Display only claims supported by a reproducible artifact.

### Minimum product passport
- Stable product ID and version.
- Problem solved, intended users, supported inputs/outputs.
- Features that actually work; known limitations.
- Demo URL and dated screenshot (or explicit “demo not available yet”).
- Installation/use guide, accessibility notes, license/asset provenance.
- QC test results and release decision.
- Price/currency, included deliverables, update policy, support/refund terms.
- QR code pointing to the canonical passport URL, not to a fabricated QC claim.

## 7. Security-first backlog (practical, not hype)
1. Inventory public routes, workflows, dependencies, secrets references, and third-party integrations.
2. Confirm least-privilege GitHub permissions; pin actions to reviewed immutable references where practical; protect the default branch and review workflow changes.
3. Scan dependencies and secret exposure; rotate any credential that may have been committed. Never place API keys in HTML, public repositories, logs, or generated artifacts.
4. Treat all user content, URLs, uploaded files, and generated content as untrusted; validate inputs and escape output.
5. Add automated lint/build/tests and dependency/security checks; preserve logs and artifacts with retention limits.
6. Review privacy, consent, copyright, voice/face authorization, and data deletion before launching AI voice/avatar or social features.
7. Keep payment, email, and WhatsApp integrations disabled until credentials, consent, provider setup, and end-to-end tests are complete.

“Ethical hacking” means authorized testing of owned systems or systems with written permission. Do not probe third-party systems without authorization.

## 8. Measurement dashboard (weekly)
Track counts with evidence links:
- prospects discovered / official sources checked / relevant drafts prepared / messages actually sent
- replies / qualified leads / quotes / orders / confirmed payments / deliveries / genuine reviews
- products with working demo / guide / screenshot / passport / completed QC / released to showroom
- build and security checks passed / failed / unresolved critical findings
- customer-reported issues fixed and release versions published

Baseline for this sprint: **not yet measured here**. Do not invent a starting count or report income until payment evidence is recorded.

## 9. First 7-day execution target
- Day 1: inspect existing service page and ensure all links work; finalize one sample writing/research deliverable.
- Day 2: assemble 20 source-checked prospects and personalize 10 messages.
- Day 3: send up to 5–10 relevant messages through authorized official channels; record evidence.
- Day 4: publish one honest portfolio sample with source notes and clear scope.
- Day 5: follow up only where appropriate; prepare quotes for replies.
- Day 6: implement one small, real product improvement and attach tests/screenshots.
- Day 7: report actual funnel metrics, blockers, product artifacts, and next actions.

These are targets, not completed outcomes or guaranteed earnings.
