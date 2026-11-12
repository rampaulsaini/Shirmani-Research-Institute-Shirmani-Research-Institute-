# Automission: Revenue-First Writing & Research Pilot
**Prepared:** 2026-10-16  
**Status:** Operating plan / proposed pilot; not evidence of outreach, sales, or revenue.

## 1. Scope and guardrails
Start with the services currently available: Hindi/English editing, article or website/blog copy, and source-based research summaries. Do not market unbuilt AI products, claim 195-country outreach, or describe drafts as sent. The larger platform, studio, library, social network, voice/avatar system, and live Q&A remain separate engineering workstreams until tested.

All prices below are proposed pilot rates from the current canonical service menu, not market-validated prices:
- Editing/proofreading: up to 700 words — from ₹499.
- Article / website copy: up to 1,000 words — from ₹999.
- Source-based research brief: about 800–1,200 words, with 3–5 credible sources — from ₹1,499.

Final quote depends on scope, source complexity, language, deadline, and revision needs. Never begin paid work until the customer has accepted a written scope, deliverables, deadline, price, revision policy, and payment terms.

## 2. First-customer offer
**Offer:** “Hindi/English Research & Content Pilot”
1. Customer chooses one deliverable: edit a supplied draft, write one article/web page, or prepare a source-based brief.
2. Institute confirms scope and provides a written quote.
3. Customer approves the scope and payment terms in writing.
4. Work begins only after the agreed advance/payment condition is met.
5. Deliver the agreed file, source list where relevant, and one clearly defined revision round.
6. Ask for feedback; request permission separately before publishing a testimonial or using the work as a case study.

### Required enquiry fields
Customer / organisation; contact channel; goal; topic; language; word count; audience; intended use; source links/files; deadline; budget; requested deliverable; rights/confidentiality constraints.

## 3. Outreach sequence — human approval required
Target only relevant, publicly listed institutional contacts and use official contact channels. Verify the address from the institution's own website immediately before sending. Do not scrape private addresses, guess email patterns, or send bulk unsolicited messages. Respect opt-outs and applicable anti-spam/privacy rules.

1. Research one organisation and identify a concrete writing/research need from public evidence.
2. Record the official source URL and why the offer is relevant.
3. Draft a short, tailored email; a human checks recipient, claim accuracy, and relevance.
4. Send manually from an authorised account. A generated draft is not a sent message.
5. Follow up at most once after 5–7 business days, unless the recipient opts out or policy says otherwise.
6. Log response and next action; stop on opt-out or negative response.

### Email draft (do not send automatically)
**Subject:** Hindi/English research and content support for [organisation]

Hello [Name/Team],

I’m contacting you on behalf of Shirmani Research Institute. We offer scoped Hindi/English editing, article or website content, and source-based research summaries.

I noticed [specific, verifiable public item/need and official URL]. If useful, we can propose a small pilot deliverable with agreed scope, sources, deadline, revisions, and a written price before work begins.

Our proposed pilot rates start at ₹499 for editing up to 700 words, ₹999 for article/web copy up to 1,000 words, and ₹1,499 for a source-based research brief of approximately 800–1,200 words with 3–5 credible sources. Final pricing depends on scope.

Would a short sample scope or quote be useful? If this is not relevant, let me know and I will not follow up.

Regards,  
Shirmani Research Institute  
[approved contact details]  
[public service page]

**Before sending:** replace every bracketed field; verify the official contact and public source; ensure the price menu matches the current public page; include real sender/contact details. No fabricated affiliation, prior work, testimonials, or promised results.

## 4. Automission state machine
`IDEA → PROSPECT_RESEARCHED → CONTACT_VERIFIED → DRAFT_READY → HUMAN_APPROVED → SENT_CONFIRMED → REPLY_RECEIVED → QUALIFIED → SCOPE_SENT → SCOPE_ACCEPTED → PAYMENT_CONFIRMED → IN_PROGRESS → QA → DELIVERED → FEEDBACK_REQUESTED → CLOSED`

Exceptional states: `OPTED_OUT`, `NO_REPLY`, `NOT_QUALIFIED`, `PAYMENT_PENDING`, `BLOCKED`, `REFUND_OR_DISPUTE`.

Rules:
- State changes require an event timestamp and evidence (URL, message ID, written approval, invoice/payment reference, or delivery link as applicable).
- Never infer SENT from a draft, PAYMENT_CONFIRMED from an invoice, or DELIVERED from a generated file existing.
- No autonomous sending, payment collection, price changes, or binding scope acceptance without authorised human approval.
- Store only necessary business contact data; restrict access, set a retention period, and honour correction/deletion requests.
- Keep personal philosophical statements distinct from evidence-backed product claims.
- Every claim in research work gets a source or is labelled interpretation/uncertain; missing evidence cannot be marked verified.

## 5. Measurement dashboard
Record weekly, with a source for each number:
- prospects researched;
- official contacts verified;
- drafts prepared;
- messages actually sent;
- replies received;
- qualified enquiries;
- quotes sent;
- scopes accepted;
- invoices issued;
- payments confirmed;
- jobs delivered on time;
- revisions / refunds / complaints;
- customer feedback and repeat requests;
- gross receipts, refunds, direct costs, and net contribution.

**Starting baseline for this work session:** outreach sent 0; replies 0; accepted scopes 0; paid invoices 0; verified revenue ₹0. Update only from records. Do not use targets as actual results.

## 6. First 7-day experiment
- Day 1: reconcile the public price menu and verify the enquiry route on the deployed site.
- Day 2: choose 10 relevant organisations from public, official sources; record one evidence-backed reason each is relevant.
- Day 3: prepare 5 individually tailored drafts and have a human approve them.
- Days 4–5: send only approved messages manually; log sent evidence.
- Days 6–7: respond to enquiries, issue written scopes/quotes, and review funnel data.

Experiment targets (targets, not promises): 10 researched prospects; 5 approved drafts; 0–5 messages sent depending on verification and approval; all replies logged within one business day. Success means a clean, auditable funnel and qualified conversations—not guaranteed sales.

## 7. Definition of done for the pilot
- One canonical service price menu, consistent with the public page.
- Working enquiry path checked on mobile and desktop; any untested route is labelled NOT VERIFIED.
- Lead tracker has evidence-backed states and no sensitive unnecessary data.
- At least one reviewed sample deliverable exists before it is advertised as a sample.
- Every outreach action, quote, acceptance, delivery, and receipt is separately recorded.
- No claims of sales, revenue, live AI integration, or end-to-end testing without evidence.

## 8. Next engineering layers (not prerequisites for first sale)
After the service workflow is operating, build and test: (a) evidence-gated research and impartial-understanding audit; (b) versioned product showroom with real demo links and QC state; (c) voice/avatar pipeline with explicit consent and end-to-end test evidence; (d) secure CRM and email draft automation with human approval; (e) product update/feedback loop. Do not represent these as complete until their acceptance tests pass.
