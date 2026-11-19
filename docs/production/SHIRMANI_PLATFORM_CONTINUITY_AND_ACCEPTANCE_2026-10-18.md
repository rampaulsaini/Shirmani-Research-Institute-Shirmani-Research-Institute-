# Shirmani Platform Continuity, Acceptance Gates & Production Chain
Date: 2026-10-18
Status: implementation/acceptance contract; this document does not claim deployment, revenue, live telemetry, authentication, or end-to-end provider verification.

## 1. Non-negotiable continuity rules
- Preserve existing pages, media, research, tools, product records, generated assets, legacy routes, and private/internal work. Do not delete or overwrite an item merely because it is not linked from the public homepage.
- Prefer improving the current entry point and connecting existing destinations over creating another competing homepage or duplicating catalogues.
- Every module must contain usable material or explicitly state what is missing, what blocks it, and the next test. A title/card alone is not a completed module.
- Do not repeat requests for the user's portrait, voice, or existing HeyGen reference. Reuse authorized existing references; ask only if an exact asset cannot be accessed or authorization is genuinely unresolved.
- Never invent counters, evidence, successful tests, sales, income, external messages, account features, or provider states. Keep "not connected", "not tested", "failed", and "verified" distinct.
- Complete and validate one bounded task before starting unrelated work. A blocker must be recorded with owner/action/evidence rather than hidden by a green status.

## 2. Public entry page: top-to-bottom visitor journey
The public entry page should guide a first-time visitor in this order:
1. Clear identity, plain-language purpose, and primary actions.
2. Income-first services that can genuinely be delivered now (writing/research enquiry, scope, deliverables, turnaround, quoted price, and payment instructions only when configured).
3. Digital product catalogue with category, problem solved, use cases, limitations, quality evidence, demo/test-drive, price/status, and a clear enquiry/order path.
4. Product demos and studio/labs; separate working demos from concept/specification pages.
5. Heart-View character and media chain, with separate evidence for source asset, voice authorization/match, generated audio/video, lip-sync, live Q&A, and end-to-end run.
6. Research, education, library, nature/conservation, public/private-sector solutions, and institutional offerings.
7. Production/accountability dashboard, quality methodology, open blockers, changelog, and evidence links.
8. Account area: show signup/login as unavailable until a real identity provider, secure session handling, recovery, privacy notice, and tests are connected. Never present a mock form as working authentication.
9. Archive/internal-work index so material not appropriate for the public hero still remains discoverable to maintainers.
Use responsive layout, accessible contrast/focus states, plain Hindi-first wording, stable local links, and a small set of clear primary actions. Avoid a dense "everything at once" wall of cards.

## 3. Measurable production counters
Counters must be computed from timestamped records, with source and time window visible. Until server-side telemetry is connected, label browser-local/manual data as a prototype and do not call it platform-wide live data.

Required counters:
- Cycles recorded (all-time) and cycles completed today, with timezone and last update.
- Completed / attempted cycles and success rate = completed ÷ attempted × 100.
- Evidence-backed passed checks / checks evaluated and evidence-backed pass rate = passed with linked evidence ÷ evaluated × 100.
- Open blockers, failed checks, stale evidence, and pending human reviews.
- QC score by dimension (functionality, accessibility, link integrity, security, content accuracy, media/audio-video sync); show denominator, rubric/version, evaluator, and evidence.
- Production hours/runs only when actual timestamps/logs exist.
- Sales enquiries, quotes sent, paid orders, refunds, and net receipts only from authoritative records; separate each state and currency.
- Automation cycles and workflow run IDs sourced from GitHub Actions or an authenticated backend when integrated. A local button press is not an automation cycle.
- 24/7/365 report: daily rows, missing-data indicator, export (CSV/JSON), generated-at timestamp, and audit trail. Do not imply continuous monitoring when no scheduled collector is running.

Never calculate an overall "truth", "purity", or human-worth percentage from philosophical claims. Personal/philosophical frameworks may be presented as perspectives; scientific claims need an operational definition, method, data, uncertainty, and reproducible evidence.

## 4. Voice → Voice System → Content → Photo/Lip-sync → Live presentation
Use the already supplied HeyGen reference:
https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7

Record each gate separately:
1. Reference/access: the saved URL is reachable by an authorized reviewer; record check timestamp and observed status.
2. Source assets: identify the exact authorized portrait and original voice asset by provider asset ID and cryptographic hash where available; never treat a matching filename as a hash match.
3. Voice system: record voice/consent authorization, language, pronunciation sample, provider job ID, output audio, and human listening result.
4. Content: version the script, language, source/fact checks, pronunciation notes, and approval.
5. Rendered media: record provider job ID/status, output file, duration, resolution, audio track, and review result.
6. Lip-sync: use a repeatable sample with annotated timestamps; measure visible/audio offsets and record reviewer, method, tolerance, and pass/fail.
7. Live Q&A: record test set, expected/actual response, latency, timeout/error, audio/video continuity, safety behaviour, and human review. A pre-rendered clip is not live Q&A.
8. End-to-end: run the chain from input question through answer/script, authorized voice, render/lip-sync, presentation, and captured result. Save logs and artifacts; do not promote to VERIFIED until every required gate passes.
9. External provider verification: distinguish provider UI status from independent playback/review and from full integration testing.
10. Improvement loop: every failure creates a ticket with evidence, root-cause hypothesis, fix, regression test, and retest result.

Current repository notes say a completed ~38-second HeyGen sample exists, but the sample alone does not prove original-voice match, portrait fidelity, lip-sync accuracy, latency, live Q&A, or end-to-end production. Treat those as separate open gates until evidence is attached.

## 5. Security and account/payment readiness
- Threat-model public forms, uploads, generated assets, API keys, webhook endpoints, admin actions, and outbound communications.
- Keep secrets server-side; never commit API keys or expose them in browser JavaScript.
- Require least privilege, dependency and secret scanning, input validation, rate limits, CSRF/session protections where applicable, secure headers, backups, audit logs, and recovery procedures.
- Login/signup requires a real identity provider or properly implemented backend, password/session protections, email verification/recovery as appropriate, privacy/retention policy, and positive/negative tests.
- Payments require a configured provider, server-verified webhooks, idempotency, currency/tax/refund handling, receipt records, and test-mode plus production-mode evidence.
- Outbound email/WhatsApp requires verified sender identity, opt-in/appropriate lawful basis, suppression handling, rate limits, delivery/error logs, and human approval before bulk campaigns. Do not scrape or mass-message institutions without permission.

## 6. Revenue-first delivery path
Start with a small number of honest, deliverable services and products instead of advertising the entire future vision as already operational.
For every offer, publish: target user, concrete problem, exact deliverables, exclusions, turnaround, revision limit, price/currency, sample/demo, evidence, contact/order route, and refund/terms.
Track the funnel as separate factual stages: enquiry → qualified → quote → accepted → payment verified → delivery → customer acceptance → support/refund. Revenue is zero until payment evidence exists; enquiries and quotes are not income.
Institutional outreach should be permission-aware and personalized, with truthful product claims, an opt-out, and recorded delivery status. Do not claim partnerships or customer results without proof.

## 7. Acceptance checklist for each change
- [ ] Existing content/assets inventoried and preserved; no unrelated destructive change.
- [ ] Module has working content, meaningful destination, and honest readiness label.
- [ ] New local links resolve; external links and security attributes reviewed.
- [ ] Keyboard/focus, mobile width, headings, labels, contrast, and Hindi text checked.
- [ ] Tests/CI result recorded with exact run URL and commit.
- [ ] Counters derive from traceable records and display missing/stale data honestly.
- [ ] User-facing claims match evidence; no mock functionality represented as live.
- [ ] Reviewer, timestamp, evidence, known limitations, and next action recorded.
- [ ] PR preview reviewed before merge; merge/deploy status recorded separately.

## 8. Work order
1. Reconcile existing homepage/showroom/start-here PRs and avoid parallel duplicate entry pages.
2. Validate one canonical public entry route and every primary destination.
3. Validate the existing telemetry prototype and clearly mark local/manual versus server-sourced data.
4. Continue the Heart-View evidence chain from the existing HeyGen reference without requesting the media again.
5. Offer one genuinely deliverable paid service with transparent scope and order path.
6. Add account/payment/provider integrations only as separately tested implementations.
7. Inventory remaining product, research, library, lab, and internal materials; link them without deletion.
8. Run regression checks after each bounded change and publish only observed results.

## Current limitation
This contract records the acceptance standard and sequence. It is not itself proof that the website has been deployed, counters are live, accounts/payments are functional, security testing is complete, HeyGen is connected end-to-end, or income has been earned.
