# SHIRMANI SUPREME — Public Interface Reorganization & Truthful Operations Dashboard

**Status:** implementation contract / proposed acceptance criteria  
**Date:** 2026-10-18  
**Scope:** public showroom information architecture, visible operational counters, product discovery, account entry points, evidence-backed demonstrations, and release gates.

This document is a build specification. It does not claim that the UI, authentication, live counters, integrations, sales, or revenue are already implemented.

## 1. Primary outcome

Replace the “everything in one page” experience with a calm, responsive, vertically ordered public experience. A first-time visitor should understand within seconds what the platform offers, what works today, how to try it, what it costs or how to request a quote, and what remains under development.

Preserve existing material and routes. Reorganize before deleting; do not discard prior research, product drafts, experiments, or specifications merely because they are not part of the first screen.

## 2. Public page order

1. **Header and navigation** — brand, language choice, search, product catalogue, research library, creators/studio, education, nature & sustainability, institutions, pricing, sign in, create account.
2. **Hero / clear promise** — one short, comprehensible explanation of the platform, one primary “Explore products” action, one secondary “Try a demo” action. No unsupported “world’s best” or guaranteed-capacity claims.
3. **Trust and live status strip** — last update timestamp, service health, active automation runs, latest successful run, failed/blocked runs, and evidence freshness. Show “unavailable” rather than a fabricated zero if telemetry is not connected.
4. **Featured working demos** — only demos that load and perform their stated function; each card states input, output, version, last-tested time, limitations, and evidence link.
5. **Product catalogue** — searchable/filterable cards by category, audience, delivery type, price/quote basis, maturity, and language. Separate Available, Beta, Prototype, Planned, and Blocked.
6. **Heart-View / SHIRMANI SUPREME Character Studio** — clearly distinguish character brief, response workbench, recorded media, generated media, provider-connected status, and end-to-end verification. Use the already supplied HeyGen reference URL: https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7
7. **Research institute and knowledge library** — topic search, curated sources, publication date, source type, language, access/licensing status, and “fact / interpretation / hypothesis” labels. Do not imply copyrighted or restricted works are available without rights.
8. **Creator / studio workspace** — describe the planned multi-version studio and voice-driven creation separately from features that can actually be executed today.
9. **Education, labs, nature and public-interest projects** — clearly scoped pages, not one oversized paragraph. Include practical conservation and human-needs initiatives only where an actual project or resource exists.
10. **Institutional and commercial services** — buyer use cases, deliverables, supported formats, security/data-handling summary, sample output, price or quote method, and a request/proposal flow.
11. **Account entry** — sign-up/sign-in links only when backed by a working authentication service. Otherwise label the entry as planned; never collect passwords in a static prototype.
12. **Footer** — About, contact, privacy, terms, accessibility, security reporting, product status, version history, and correction/report-a-problem path.

## 3. Page design and accessibility

- Mobile-first responsive layout; no horizontal overflow at 320 CSS pixels.
- Use semantic headings, consistent spacing, short paragraphs, cards, progressive disclosure, readable contrast, keyboard focus, accessible names, and reduced-motion support.
- Hindi is the default where appropriate, with clear English equivalents; language switching must preserve the page and query.
- Use a single visual system: restrained deep-ink background, readable light panels, clear typography, and a small accent palette. Do not let decoration obscure status or actions.
- No empty module cards that merely display a name. A module must show a working capability or an explicit status, purpose, owner/dependency, next action, and last-tested time.
- Keep existing product and research material discoverable through catalogue/search rather than putting every detail on the home page.

## 4. Truthful live-counter contract

Counters must be derived from real event records or monitoring sources. Every counter exposes its definition, time window, last updated timestamp, data source, and freshness state.

| Counter | Definition | Required evidence |
|---|---|---|
| Automation cycles | Actual started runs in the selected window | Run ID, start/end, status, workflow |
| Successful cycles | Runs that ended successfully and passed required assertions | Run ID and test results |
| Failed / blocked cycles | Runs with failure, cancellation, timeout, or a dependency block | Reason and event timestamp |
| Production output | Actual artifacts produced and validated | Artifact ID, checksum where relevant, validator result |
| Quality score | Passed test assertions / executed applicable assertions | Test suite version, numerator, denominator |
| Evidence coverage | Applicable requirements with current evidence / applicable requirements | Requirement IDs and evidence links |
| Availability | Measured successful probes / scheduled probes | Probe source, interval, outages |
| Revenue | Payments confirmed by a payment provider or reconciled ledger | Transaction reference, amount, currency, timestamp |
| Outreach | Messages actually sent through an authorised connected channel | Provider message ID and delivery state; drafts do not count |
| Product readiness | Gates passed / gates applicable to that product version | Gate IDs, evidence and test date |

Never label a count “live” unless the source is connected and freshness is visible. If a source is not connected, display **NOT CONNECTED**. If there are no records for a confirmed period, show **0 recorded events** with the window; do not substitute missing telemetry with zero.

Percentages must use a displayed numerator and denominator. Do not use “99.9999% quality”, “accuracy”, “frequency”, or “evidence” without a defined metric, dataset, time window, and reproducible calculation. Philosophical or personal worldview ratios are not scientific or product-quality measurements unless an operational, validated measurement method exists.

## 5. Automation continuity and safe recovery

- Every automation has a unique run ID, trigger, start/end time, status, outputs, retries, dependencies, and error details.
- Retry only transient failures with bounded exponential backoff and a maximum attempt count.
- Idempotency keys prevent duplicate sends, purchases, or artifact creation.
- Use a queue and explicit states: queued → running → succeeded / failed / blocked / cancelled.
- A watchdog detects stale runs, but it must not claim a cycle is running when no worker heartbeat exists.
- Failed work is resumable from a documented checkpoint; do not silently restart destructive actions.
- Preserve logs and prior output. Cleanup/deletion requires retention rules and an auditable decision.
- Human approval is required before external outreach, spending, public release of personal media, or destructive repository/data actions.
- “24/7/365” is a service objective, not a proven availability claim until measured.

## 6. Security baseline

- Least-privilege GitHub Actions permissions, pinned third-party actions where feasible, dependency and secret scanning, CodeQL where supported, and documented remediation ownership.
- Configure branch protection/rulesets, required checks, secret scanning/push protection, and security contact in repository settings; workflow files alone do not activate all repository protections.
- Never place provider API keys, email credentials, payment secrets, or personal source media in public code or logs.
- Use a server-side secret store for provider credentials. Never expose secrets in client JavaScript.
- Authentication must use a maintained identity provider or audited server implementation, secure sessions, rate limits, abuse protection, account recovery, and privacy/consent flows.
- Keep security test environments separate from production. Only test systems and accounts for which the owner has authorization.

## 7. Product card acceptance contract

Every product card must include:
- unique product ID, name, version, category, status and last-tested timestamp;
- plain-language capability statement and intended users;
- input → process → output with a sample that can actually be inspected;
- demo action that works, or explicit **DEMO NOT AVAILABLE**;
- product-specific passport/guide and QR destination, tested separately;
- actual screenshot/video, or explicit **ILLUSTRATIVE MOCK-UP** / **STORYBOARD — NOT RECORDED**;
- price, quote basis, or **PRICE NOT SET**;
- data/security notes, limitations, support path, and next improvement;
- evidence links and a clear “report an issue” action.

A manifest passing validation means its metadata is consistent; it does not prove a URL is reachable, a QR scans, media is authentic, or a demo works.

## 8. Character / media verification chain

Use the measurable chain:

**User question → voice input (if enabled) → speech-to-text → intent/context → source/evidence check → response content → authorised portrait/media → voice generation/provider output → lip-sync → playback/live Q&A → independent review → audit record.**

Record each stage independently with a correlation/run ID, timestamps, input/output references, latency, status, and failure reason. Redact secrets and avoid retaining unnecessary personal data.

For the already supplied HeyGen reference, test only what the linked provider asset actually permits. Keep these states separate:
- reference link supplied;
- provider page reachable;
- video playback verified;
- original photo provenance verified;
- authorised voice verified;
- lip-sync reviewed;
- live Q&A connected and tested;
- end-to-end acceptance passed.

A video link alone is not proof of live Q&A, provider API access, or that the supplied portrait/voice is the source used.

## 9. Commercial workflow and immediate income integrity

- Create a real service catalogue with bounded deliverables: writing, research summaries, product documentation, localization, prototype review, and other services only when they can be delivered.
- Each offer states scope, exclusions, turnaround, revision count, price/currency, payment terms, and sample deliverable.
- Institutional lead lists must use public, official, relevant contact sources and comply with applicable privacy, anti-spam, and platform rules.
- Generate a draft proposal first. Sending requires an authorized outbound connection, owner approval, and a recorded provider result. Never claim outreach from a prepared draft.
- Track funnel states independently: prospect identified → contact verified → proposal drafted → approved → sent → response → scope accepted → delivered → invoice issued → payment confirmed.
- Do not claim revenue until payment evidence exists. Do not promise that contacting all 195 countries or millions of institutions is already underway.

## 10. Delivery phases and exit criteria

### Phase A — Inventory and protect
- Inventory public routes, products, existing research, assets, and dependencies.
- Preserve all existing material; create an index of routes and orphaned content.
- Record current build/test/deployment status without assuming success.

### Phase B — Public information architecture
- Implement shared header/footer, page sections, category catalogue, status labels, and responsive design.
- Confirm no existing route or product content was silently dropped.
- Run link, mobile viewport, keyboard, and accessibility checks.

### Phase C — Product discovery and demo integrity
- Validate each product record, unique IDs, passport links, demo links, and real media.
- Publish only accurate states; block unsupported claims.

### Phase D — Operational telemetry
- Connect real automation, deployment, artifact, quality, and uptime sources.
- Show timestamps, freshness, denominators, failures and missing-data states.
- Test stale telemetry and failed jobs.

### Phase E — Accounts and commercial delivery
- Implement secure account system only with a real backend/provider.
- Add service offers, proposal generation, approval, delivery tracking, and payment reconciliation.
- Test access control and privacy boundaries.

### Phase F — Character and external integrations
- Connect provider services only after credentials, permissions, data handling and costs are reviewed.
- Run documented voice, playback, lip-sync and live Q&A tests; publish only what passed.
- Maintain four product versions only if each has a distinct scope, tested behavior and price.

## 11. Definition of done

The public interface is ready for release only when:
- a first-time visitor can understand the platform and find a relevant product quickly;
- all primary navigation links work and the layout is readable on mobile;
- every visible module contains real useful content or an honest, actionable status;
- counters are sourced, timestamped, defined, and correctly distinguish zero from missing data;
- products have unique records, accurate states, working demos or explicit missing-demo labels;
- login/signup never pretends to work without a backend;
- tests, security checks, deployment result and rollback path are recorded;
- no fabricated metrics, live integrations, scientific proof, customer contact, sales, or income are shown.

## 12. Reporting format for every delivery

Report only:
1. files/routes changed;
2. implementation completed;
3. tests actually executed and results;
4. evidence links/artifacts;
5. failures and remaining blockers;
6. next single highest-value action.

**Current baseline warning:** the existing Character Studio HTML describes itself as a browser-local prototype, not a connected HeyGen avatar. Preserve that honesty while improving the experience. The immediate objective is to turn the public page into a navigable, evidence-backed product front door—not to add more empty modules or unsupported claims.
