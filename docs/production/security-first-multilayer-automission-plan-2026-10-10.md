# Security-First Multi-Layer Automission & Production Plan
**Date:** 2026-10-10  
**Status:** Implementation specification — not a claim that the runtime is already secured or autonomous.

## Mission
Prioritize useful production output while protecting the repository, users, product data, and customer communications. Verification is a gate on work products, not the only work performed. No external outreach, payment, sale, production deployment, or independent verification is claimed unless an auditable event proves it happened.

## Operating lanes (run in parallel where dependencies allow)

1. **Security & recovery lane** — least-privilege GitHub tokens, protected default branch, required reviews/checks, secret scanning, dependency review, pinned third-party actions, HTTPS, backup/restore drill, incident response, and audit log. Never place secrets in HTML, repository files, issue comments, or logs.
2. **Concrete product lane** — take one product at a time through Institute → Factory → QC/Gate → Showroom. Each record must point to a real runnable asset, not only a catalogue name.
3. **Customer experience lane** — product-specific screenshots, demo video or storyboard, usage guide, limitations, accessibility/mobile checks, QR to the product passport, version, support route, and customer feedback loop.
4. **Revenue lane** — begin with the currently deliverable services: Hindi/English writing, research summaries, and website/blog content. Build prospect lists only from official public sources; draft tailored messages for human review; send only through an authorized account after approval. No unsolicited bulk WhatsApp, scraped personal addresses, or invented endorsements.
5. **Voice/presentation lane** — prototype voice input, script, evidence state, browser speech, and visual preview; connect an external voice/avatar provider only with account authorization, explicit consent, and a tested integration. Never imply a photo preview is an animated avatar or a browser speech voice is a voice clone.
6. **Catalogue scale lane** — shard the catalogue by stable product IDs and category. Scale counts represent targets/records, not completed products. A product counts as concrete only when its runnable asset, guide, demo evidence, pricing state, and release state exist.

## Product state machine

`IDEA → RESEARCHED → SPECIFIED → BUILT → LOCAL_TESTED → QC_PASSED → PUBLISHED → OFFERED → ORDERED → DELIVERED → FEEDBACK → IMPROVEMENT`

- Failed gates return to the relevant build/test state with a named issue.
- `PUBLISHED` does not mean `SOLD`; `OFFERED` does not mean `ORDERED`.
- A price must be explicitly marked **proposed**, **published**, or **quoted**.
- Only mark `QC_PASSED` when the stated checks have evidence. Independent research verification is a separate state.

## Minimum product passport

- Stable product ID, name, version, category, intended user, problem solved.
- What works now, what does not work yet, prerequisites, privacy/data handling.
- Runnable demo URL and dated screenshots; MP4 demo URL when a real video exists.
- Step-by-step usage guide and expected result.
- Price status/currency, offer expiry if any, refund/support terms where applicable.
- QC checklist and result evidence; QR destination to the full passport.
- Customer review/rating, issue link, owner, next improvement, last-updated timestamp.

## Security gates before public production

- [ ] Protect default branch; require reviewed pull requests and passing checks.
- [ ] Enable secret scanning/push protection where available; rotate any exposed credential immediately.
- [ ] Review dependency and GitHub Actions permissions; grant minimum required `permissions:` per workflow and pin third-party actions to reviewed commit SHAs.
- [ ] Add dependency/security scanning appropriate to the actual stack and review findings; do not report a scan as passed until a run exists.
- [ ] Keep API keys, email credentials, payment secrets, voice-provider keys, and customer data out of static client-side files.
- [ ] Validate and encode user input; use a server-side backend for authentication, payments, orders, uploads, and persistent records.
- [ ] Test HTTPS, security headers, access control, rate limits, backup restoration, monitoring, and rollback on the real hosting/runtime.
- [ ] Record owner, timestamp, evidence link, severity, remediation, and retest result for each finding.

## Measurable work dashboard

Track counts from repository/runtime evidence, not optimistic estimates:

| Metric | Counting rule |
|---|---|
| Concrete products | Distinct product IDs with a runnable asset |
| Demo coverage | Concrete products with a working demo or clearly labeled storyboard |
| Visual coverage | Concrete products with product-specific screenshot(s) |
| Guide coverage | Concrete products with step-by-step usage instructions |
| QC pass | Products with a dated checklist and evidence |
| Public catalogue coverage | QC-passed products visible with accurate readiness/pricing state |
| Outreach sent | Messages confirmed by an authorized provider or sent-mail record |
| Replies / qualified leads | Actual responses matching documented criteria |
| Orders / revenue | Confirmed order and payment records only |
| Improvement closure | Feedback issues with a linked fix and retest |

Publish numerator, denominator, timestamp, and source for every percentage. Do not infer completed production from workflow-run counts or scheduled work units.

## First revenue sprint (7 days)

1. Prepare three examples: one Hindi/English website-copy sample, one research-summary sample with source ledger, and one blog/article sample.
2. Publish a clear service page with deliverables, boundaries, enquiry form, and proposed starter prices that are confirmed with the client before work.
3. Build a small, relevant prospect list from official organization websites; record organization, official URL, why the service fits, and a public contact channel.
4. Prepare personalized email drafts; manually review and send through an authorized account.
5. Track sends, replies, qualified enquiries, quotes, accepted scopes, delivery, and paid invoices. Report zero when there is no evidence.

## Voice-to-presentation acceptance gates

`Consent → authorized voice/avatar source → transcript review → content/evidence label → spoken output → face/lip-sync integration → timing/quality tests → accessibility/privacy review → live release`

The current browser prototype is not a production voice clone, photorealistic lip-sync, remote reasoning engine, live broadcast, or payment service. Provider integration and end-to-end tests are separate deliverables.

## Five-minute automission cycle

Each scheduled cycle should select a bounded task, check dependencies, create or improve a concrete asset, run relevant tests, write an auditable result, and enqueue the next independent task. Use concurrency limits, idempotency keys, timeouts, retry caps, a dead-letter queue, and a human approval gate for external communications, purchases, destructive changes, security-sensitive changes, or high-impact decisions.

A scheduled workflow is not proof that every five-minute cycle succeeded. Measure actual run completion, artifacts created, tests passed, failures, and queue age. Do not promise unattended permanent operation or a five-month/one-year verification outcome without observed reliability data.

## Immediate implementation order

1. Resolve and merge the existing Voice-to-Presentation Studio PR without discarding newer main-branch README material.
2. Apply repository security controls and add evidence-backed CI/security checks.
3. Make the public showroom point to real concrete products with honest state and product-specific demos/visuals.
4. Prioritize the writing/research revenue path before speculative large-scale platform features.
5. Add provider-backed voice/video, checkout, email sending, and persistent review aggregation only after credentials, backend, consent, privacy, and end-to-end tests are available.
