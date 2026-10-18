# Public Interface Rebuild & Evidence Contract
**Date:** 2026-10-18  
**Status:** Implementation contract / acceptance criteria; not a claim that the public site has already been rebuilt or that integrations are live.

## Purpose
Replace the confusing “everything on one page” experience with a calm, ordered public showroom. Keep the existing work discoverable; do not silently delete, overwrite, or mark unfinished work complete. Prioritise the first usable customer journey and a credible path to paid work.

## Public interface: top-to-bottom information architecture
1. **Home / clear promise** — “Shirmani Swarup Drishtikon”; one sentence explaining that people can explore, test, commission, and purchase digital tools and research/writing services. Primary actions: Explore tools, Try a demo, Request a service, Sign in.
2. **Featured working demos** — show only tools that can be opened and tried now. Every card states: what it does, who it helps, input, output, limitations, last checked date, and demo link.
3. **Product showroom** — searchable/filterable categories: AI & automation; writing/research; creator/media studio; education/library; nature & conservation; commerce; institutional/government/private-sector tools; labs and experiments. Categories may be labelled “planned” only when no working item exists.
4. **Services / earn first revenue** — Hindi/English writing, research summaries, and website content. Show a clear brief form, sample deliverable, scope, turnaround, revision policy, price/quote path, and payment terms. Never imply a booking, payment, or sale has happened unless the system records it.
5. **Heart-View / Character experience** — distinguish the character philosophy/specification from the actual video, voice, lip-sync, dialogue, and live Q&A capabilities. Use the already supplied HeyGen reference: https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7 . Do not ask the owner to re-send this reference.
6. **Research institute** — research papers, explainers, methods, source ledgers, experiments, and evidence limitations. Label hypotheses, personal philosophy, measured findings, and independently reproduced results separately.
7. **Library & learning** — curated topic shelves and source links. Do not imply that copyrighted or unavailable full texts are hosted; distinguish catalogue/link, excerpt, public-domain copy, and licensed content.
8. **Nature / public benefit** — conservation, education, healthcare, food, clothing, and housing initiatives with practical partners and measurable outcomes; avoid unsupported impact claims.
9. **Institutional / creator solutions** — use cases, product capability sheets, demo request, procurement/contact path, and an honest “not yet available” label for unbuilt features.
10. **Trust, security, accessibility, account** — privacy notice, terms, contact, report a problem, login/signup only when backed by a real identity/session backend. Until then, label account UI as a prototype and do not collect real passwords or sensitive information.

## Product-card minimum contract
Each product card must include:
- Unique ID and category
- Plain-language purpose and intended user
- Current state: idea, prototype, demo-ready, verified, published, or retired
- Real demo/open action (not a dead button)
- Input → process → output example
- Limitations and human-review requirements
- Version, last verified timestamp, verification method, and evidence link
- Price or “request a quote”; never fabricate pricing, customers, ratings, or sales
- Owner/support path and known dependencies

A category or module is not “complete” merely because its name appears in a menu. A module passes only when its stated action produces its stated output and its acceptance test is recorded.

## Evidence-gated Heart-View chain
Track each stage independently; downstream stages cannot inherit a “pass” from an upstream stage.

| Stage | Minimum evidence to mark PASS | If absent |
|---|---|---|
| Reference video | Existing supplied URL opens and identifies the intended reference | REFERENCE_LINK_UNCHECKED |
| Voice | A consented, actual audio sample is playable and source/permission is recorded | VOICE_NOT_VERIFIED |
| Content/dialogue | Exact script/prompt and generated response are saved with timestamp | CONTENT_NOT_VERIFIED |
| Photo/avatar | Exact approved portrait/avatar asset and permission/source record exist | AVATAR_ASSET_NOT_VERIFIED |
| Lip-sync/video | Actual generated output is playable; visible speech/audio are checked against a stated sample and tolerances | LIPSYNC_NOT_VERIFIED |
| Live presentation | A real live session or provider test result is recorded, not a mock UI | LIVE_NOT_VERIFIED |
| Live Q&A | Timestamped test prompts and actual responses, failures, latency, and safety fallback are recorded | QA_NOT_VERIFIED |
| External provider | Provider response/job ID or export plus timestamp and error details are saved | PROVIDER_NOT_VERIFIED |

The supplied HeyGen URL is a known reference, not by itself proof of voice provenance, successful lip-sync, live Q&A, or end-to-end integration. Preserve that distinction visibly.

## Honest operational counters
Display “Not instrumented” rather than zero when no telemetry exists. Display zero only after a collector has run successfully for the stated interval.

- **Availability:** successful health checks / total scheduled health checks, with window and timestamp.
- **Automation cycles:** completed / started; show failures, retries, skipped runs, last run, and scheduler status.
- **Production:** artifacts actually created and validated per day; link to each artifact or run log.
- **Quality:** passed acceptance checks / checks executed, with test-suite/version and sample size. Do not convert subjective ratings into scientific accuracy.
- **Evidence coverage:** claims with linked evidence / claims sampled; show exclusions and audit date.
- **Security:** latest dependency/code/config scan status, finding counts by severity, scan time, and unresolved findings. Never expose secrets or sensitive logs publicly.
- **Sales funnel:** enquiries received, replies sent, quotes issued, paid orders, refunds; each number comes from recorded events and has a date range. Do not equate outreach with revenue.
- **Uptime:** only from a real monitor with a published measurement window and definition.

Every counter must have a definition, unit, interval, source, last-updated time, and drill-down evidence. Do not display made-up 24/7/365 activity, cycle counts, percentage scores, or “99.9999%” quality claims without reproducible data.

## Revenue-first execution lane
1. Make the existing SRI-WRITE-006 and SRI-WRITE-007 browser-local demos easy to discover and try.
2. Publish one clearly scoped service offer: Hindi/English website copy, writing, or research-summary preparation. State that research claims require sources and human review.
3. Provide a brief intake template: objective, audience, language, length/pages, source material, deadline, deliverable format, usage rights, and review needs.
4. Quote only after scope is known; record price, delivery date, revision limits, and payment terms in a written order.
5. Prepare a small sample/demo deliverable and a one-page capability sheet. Contact only relevant, publicly listed official business/institutional channels with tailored messages and an opt-out; no bulk spam, invented contacts, or claims of partnerships.
6. Track each lead from identified → qualified → contacted → replied → quoted → paid → delivered; count income only when payment is actually confirmed.
7. Keep a daily work log with links to outputs, blockers, time spent, and next concrete action. A completed document is not the same as a deployed feature or a paid sale.

## Security and privacy baseline
- Never commit API keys, provider tokens, passwords, private voice/portrait files, customer briefs, or raw personal data.
- Use least-privilege credentials, server-side secret storage, dependency updates, input validation, output escaping, rate limiting, audit events, backups, and documented incident recovery before production launch.
- Do not claim “ethical hacking complete” without scope, permission, tool/version, timestamp, findings, remediation, and retest evidence.
- Keep login/signup disabled or clearly prototype-only until server-side identity, secure sessions, account recovery, privacy/retention rules, and abuse controls are tested.
- Separate public showcase assets from private source assets; retain consent and licensing records.

## Acceptance checklist
- [ ] The homepage has a clear hierarchy and works on mobile and desktop.
- [ ] No dead navigation or decorative-only product buttons.
- [ ] Every listed tool has a state, actual action, output example, limitation, and verification date.
- [ ] Planned features are visibly distinguished from working demos.
- [ ] Existing project assets remain discoverable through a catalogue; no unreviewed deletion.
- [ ] Heart-View evidence stages remain independently labelled.
- [ ] Counters are sourced from telemetry or display “Not instrumented”.
- [ ] Login/signup does not collect real credentials until a secure backend exists.
- [ ] At least one service offer can be understood, requested, quoted, delivered, and recorded without pretending payment automation exists.
- [ ] Keyboard navigation, contrast, readable Hindi/English text, and mobile layout are checked.
- [ ] Tests, screenshots/URLs, and release notes are attached before any module is called production-ready.

## Non-goals for this document
This contract does not itself redesign the live homepage, wire up a database, connect HeyGen, create a verified voice clone, implement streaming, run security scans, send outreach, process payments, or create revenue. Those require separate code changes and observable test evidence.