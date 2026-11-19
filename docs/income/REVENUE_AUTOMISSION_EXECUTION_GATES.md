# Revenue Automission: Evidence-Gated Execution Plan

**Status:** Proposed operating specification; not evidence of sales, outreach, payment, delivery, or revenue.  
**Last reviewed:** 2026-10-16  
**Owner approval:** Pending  
**Production activation:** Not authorized until the gates below pass.

## 1. Immediate business objective

Convert the currently identified service capability—Hindi/English writing, research summaries, and website/blog content—into a measurable, auditable first-client workflow. Build larger product lines only after demand, delivery capacity, cost, and customer outcomes are demonstrated.

This plan deliberately separates a blocker from a business outcome. A configured checklist, draft message, public page, or automation run is not a lead contacted, sale, payment, or earned revenue.

## 2. Pricing conflict: preserve, do not silently normalize

Repository review reported the following distinct proposed menus:

| Surface | Proposed amounts | Known issue |
|---|---:|---|
| Public `services-writing-research.html` | ₹499 / ₹999 / ₹1,499 | Proposed starting rates; scope differs from other menus |
| `docs/commerce/FIRST-CLIENT-OFFER-OUTREACH-PACK.md` | ₹799 / ₹1,999 / ₹2,999 | Different scope family |
| `revenue/README.md` | ₹499 / ₹999 / ₹1,499 | Different scope definitions |
| `showroom/prospect-pipeline-desk.html` | ₹999 / ₹1,999 / ₹2,999 | Proposal anchors, not approved canonical prices |

These figures are **unapproved proposals**, not a unified price list. Do not change public prices, send a price-bearing offer, or represent any amount as approved until the owner signs off on a scope-by-scope worksheet.

### Required price worksheet

For every package, record:
- exact deliverables, word/length limits, included source count, revision count, exclusions, and acceptance criteria;
- estimated and observed labor hours by task;
- direct tools/provider costs and overhead allocation;
- payment fees, refunds/chargebacks allowance, and applicable tax treatment confirmed by a qualified adviser;
- target gross margin and capacity per week;
- turnaround time and rush-work conditions;
- calculated minimum viable price, proposed selling price, worksheet version, approver, approval timestamp.

Suggested calculation (not tax or accounting advice):

`minimum price = (labor cost + allocated overhead + direct costs + payment costs + risk allowance) / (1 - target gross-margin rate)`

Do not calculate a final price when any required input is unknown. Mark it `BLOCKED_INPUTS`; never substitute invented assumptions.

## 3. First-client workflow and evidence states

Use one auditable record per opportunity, with timestamps and links to supporting evidence.

1. `DRAFT` — offer or prospect record prepared; not sent.
2. `OWNER_APPROVAL_PENDING` — price, scope, recipient, and channel await approval.
3. `APPROVED_TO_CONTACT` — explicit approval recorded for this recipient and message.
4. `SENT_CONFIRMED` — provider event or sent-message record proves dispatch.
5. `DELIVERED` — delivery evidence exists, when the provider exposes it.
6. `RESPONSE_RECEIVED` — an actual response is linked.
7. `SCOPE_CONFIRMED` — customer and owner agree in writing on deliverables, schedule, price, revisions, and exclusions.
8. `PAYMENT_PENDING` — invoice/payment request exists; this is not payment.
9. `PAYMENT_CONFIRMED` — provider/bank record confirms receipt; store a reference, not secrets.
10. `IN_PROGRESS` — work starts only after required payment/authorization and scope confirmation.
11. `DELIVERED_TO_CUSTOMER` — dated delivery link or receipt exists.
12. `ACCEPTED` — customer acceptance evidence exists, or a documented dispute/refund state applies.
13. `REVENUE_RECONCILED` — payment, refunds, fees, tax/accounting treatment, and delivery are reconciled by an authorized owner.

A stage transition requires its evidence reference. No automatic transition may infer a response, payment, acceptance, or revenue from a draft, page view, email open, workflow success, or repository change.

## 4. Outreach automation: safe-by-default

- Begin with a human-reviewed prospect list and a small, relevant pilot; do not mass-email 195 countries or harvest personal contact data.
- Prefer publicly designated institutional contact channels and comply with applicable anti-spam, privacy, platform, and country-specific rules.
- Keep source URL, institution, role-relevance rationale, contact channel, date checked, and opt-out/suppression status.
- Generate drafts only by default. Sending requires an explicit per-campaign or per-recipient owner-approved gate, plus valid sender configuration and suppression checks.
- Never send WhatsApp or email messages, submit bids, purchase services, alter payment settings, or make commitments without the appropriate authorization.
- Provide clear sender identity, relevant purpose, accurate capability claims, and a simple opt-out. Honor opt-outs immediately.
- Rate-limit, deduplicate, log provider message IDs, and stop the campaign on authentication errors, complaints, unexpected volume, or data-quality failures.
- Keep credentials in the provider's secret store; never commit API keys, passwords, session tokens, or private customer data.

## 5. Metrics that are allowed to be reported

Report counts only from evidence-backed records:
- prospects researched;
- drafts prepared;
- messages approved;
- messages sent and delivery-confirmed;
- replies received;
- qualified enquiries;
- scopes approved;
- invoices issued;
- payments confirmed;
- work delivered and accepted;
- gross receipts, refunds, fees, and net receipts reconciled.

For each metric, show the period, source query or ledger view, numerator, denominator where applicable, and last refresh. If no evidence exists, report `NOT VERIFIED`, not zero and not success. Revenue must remain unclaimed until the reconciliation gate passes.

## 6. Public menu and enquiry journey release gates

Before treating the public storefront as ready:
- verify the deployed page at its actual public URL (not only the repository file);
- test mobile and desktop layout, accessibility basics, all internal/external links, and enquiry submission;
- submit a test enquiry and confirm receipt in the configured destination;
- verify privacy notice, data minimization, consent/opt-out handling, terms, scope, delivery, revisions, refund, tax/invoice, and payment instructions;
- ensure every visible price matches an owner-approved worksheet and scope;
- label proposed/demo content clearly and prevent demo orders from being mistaken for real transactions.

A repository commit does not prove deployment. A successful deployment does not prove enquiries, sales, or revenue.

## 7. Human-presentation system: architecture and verification

Build incrementally as a separate product capability; do not describe it as complete before end-to-end tests pass.

`Voice input → speech recognition → context/intent → evidence gate → response → authorized voice output → authorized avatar/photo → lip-sync → live Q&A → audit`

Required evidence labels:
- `VERIFIED`: the specific claim has sufficient direct test or source evidence.
- `SOURCE_BASED`: sourced information is shown, but independent verification is incomplete.
- `PHILOSOPHICAL_IDENTITY`: personal philosophy or self-description, not presented as a scientific finding.
- `INSUFFICIENT_EVIDENCE`: system says evidence is insufficient and does not invent an answer.

Minimum test gates:
- speech recognition across supported languages/noise levels;
- intent/context and uncertainty handling;
- factual response with traceable sources and citation checks;
- abstention on unknown questions;
- authorized voice provider authentication and output;
- consent/authorization for face and voice assets;
- facial movement, gaze, timing, lip-sync, and latency;
- live Q&A interruption/error recovery;
- privacy, data retention, deletion, access controls, and audit logs;
- regression tests for respectful, non-discriminatory communication.

Use the owner's already supplied HeyGen reference as a reference point; do not repeatedly ask for the same photo/video. This reference alone does not prove integration, live Q&A, voice authorization, or successful end-to-end behavior. Record each test's build/version, input, expected result, observed result, timestamp, and evidence link.

## 8. Security and continuous improvement

- Threat-model authentication, authorization, secrets, prompt injection, upload handling, API abuse, tenant isolation, backups, and incident response.
- Apply least privilege, dependency scanning, secret scanning, branch protection, review gates, and tested recovery procedures.
- Treat uploaded documents, external pages, and customer prompts as untrusted input.
- Use opt-in data collection, clear retention limits, access/deletion controls, and documented consent for voice/face likeness.
- Run improvement loops on measured failure cases; never label the platform “fully secure,” “uncopyable,” or “unlimited.” State tested scope and residual risks honestly.
- Large-scale targets (195 countries, 8.5 billion users, global library, studio, social network) are long-term ambitions, not current capacity claims. Validate one useful, affordable service with real customers before expanding.

## 9. Owner decision checklist

The owner must provide or approve:
- [ ] package scopes and acceptance criteria;
- [ ] actual labor-cost basis, overhead, payment fees, tax treatment, margin, and delivery capacity;
- [ ] one canonical price per package and effective date;
- [ ] sender identity, sending domain/provider, permitted channels, and outreach scope;
- [ ] privacy/retention/opt-out policy and applicable terms;
- [ ] payment and refund process;
- [ ] public deployment URL and a successful test-enquiry record;
- [ ] approved voice/avatar assets and provider permissions;
- [ ] release decision after tests and security review.

Until these decisions and evidence exist, retain the pricing blocker and keep outreach in draft-only mode.

## 10. Current status snapshot

As of 2026-10-16, based on the reported repository review:
- pricing conflict: **OPEN / BLOCKED**;
- actual labor, overhead, payment fees, tax treatment, margin, capacity: **NOT PROVIDED**;
- owner pricing approval: **PENDING**;
- live Pages deployment: **UNVERIFIED**;
- end-to-end HeyGen voice/lip-sync/live-Q&A integration: **NOT VERIFIED**;
- sent outreach, customer contact, sales, payment, delivery, earned revenue: **NO EVIDENCE PROVIDED**.

This status must be updated only from verifiable artifacts. Do not infer progress from the existence of this document.
