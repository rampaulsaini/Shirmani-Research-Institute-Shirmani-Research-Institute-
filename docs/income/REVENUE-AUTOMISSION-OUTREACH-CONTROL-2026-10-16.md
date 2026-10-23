# SRI Revenue Automission — Outreach Control & Evidence Runbook
**Version:** 1.0  
**Prepared:** 2026-10-16  
**Status:** PROPOSED / REVIEW REQUIRED — not deployed; no messages sent; no revenue verified.

## 1. Immediate commercial scope
Sell only currently supportable services until the delivery team and capacity are evidenced:
1. Hindi/English writing and editing — up to 800 words — proposed pilot ₹999.
2. Research summary — up to 1,200 words, up to 5 supplied/approved sources — proposed pilot ₹1,999.
3. Website/blog content pack — 3 pieces, up to 600 words each — proposed pilot ₹2,999.

These are proposed pilot prices, not confirmed public prices. Before publication, reconcile existing public pages that may show ₹499/₹999/₹1,499. Quote only after scope, language, source access, word count, deadline, revision count, rights, and payment terms are agreed in writing. Do not promise legal, medical, financial, scientific peer-review, or guaranteed SEO outcomes.

## 2. Lead-to-cash state machine
`DISCOVERED → QUALIFIED → DRAFT_READY → HUMAN_APPROVED → SENT → REPLIED → BRIEF_CONFIRMED → QUOTED → ACCEPTED → PAID_CONFIRMED → IN_DELIVERY → QA_PASSED → DELIVERED → CLOSED`

Terminal/exception states: `DO_NOT_CONTACT`, `BOUNCED`, `NO_RESPONSE`, `DECLINED`, `PAYMENT_DISPUTED`, `BLOCKED_EVIDENCE`.

Rules:
- No automatic send. `HUMAN_APPROVED` must record approver, timestamp, exact recipient, subject, body hash, and approved claims.
- Never infer that a message was sent from a draft, queue entry, or provider connection.
- Never infer payment from an invoice, promise, screenshot without context, or checkout link; require a verified transaction record.
- Never mark delivery complete until the output, QA checklist, and client handoff evidence are linked.
- Respect unsubscribe/opt-out immediately; suppress future outreach to that contact.
- Use public official contact channels only where relevant to the recipient's remit. Collect only business contact data needed for the outreach purpose; obey applicable laws and platform terms.
- Do not scrape private data, bypass rate limits, mass-message, or claim affiliation/endorsement that is not documented.

## 3. Daily Automission cadence (Asia/Kolkata)
1. **08:30 — Evidence/operations preflight:** verify public offer copy, repository release status, enquiry form, working contact route, payment instructions, and delivery capacity. If any critical check fails, pause outreach.
2. **09:00 — Lead discovery:** research a small, relevant batch from official institutional/company websites; save source URL, organization, public contact route, role fit, reason for relevance, country, and discovery date.
3. **10:00 — Qualification:** score each lead on fit (0–2), active need evidence (0–2), official contact validity (0–2), ability to serve (0–2), and compliance/consent risk (0–2). Human review required; no contact if official route or relevance is unclear.
4. **11:00 — Draft preparation:** generate one concise, personalized message with a specific low-risk pilot offer, sample/demo link only if it actually works, price marked as proposed/confirmed accurately, and a clear opt-out.
5. **Before sending — human approval gate:** verify every factual claim, recipient, current offer, sample link, capacity, and legal basis. Send manually or through an explicitly authorized, connected channel only after approval.
6. **15:00 — Follow-up review:** follow up at most once after 5–7 business days if lawful, relevant, and no opt-out; stop after decline, bounce, or opt-out.
7. **17:00 — Measurement and learning:** update the CRM from evidence, record objections and conversion, inspect delivery capacity, and produce a daily summary. Do not invent missing counts.

If no automation scheduler is actually connected, this is a schedule specification only; do not report a scheduled job as active.

## 4. Lead record schema
Required fields:
- `lead_id` (stable internal ID)
- `organization`, `country`, `sector`, `official_source_url`, `contact_route`
- `relevance_reason`, `need_evidence`, `discovered_at`
- `qualification_score`, `reviewer`, `contact_permission_basis`
- `state`, `next_action_at`, `opt_out`
- `message_subject`, `message_body_hash`, `approval_by`, `approval_at`
- `sent_at`, `provider_message_id`, `reply_at`
- `scope_confirmed_at`, `quote_id`, `quote_amount`, `currency`
- `payment_status`, `payment_evidence_ref`, `delivery_evidence_ref`, `qa_evidence_ref`
- `actual_revenue`, `refund_amount`, `notes`

Do not store passwords, API keys, payment-card data, or unnecessary personal information in the lead tracker.

## 5. Suggested outreach copy — draft only
**Subject:** Hindi/English research and content support — small pilot

Hello [Name/Team],

I’m contacting you on behalf of Shirmani Research Institute because your official page describes work in [specific, verified area]. We provide Hindi/English writing, research summaries based on cited sources, and website/blog content.

If useful, we can scope a small pilot first:
- Writing/editing: up to 800 words — proposed ₹999
- Research summary: up to 1,200 words, up to 5 sources — proposed ₹1,999
- Three website/blog pieces, up to 600 words each — proposed ₹2,999

These are pilot proposals, subject to confirming scope, deadline, source availability, revisions, and current pricing. We will not begin until deliverables and payment terms are agreed in writing. If this is not relevant, please let me know and I will not follow up.

Regards,  
Shirmani Research Institute  
[Verified official website/contact details]

Before sending: replace every bracketed field, verify the institution's official source, verify current public prices, ensure capacity, and have a human approve the exact final message. Do not send this generic draft unchanged.

## 6. Metrics and formulas
- Qualified leads = leads passing human qualification.
- Approval rate = approved drafts / drafts reviewed.
- Delivery rate = provider-confirmed sent messages / approved sends.
- Reply rate = unique replies / provider-confirmed delivered messages.
- Positive reply rate = positive replies / unique replies.
- Quote acceptance rate = accepted quotes / quotes issued.
- Paid conversion = verified paid orders / quotes issued.
- Realized revenue = verified receipts − refunds; report currency and period.
- On-time delivery = QA-passed deliveries on/before deadline / deliveries due.
- Gross contribution = realized revenue − directly attributable delivery costs (only where costs are recorded).

Report numerator, denominator, period, evidence reference, and missing data. Zero observations must be shown as 0; unavailable observations as UNKNOWN, never silently treated as zero.

## 7. Initial 14-day experiment
- Day 1: reconcile pricing, test the enquiry path, validate 3 samples, define capacity and payment evidence.
- Days 2–3: build 20 relevant leads from official sources; human-review every record.
- Days 4–8: send up to 5 approved, personalized messages per business day; keep drafts/sends separate.
- Days 9–12: one eligible follow-up; answer replies and issue scoped quotes.
- Days 13–14: audit evidence, measure funnel and delivery capacity, and decide whether to expand.
Targets are experiment limits, not forecasts or promises. No claim of sales or income until verified records exist.

## 8. Global expansion guardrails
The long-term goal may cover organizations in 195 countries and government/private sectors, but begin with a controlled pilot and expand by country only after local outreach/privacy rules, language, time zone, procurement rules, tax/payment availability, and delivery capacity are reviewed. Do not represent global coverage as currently operational.

## 9. Acceptance checklist
- [ ] Public prices reconciled across the site and repository.
- [ ] Enquiry form and response route tested end-to-end.
- [ ] At least one real deliverable sample checked for accuracy, citations, language, and rights.
- [ ] Lead schema and opt-out suppression tested.
- [ ] Human approval is mandatory before sending.
- [ ] Send, reply, quote, payment, delivery, and refund evidence remain separate.
- [ ] Dashboard uses UNKNOWN for missing data and never manufactures revenue.
- [ ] Scheduler, email, WhatsApp, payment, and CRM integrations are marked NOT CONNECTED until actual tests prove otherwise.
- [ ] Protected branch and all existing verification gates remain unchanged.

## 10. Current evidence boundary
This document is a proposed operating runbook. It does not establish that the workflow is deployed, any scheduled automation is active, email/WhatsApp integrations are connected, any prospect has been contacted, any payment has cleared, or any revenue has been earned.
