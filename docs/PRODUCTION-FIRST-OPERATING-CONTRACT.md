# SHIRMANI — Production-First Operating Contract
Updated: 2026-10-10

## Purpose
Turn repository work into visible, usable deliverables and a measurable path to paid Hindi/English writing and research work. A workflow run is not itself a product, a sale, or proof of independent verification.

## Four-stage production chain
1. **Institute / Research** — record a specific customer problem, intended user, comparable solutions, source links, and a testable product hypothesis.
2. **Factory / Build** — produce an executable module or complete customer deliverable, not a name-only catalogue entry. Include README/usage instructions and sample input/output.
3. **QC / Gate** — run relevant automated checks, record pass/fail and evidence; assign a QC code only after checks run. Keep security review and independent verification distinct.
4. **Showroom / Dispatch** — publish only a working demo or clearly labelled prototype, accurate description, usage guide, version, price/offer (if set), support terms, and purchase/enquiry route. Never imply a sale or dispatch without an actual transaction/dispatch record.

## Product release checklist
- [ ] Unique product ID, name, category, version and owner
- [ ] User problem, intended use, limitations and supported inputs/outputs
- [ ] Working implementation committed to repository
- [ ] Runnable demo or reproducible test-drive instructions
- [ ] Product-specific screenshot/visual; no generic image represented as a real product screenshot
- [ ] Short image caption and QR linking to a stable product passport / full documentation
- [ ] Usage guide, privacy/security notes, dependencies and accessibility notes
- [ ] Automated tests and recorded results
- [ ] QC code, gate number and dispatch status derived from real run results
- [ ] Price, offer, refund/support terms only when deliberately configured
- [ ] Public reviews collected transparently; feedback informs a versioned improvement backlog
- [ ] Public listing links to the actual implementation and demo

## Product passport fields
`product_id, name, category, version, status, problem, audience, description, features, requirements, demo_url, source_url, usage_guide_url, screenshot_url, qr_target, price, offer, qc_code, gate, dispatch_status, test_summary, known_limits, privacy_notes, support_terms, review_url, last_updated`

Use `prototype`, `in_progress`, `qc_passed`, `published`, `withdrawn` as lifecycle states. Do not promote a product to `published` solely because a scheduled workflow succeeded. Empty fields should remain explicitly unset rather than filled with invented values.

## Security baseline before public release
- Never commit API keys, tokens, passwords, private customer data or voice/face source files without explicit authorization.
- Use least-privilege GitHub tokens and repository permissions; pin third-party Actions to reviewed immutable commit SHAs where feasible.
- Treat issue text, pull-request content, uploaded files and external web pages as untrusted input to automation.
- Do not run untrusted pull-request code with privileged secrets.
- Add dependency and secret scanning, input validation, rate limits, audit logs and a documented incident/rollback path.
- Only test systems for which the institute has explicit authorization; no unauthorized access, credential harvesting, stealth, persistence or destructive tests.
- Do not connect a voice/face clone or send outbound messages until the person/account is authorized and the channel is configured.

## Immediate income lane: Writing & Research
Current offer is limited to Hindi/English writing, editing, website/blog copy, source-organized research summaries and presentation outlines. Existing public service page lists *proposed pilot prices* (not evidence of sales):
- Proofreading/clarity edit up to 1,000 words: ₹299 proposed
- 600–900 word article/product copy: from ₹599 proposed
- Research brief up to 3 pages with source links: from ₹999 proposed
- 8–10 slide research/presentation outline: ₹799 proposed

Before accepting a job, confirm in writing: customer objective, topic, audience, language, word/page limit, supplied sources, deadline, deliverables, revision count, final price, payment milestones and rights/attribution. Start only after both sides agree. Do not promise unsupported research, fabricated citations, guaranteed outcomes or work that violates academic integrity.

### Outreach protocol
1. Build a small, relevant list of publicly listed official business contact channels for organisations whose needs match a specific writing/research offer.
2. Record organisation, official source URL, public contact route, fit rationale, date checked, outreach status and next follow-up date.
3. Send a personalised, truthful message only through an authorised channel; respect consent, unsubscribe/opt-out and platform rules. No mass unsolicited WhatsApp or scraped personal addresses.
4. Track `drafted → approved → sent → replied → scoped → quoted → accepted → paid → delivered`. Only mark sent when the channel confirms sending; only mark paid when payment is actually confirmed.
5. Start with a small pilot batch and measure replies, qualified enquiries, accepted quotes, paid work, delivery time and client feedback. Do not report projected amounts as revenue.

### Outreach message (draft; not sent)
**Subject:** Hindi/English writing and source-organised research support

Hello [Name/Team],

I’m contacting you from SHIRMANI Research Institute to offer focused Hindi/English writing and research support for [specific, relevant need]. Possible deliverables include a concise research brief with source links, website/blog copy, product descriptions, or a presentation outline.

If this is relevant, please share the topic, intended audience, preferred language, scope and deadline. I will reply with a written deliverables list, proposed price and timeline before any work begins. No commitment is required.

Regards,  
SHIRMANI Research Institute  
[Public service page] · [Enquiry route]

## Weekly measurable scorecard
Report counts, not inflated percentages:
- Product ideas researched
- Modules actually implemented
- Demos that run successfully
- QC checks executed / passed / failed
- Product passports and screenshots published
- Listings published with working demo and enquiry/purchase route
- Relevant organisations researched / messages approved / messages actually sent
- Replies / qualified enquiries / quotes accepted
- Payments received (amount and date only when evidenced)
- Deliverables completed and customer feedback received

## Current implementation boundary
This file defines an operating contract and release checklist; it does not claim the entire platform is secure, that all products exist, that 5-minute jobs always succeed, that 195-country outreach has happened, or that any income has been earned. Record actual results from repository commits, workflow logs, live demos and payment records.
