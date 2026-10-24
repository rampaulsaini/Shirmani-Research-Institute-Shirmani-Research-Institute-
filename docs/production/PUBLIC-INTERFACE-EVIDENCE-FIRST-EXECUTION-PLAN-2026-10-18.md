# Public Interface, Evidence and First-Revenue Execution Plan
**Date:** 2026-10-18  
**Repository:** Shirmani Research Institute  
**Status:** execution contract; this document is not proof that listed integrations or revenue already exist.

## 1. Operating rule

Work on the highest-value incomplete deliverable until its acceptance checks pass or a specific blocker is recorded. Do not repeatedly rebuild completed artifacts without a new defect, regression, changed requirement, or failed acceptance test. Preserve existing content and links; use additive changes and reversible migrations.

A workflow run, catalogue identity, product name, plan, browser-local draft, or successful build is not by itself a finished product, a customer, a sale, independent verification, or a live AI integration.

## 2. Public-home information architecture

Keep the public entry page understandable to a first-time visitor, from top to bottom:

1. **Institute identity and purpose** — concise Hindi/English introduction and a clear primary action.
2. **Start here** — Explore products, Try a demo, Request a service, Check evidence.
3. **Six visitor paths** — Research & Education; AI/ML/NLP; Creator & Media; Nature & Public Good; Commerce & Institutions; Community.
4. **Featured usable products** — only real product pages, working core use cases, example inputs/outputs, usage guide, known limitations and QC state.
5. **Services and first-revenue offer** — scope, deliverables, revision policy, indicative price or quote basis, turnaround, enquiry route and payment terms confirmed before work starts.
6. **Community and accounts** — link to the social MVP. Clearly distinguish a local prototype from real accounts. Do not display a working-login claim until server-side authentication, session handling, password reset, authorization, privacy policy and security tests exist.
7. **Heart-View / presentation** — authorized image and voice identity, script, provider job, rendered media, audio, lip-sync and live Q&A as separately evidenced capabilities.
8. **Production and trust** — live telemetry with timestamp and source, QC, security, evidence and known blockers.
9. **Research archive and footer** — complete legacy materials retained through searchable categories and stable links.

Do not put every module on the first screen. Keep a small number of primary choices, searchable/filterable catalogues, descriptive titles, mobile-friendly spacing, and accessible keyboard/focus states. Do not remove a legacy tool merely because it is not a top-level link.

## 3. Account and community release gates

The static GitHub Pages frontend alone cannot safely provide a production account system. Before claiming signup/login is live, select and configure a supported backend or identity provider and implement:

- registration, login/logout, email verification and password reset;
- server-side authorization and session expiry; secure secret storage and rate limits;
- privacy notice, consent and data deletion/export route;
- abuse reporting, moderation and account recovery;
- automated tests for unauthorized access, invalid inputs, session handling and accessibility;
- documented data retention, backups and incident recovery.

Until these gates pass, label the social page **prototype / local-only** and do not collect sensitive personal data.

## 4. Evidence-backed live counters

Every metric must show its source, last-updated timestamp, measurement window and formula. Missing/stale telemetry must display **Unknown / stale**, never a fabricated zero or 100%.

| Metric | Definition |
|---|---|
| Workflow cycles | Count of actual workflow runs in the stated window; split success, failure, cancelled and skipped |
| Concrete production | Unique repository-bound artifacts that pass their product-specific existence/structure checks |
| QC pass rate | Products passing defined QC ÷ products tested × 100; show sample size |
| Evidence coverage | Required evidence items present ÷ required evidence items × 100; do not call this scientific truth |
| Release readiness | Products passing every mandatory release gate ÷ products evaluated × 100 |
| Media completeness | Products with actual required media and documentation ÷ products in the stated release cohort × 100 |
| Outreach | Prospect researched, draft prepared, human-confirmed send, reply, quote, accepted work and delivered work as separate states |
| Revenue | Confirmed payments only, with date and evidence; otherwise report ₹0 confirmed in the period or unknown if records are unavailable |
| Reliability | Successful eligible runs ÷ all eligible completed runs × 100; exclude skipped runs only if the rule is disclosed |
| Freshness | Age of the latest successful telemetry publication, with an explicit stale threshold |

Do not infer model accuracy, independent verification, human wellbeing, emotion, or a person's “heart/mind percentage” from workflow counts or arbitrary percentages. Philosophical proportions such as 99.9999% / 0.0001% may be displayed as the author's stated framework, not as experimentally established human measurements unless a validated operational definition and independent study support that interpretation.

## 5. Automission job contract

Each job must have a bounded input, idempotency key, timeout, retry/backoff policy, durable output, tests, run identifier, provenance, and a human-review gate for external/public actions. Record: started, completed, failed, blocked, skipped, output artifact, duration and last-success timestamp. Use concurrency groups or queue locks where overlapping runs could corrupt state. Add dead-letter/recovery handling for repeated failures. A job without a useful output or verified state change must not be counted as production.

Prioritization order:
1. preserve platform integrity and backups;
2. unblock a customer-visible product or critical defect;
3. complete one release candidate and its QC evidence;
4. pursue a small, paid, clearly scoped service pilot;
5. improve telemetry and recurring production;
6. expand catalogue volume only when concrete product quality can be maintained.

## 6. First-revenue operating loop

Start with services already represented by the bilingual writing/research tools. Choose a small offer with a defined deliverable, sample, delivery date, revision limit and written payment terms. For each prospect, store only relevant business contact information from an official public source and the source URL/date. Draft individually; a human reviews and sends. Respect opt-outs and site terms. Do not scrape private contact data or mass-send unsolicited messages.

Track the funnel without estimating success:
**qualified prospect → tailored draft → human-confirmed send → reply → scope/quote → accepted job → deliverable → invoice → payment confirmed → feedback**.

A prepared draft is not outreach. An opened email is not a reply. An accepted quote is not revenue. A delivered draft is not paid until payment evidence is recorded.

## 7. Heart-View / HeyGen evidence chain

Use the already-provided HeyGen video reference in the project; do not repeatedly ask the user for the same photo or video. Record provider and asset references without exposing credentials. Validate these independently:

1. source/identity authorization and exact approved script;
2. provider job accepted and job ID recorded;
3. completed rendered video exists and is retrievable;
4. video playback, duration and audio track checked;
5. voice content checked against the approved script;
6. lip-sync reviewed on a defined sample of utterances, with defects recorded;
7. live Q&A tested separately with actual prompt/response logs and latency;
8. external-service result, timestamps, errors and reviewer recorded.

A pre-existing hosted video is evidence of that asset only; it does not prove that a live provider connection, voice generation, lip-sync pipeline or real-time Q&A works end-to-end today.

## 8. Security and release

Use least-privilege GitHub Actions permissions, pinned/reviewed actions where practical, secret scanning, dependency checks, input validation, output escaping, backup/recovery tests and an incident log. Only run authorized tests against owned systems. Do not delete a filter or security control solely because it slows a run: first establish what it blocks, reproduce the failure, and replace it with a safer targeted control. Preserve data and provide a rollback.

## 9. Acceptance checklist for the next implementation pass

- [ ] Inspect current public entry page and preserve its legacy destinations.
- [ ] Test all public navigation links and mobile layout.
- [ ] Publish a small featured-product set based on working artifacts, not catalogue identity count.
- [ ] Add explicit account/community readiness state; no fake authentication.
- [ ] Ensure each public live counter names a machine-readable source, timestamp and formula.
- [ ] Verify one end-to-end customer deliverable from input to export and human QC.
- [ ] Prepare a small official-source prospect list and tailored drafts; record sends only when actually sent.
- [ ] Verify the supplied HeyGen asset and any live integration separately; report only observed results.
- [ ] Run existing CI/tests, record failures and create fixes for reproduced defects.
- [ ] Publish a dated report separating completed, blocked, unverified and next actions.

## 10. Definition of done

A task is complete only when the changed artifact is committed, relevant tests pass, the public link works where applicable, its status and limitations are accurate, and evidence is linked. If blocked by credentials, provider entitlement, human approval, unavailable service, or missing backend, state the exact blocker and leave the capability visibly unverified rather than claiming completion.
