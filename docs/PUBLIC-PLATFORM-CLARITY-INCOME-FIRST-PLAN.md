# Public Platform Clarity, Verified Production, and Income-First Delivery Plan

**Purpose:** Turn the existing collection of pages and modules into a navigable public platform, with truthful operational evidence and a practical path to the first paid customer.

**Status:** Planning baseline; this document is not proof that implementation, deployment, account creation, sales, or third-party verification has happened.

## 1. Delivery rules

1. **Finish one vertical slice before expanding.** Every slice includes UI, real behavior, tests, evidence, and a visible status. Do not create another nominal-only module.
2. **Preserve existing work.** Inventory and link existing pages first; do not delete or overwrite working modules as part of a redesign. Use small PRs with rollback paths.
3. **Evidence before claims.** Separate `NOT_IMPLEMENTED`, `DEMO`, `IN_PROGRESS`, `PASS`, `FAIL`, and `BLOCKED`. A scheduled workflow is not a completed production cycle; a passing CI check is not independent scientific verification.
4. **No invented live metrics.** Counters must come from timestamped workflow/API/DB events and show the source, time window, last update, and stale/unavailable state. If there is no live data source, display “Not connected” rather than a fabricated number or percentage.
5. **No unsafe cleanup.** A filter may quarantine irrelevant or duplicate work only when a reason and recovery route are recorded. Deletion requires a retention rule and a recoverable backup.
6. **Income first, ethically.** Prioritize a small set of deliverable services, demos, transparent prices/offers, lead tracking, and human-reviewed outreach. Do not scrape or bulk-message institutions, invent official email addresses, or send campaigns without review and a lawful basis.

## 2. Public information architecture

Use a simple, mobile-first top-to-bottom path:

1. **Home / Start here** — one-sentence purpose, clear audience, primary calls to action, language selector, and a short “what works today” status.
2. **Products and services** — searchable categories; each product card must state the user problem, actual features, input/output, limits, demo, delivery time, price/offer (or “quote required”), and support/contact route.
3. **Try a demo** — working sample with sample data, expected output, reset control, and explicit DEMO label wherever it is not connected to production services.
4. **Research and evidence** — research notes, sources, methods, limitations, reproducibility, and independent-review status. Personal/philosophical statements are presented respectfully as attributed viewpoints, not silently converted into empirical proof.
5. **Heart-View Preview** — accessible explanation and guided experience, with its own status and methodology. Keep the user-defined 99.9999% / 0.0001% figures labelled as a proposed philosophical parameter unless a reproducible measurement method and validation evidence are supplied; do not present them as established scientific measurements.
6. **Media / HeyGen** — retain the supplied existing video reference. Distinguish video existence, audio identity, lip-sync review, dialogue/interaction test, and end-to-end test. Each needs its own evidence, date, and reviewer; do not ask the user to re-upload material already referenced.
7. **Community** — explain whether sign-up, login, profiles, posts, moderation, and account recovery are actually supported. A static GitHub Pages prototype must not imply secure account creation. Enable real accounts only with a backend, secure authentication, privacy notice, abuse controls, and tested recovery.
8. **Research institute / institutions** — research, education, nature, creators, AI/ML/NLP, public-sector and private-sector use cases, contact route, and procurement-ready service sheets.
9. **Progress & accountability** — production report, workflow runs, automation cycles, test results, delivery evidence, unresolved blockers, and last-updated timestamps.
10. **About, governance, privacy, accessibility, contact** — ownership, terms, data practices, accessibility statement, corrections process, and support.

## 3. Product catalogue contract

Every product must have a real record with:
- Stable ID, name, category, audience, problem solved, current maturity, and owner.
- Working URL or an explicit “not available yet” state.
- Feature list, use cases, requirements, limitations, and demo/test instructions.
- Price, introductory offer, quote process, delivery scope, and refund/support terms where applicable.
- Evidence links: tests, sample output, release/commit, and last verified date.
- A clear CTA: Try demo, Request a quote, Contact, or Join waitlist. Buttons must do what they say.

Generate public catalogue cards from one structured manifest rather than duplicating descriptions by hand. Validate that every listed product has a destination and a truthful status.

## 4. Live accountability metrics

Only calculate a percentage when its numerator, denominator, time window, and source are defined. Recommended definitions:

- **Workflow success rate:** successful completed runs / all completed runs in the selected window. Show failures and cancellations separately.
- **Cycle completion:** cycles reaching the declared terminal state / cycles started in the window.
- **Evidence coverage:** completed deliverables with linked, reviewable evidence / completed deliverables.
- **Test pass rate:** passed tests / tests executed; show skipped and failed tests separately.
- **Product readiness:** weighted checklist items passed / applicable checklist items, with the checklist version visible. Never label this independent verification.
- **Delivery reliability:** verified fulfilled orders / orders due in the selected period.
- **Income:** actual paid receipts reconciled to a source, separately from quotes, leads, pipeline, and projected revenue.

Every metric needs `source`, `window_start`, `window_end`, `updated_at`, `status`, and a drill-down to the underlying evidence. “24/7/365” is an uptime goal until uptime monitoring proves it.

## 5. Income-first first customer loop

1. Inventory the existing service/product pages and identify the **three** strongest deliverables that can be demonstrated today.
2. Create one concise service sheet per deliverable: problem, sample/demo, features, boundaries, price/introductory offer, delivery time, and contact method.
3. Make the quote/request form collect only necessary information and deliver submissions to a monitored inbox or backend. Test the entire path using a synthetic lead.
4. Build an institution prospect list from public official sources with source URLs, relevance rationale, jurisdiction, and a human-verified contact address. Do not guess addresses.
5. Draft tailored outreach in a review queue; require human approval before sending. Record sent, bounced, replied, opted-out, and follow-up states. Respect applicable anti-spam and privacy rules.
6. Track the funnel: verified prospects → approved contacts → messages sent → replies → qualified requests → proposals → paid receipts → fulfilled work → customer feedback.
7. Publish case studies only with permission and verifiable evidence. Do not claim a sale, customer, or deployment until it actually occurs.

## 6. Heart-View and media verification gates

- **Video asset:** link resolves and video is playable.
- **Voice:** compare against an authorized reference using a documented human review or suitable test; do not infer identity from a video URL alone.
- **Lip-sync:** review defined sample intervals and record reviewer/date/result.
- **Dialogue:** test a fixed set of prompts and expected behavior; save transcripts/results with consent and privacy safeguards.
- **Live Q&A:** test the real user input → service response → displayed/audio response path.
- **End-to-end:** run from the public entry point through the real connected service and capture timestamped evidence.
- **Independent verification:** record the independent reviewer, method, scope, conflicts/limitations, and report. Automated checks alone do not satisfy this gate.

The existing user-provided HeyGen video reference is:
https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7

## 7. Security and reliability

- Keep secrets and private tokens out of static HTML, public JSON, logs, and browser code.
- Use least-privilege credentials, dependency scanning, input validation, rate limits, backup/restore tests, and a documented incident route.
- For a static public site, do not imply that client-side code alone can provide secure user accounts, private records, or server-side authorization.
- Add idempotency, retry/backoff, dead-letter/quarantine visibility, and recovery tests to automation flows before raising throughput.
- Keep security tests scoped to owned systems and authorized environments; log findings and fixes.
- Every scheduled job must publish a clear outcome and failure reason, not merely a green-looking heartbeat.

## 8. Acceptance checklist for the first release

- [ ] Homepage has a clear hierarchy and no wall of undifferentiated links.
- [ ] Navigation works on mobile, keyboard, and screen reader.
- [ ] Product catalogue is generated from a validated manifest.
- [ ] Every product card has a working destination and truthful maturity label.
- [ ] Demo path works with sample data and identifies any mocked behavior.
- [ ] Contact/quote submission is tested end-to-end.
- [ ] Operational counters are sourced, timestamped, and stale-aware.
- [ ] Heart-View and HeyGen verification gates are shown independently.
- [ ] Sign-up/login is either truly implemented and security-tested or explicitly labelled as a prototype/not available.
- [ ] Automated tests, accessibility checks, and broken-link checks pass.
- [ ] A human reviews the release and the rollback path is documented.

## 9. Execution order

**P0 — Reduce confusion:** audit current `index.html`, existing product pages, social MVP, outreach workbenches, and production reports; build a route/product manifest and flag duplicates without deleting them.

**P1 — First revenue path:** select three deliverables that demonstrably work; polish demo/service sheets; test the quote/contact flow; create a human-approved lead and follow-up pipeline.

**P2 — Public interface:** refactor the homepage into the information architecture above, reuse existing modules, add search/category filters and clear status labels.

**P3 — Evidence dashboard:** connect real workflow/test/order sources; publish source-backed counters and daily reports. No synthetic “live” values.

**P4 — Accounts and community:** choose and configure a suitable backend before enabling real sign-up/login; implement privacy, moderation, access controls, and recovery tests.

**P5 — Verification and scale:** complete Heart-View/HeyGen evidence gates, recovery/idempotency testing, security review, and then increase automation throughput.

## 10. Completion reporting format

For every work item report: `DONE`, `IN PROGRESS`, `BLOCKED`, or `NOT STARTED`; exact files/commit; test command and result; evidence link; remaining risk; next action. Never report “complete” based only on a page existing or a workflow being scheduled.
