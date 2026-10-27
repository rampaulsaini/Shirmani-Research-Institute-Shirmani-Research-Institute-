# Shirmani Research Institute — Revenue-First Platform Improvement Plan

**Status:** Proposal and execution checklist; not a claim that features, sales, or external integrations are already live.  
**Principle:** Preserve existing work. No destructive cleanup, mass outreach, unverified claims, or production changes without evidence and review.

## 1. Immediate priority: a real, measurable income path

Start with the services already stated as available:
- Hindi/English writing and editing
- Research summaries and source-based research
- Website and blog content

Do not advertise products or capabilities as available until a working demo and acceptance checks exist.

### Enquiry form
Collect only what is needed to scope the work:
- Name and reply email
- Service type
- Topic / intended audience
- Language and approximate word count
- Desired deadline
- Source links or supplied files
- Budget range
- Permission to contact about this enquiry

Show this notice before submission: **“We will confirm scope, price, deliverables, schedule, and payment terms in writing before work begins.”** Validate input, protect against spam, provide a clear privacy notice, and never expose submitted enquiries publicly.

### Quote-to-delivery workflow
1. Enquiry received → issue a reference ID and acknowledge receipt.
2. Human review → clarify scope and source requirements.
3. Written quote → deliverables, revision limit, schedule, price, payment terms, and cancellation/refund terms.
4. Client acceptance and agreed payment/deposit → work begins.
5. Deliver draft with sources where relevant.
6. One agreed revision round (or as quoted) → client acceptance.
7. Record invoice/payment status and request optional feedback.

**Revenue metrics:** qualified enquiries, response time, quotes sent, quote acceptance rate, paid orders, delivery-on-time rate, revision rate, refunds, and net revenue. A visit, email sent, or quote is not a sale; report revenue only from confirmed payment records.

## 2. Public showroom: clear top-to-bottom information architecture

Replace the mixed “everything on one page” presentation with a clear, responsive landing page. Keep every existing feature reachable; move lower-priority or experimental work into labelled sections rather than deleting it.

Suggested order:
1. **Header:** Shirmani Research Institute logo/name; Products; Services; Research & Learning; Creator Studio; Nature & Society; About; Sign in; Create account.
2. **Hero:** plain-language explanation of what the platform currently offers, with one primary “Request a quote” action and one “Explore demos” action.
3. **Available now:** Hindi/English writing, research summaries, website/blog content. Mark each item Available, Demo, In development, or Planned.
4. **Product catalogue:** search, category filters, cards with audience, purpose, features, version, status, price or “request a quote,” demo, documentation, and support.
5. **Live demos / test drive:** only working demos; disclose limitations and data handling.
6. **Research library:** organised by topic, language, date, evidence level, and source; distinguish original research, commentary, and external references.
7. **Creator and presentation studio:** video/voice/lip-sync capabilities only to the extent verified; separate prerecorded generation from interactive live Q&A.
8. **Institutions and enterprise:** use cases, security/privacy summary, pilot proposal, procurement contact.
9. **Trust and transparency:** verification reports, accessibility, privacy, terms, status page, contact.
10. **Footer:** policies, support, contact, social links.

### Content organisation
Create a catalogue/inventory before moving content. For every existing page, tool, product, research item, workflow, and asset, record its current path, owner/source, status, intended audience, dependencies, last verified date, and destination section. Preserve originals and links. Flag duplicates for review; never auto-delete a file or feature solely because it appears unused.

## 3. Account and customer journey

A public account flow should include:
- Sign-up, sign-in, sign-out, password reset, email verification
- Secure sessions and server-side authorisation
- User profile, order/enquiry history, consent and account deletion request
- Rate limits, bot protection, input validation, audit events
- Accessible keyboard/mobile layouts and clear error messages

Do not collect payment-card details directly unless a compliant payment provider handles them. Before enabling checkout, define currency, tax/invoice rules, refund policy, service terms, and payment reconciliation. Never store passwords in plain text or put secrets in frontend code.

## 4. Product catalogue and sustainable packaging

Each product needs a stable ID, name, plain-language outcome, target user, verified feature list, prerequisites, demo link, version, release notes, support route, limitations, data/privacy notes, price basis, and acceptance tests.

Possible packaging (only after capabilities are validated):
- **Preview:** safe, limited demo
- **Standard:** documented core workflow
- **Professional:** additional capacity/support
- **Enterprise:** agreed security, support, integration, and procurement requirements

Do not promise “un-copyable,” unlimited scale, or superiority claims without a defined, independently measurable basis. Protect legitimate IP with access controls, licensing, provenance, and security review.

## 5. HeyGen / human-presentation verification chain

Treat the provided HeyGen URL as a supplied reference, not proof that end-to-end behaviour has been independently tested. Keep these checks separate and save dated evidence for each:
1. Source voice: rights/consent and correct asset identity.
2. Voice integration: correct voice selected; successful generation; output playback checked.
3. Script/content: intended text matches the generated script.
4. Lip-sync: test clips across short/long utterances; log visible timing or pronunciation defects.
5. Video presentation: playable output, audio/video sync, mobile and desktop checks.
6. Live Q&A: only claim live interaction after a real test session proves question input, response generation, audio output, latency, and failure handling.
7. External service: record test date, account/feature availability, configuration (without secrets), outcome, and reproducible steps.

Use a chain-of-evidence record: test ID, build/version, test case, expected result, actual result, pass/fail, evidence URL or artifact, reviewer, timestamp, known limitations. A generated video alone does not prove live Q&A.

## 6. Safe automation and layered security

Use a staged, reversible workflow:
- Inventory → static checks → unit tests → integration tests → preview/staging → independent review → approved release → post-release monitoring.
- Use least-privilege GitHub Actions permissions; pin third-party actions where practical; protect production secrets; avoid exposing tokens in logs.
- Add dependency and secret scanning, input validation, access-control tests, backup/restore checks, and an incident/rollback runbook.
- Keep a health dashboard for failed jobs, repeated retries, stale tasks, external-service failures, and release status.
- Deduplicate only with a stable identity key and a dry-run report. Quarantine suspected duplicates; preserve audit trails and a restore path.
- Never delete or rewrite production data automatically just because a task is low activity. Require backup, impact report, and approval for destructive actions.
- Avoid infinite retry loops: use bounded retries, backoff, idempotency, alerting, and a dead-letter queue.

## 7. Outreach that is accurate and consent-aware

Start with a small, relevant prospect list rather than bulk messaging all 195 countries. Identify each institution's actual needs and publicly listed business contact; follow applicable email, privacy, and messaging laws. Do not scrape private personal data, send deceptive claims, or automate WhatsApp/email blasts.

Prepare a concise one-page service sheet and a tailored sample. Track prospect source, fit, contact permission/legal basis, date, response, follow-up limit, opt-out, and outcome. Send no message until sender identity, offer, pricing basis, demo, and reply route are verified.

## 8. 7-day execution sequence

- **Day 1:** inventory current pages/assets/workflows; capture baseline and backup; identify existing service/enquiry code.
- **Day 2:** define landing-page navigation and content status labels; map all existing sections to destinations.
- **Day 3:** build or refine the writing/research enquiry-to-quote path using existing architecture; validate form and privacy behaviour.
- **Day 4:** test account and enquiry journeys, mobile layout, accessibility, spam controls, and failure states.
- **Day 5:** publish verified service descriptions, sample deliverables, quote template, and a demo with limitations disclosed.
- **Day 6:** run the first small, compliant outreach batch and track replies; do not count sends as revenue.
- **Day 7:** review evidence: working pages, tests, qualified enquiries, quotes, paid orders, blockers, and next priorities.

This is a sequence, not a promise that all tasks can be completed in seven calendar days. Dependencies and current code may change the schedule.

## 9. Definition of done

A task is done only when:
- The change is committed and reviewed.
- Relevant automated tests pass.
- The public page is reachable and understandable on mobile and desktop.
- No existing feature/content was lost; inventory mapping is complete for changed sections.
- Security/privacy and accessibility checks are recorded.
- Demo claims match observed behaviour.
- Monitoring, rollback, and ownership are documented.
- Business outcomes are reported from evidence, not estimates presented as facts.

## 10. Immediate next engineering action

Inspect the existing public-interface routes, enquiry forms, authentication, product catalogue, and workflow definitions before implementing duplicate systems. Reuse working components, make the smallest reversible changes, and attach test evidence to the pull request. This document is a planning artefact; it does not itself implement or verify those runtime features.
