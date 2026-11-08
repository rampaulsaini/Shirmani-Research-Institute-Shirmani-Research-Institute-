# Shirmani Research Institute — Complete Platform Readiness Register

**Task ID:** SRI-READINESS-REGISTER-001  
**Snapshot date:** 2026-11-08  
**Repository:** `rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-`  
**Source inspection baseline:** `main` @ `c5d54496e4fb877ec0514d9afd9de19bffe47c14` (2026-11-05); **PR base at review:** `main` @ `0406c2ee8fffee4842a0dadbe6b1f4c12790f13f` (2026-11-08).  
**Change type:** Documentation only. No application code, configuration, credentials, database data, or deployment changed.

## Purpose and status rules

This register inventories the platform by capability and records the highest stage supported by repository/provider evidence at this snapshot. A stage is not a percentage of completion.

- **SPECIFIED** — a written requirement, contract, plan, or design exists; working implementation is not established.
- **PROTOTYPED** — a repository artifact or browser-local tool exists; production integration or end-to-end operation is not established.
- **TESTED** — a reproducible test or isolated validation is recorded for the stated scope. It does not imply production deployment.
- **DEPLOYED** — the named version is reported deployed to a real target. A deployment is not proof of health, data persistence, payment, or customer use.
- **VERIFIED** — independent/reproducible evidence confirms the stated acceptance criteria in the target environment.
- **NOT_CHECKED / NOT_VERIFIED** are evidence qualifiers, not extra completion stages. Missing evidence must remain missing.

A capability can have more than one state boundary (for example, API code may be deployed while its current health endpoint is NOT_CHECKED). This register deliberately avoids an overall platform completion percentage.

## Executive truth snapshot

**Fresh production evidence (2026-11-08):** `generated/product-qc-gate.json` was generated at `2026-11-08T01:55:13.890654Z`. Its scope is `PRODUCED_PRODUCTS_ONLY`: catalog identities 5,000; produced products 4,716; deterministic QC passed 4,716; failed 0; pass rate 100% within that produced subset. The remaining 284 catalog identities are outside this QC result. The gate explicitly states `independent_scientific_verification: false` and `sale_claim: false`; dispatch remains `NO` by default. This newer scoped QC record supersedes older `live-production-state.json` values of `READY_FOR_QC` and `qc_passed: 0` for QC status only. Do not interpret this as independent scientific verification or sales readiness.

The latest `generated/four-stage-production-status.json` snapshot is `2026-11-08T01:55:05.451161Z`; it reports 16,656 discovered modules and 5,000 catalogue products. Inventory labels such as READY are not deployment or operational proof. The latest inspected `generated/independent-verification-status.json` remains dated `2026-11-04T14:07:32.674830Z`: 63,950 prepared review records, 0 independently verified of 100,200. This verification snapshot is older than the QC snapshot and must be displayed with its own timestamp.

| Area | Evidence at snapshot | Readiness |
|---|---|---|
| Public entry and showroom | Static HTML pages and browser-local demos exist; README explicitly says key pages are prototypes and not connected to live AI, checkout, outreach, or sales. | PROTOTYPED; public live smoke NOT_VERIFIED |
| Product/catalog assets | `generated/four-stage-production-status.json` (2026-11-08) reports 5,000 catalogue products; `generated/live-production-state.json` is an older 2026-11-05 snapshot. | TESTED for recorded production/materialization scope; not all assets independently reviewed |
| QC | `generated/product-qc-gate.json` (2026-11-08T01:55:13Z): 4,716 produced, 4,716 deterministic QC pass, 0 fail; scope `PRODUCED_PRODUCTS_ONLY`. | TESTED: 100% of the 4,716 produced subset; remaining 284 catalogue identities not covered; independent verification separate |
| Independent verification | `generated/independent-verification-status.json`: 100,200 queued, 63,950 prepared, 0 verified, 100,200 unverified; human review required. | SPECIFIED / review preparation PROTOTYPED; VERIFIED count 0 |
| Customer income | Source state says sales_claimed 0, payment_claimed 0; no provider-confirmed paid transaction or accepted delivery is present in these snapshots. | SPECIFIED / PROTOTYPED; verified income ₹0 |
| Dispatch and delivery | `dispatch_released: 0`; no customer delivery confirmation established by these source files. | SPECIFIED; NOT_VERIFIED |
| API | PR #3645 merged; Render deployment was reported for commit `d94ac653d73ea842a75eecd93f4d122f6e49525a`. Current live health HTTP response was not checked in this register. | DEPLOYED (specific older commit); current runtime health NOT_CHECKED |
| Database | Schema/migrations exist. Render database provider reports available, but private connectivity and live counters were not readable because external DB access is blocked by the current allowlist. | PROTOTYPED; runtime connectivity NOT_VERIFIED |
| Genesis identity | PR #3653 merged; its PR description records isolated Neon validation and SELECT verification of the reservation row. Render deployment of the latest main API code is not established. | TESTED (PR-described Neon scope); Render endpoint NOT_VERIFIED |

## Module inventory

| Module / capability | Evidence in repository | Highest supported stage | Remaining proof / gap |
|---|---|---|---|
| Public hub / navigation | `index.html`, `public-interface-v3.html`, `README.md` | PROTOTYPED | Deployed root and all user journeys need fresh public smoke tests. |
| Public product showroom | `showroom/public-product-showroom.html`, `showroom/showroom-public-interface.html` | PROTOTYPED | Live availability, working links, customer usability and checkout are not verified. |
| Product catalog | `products/catalog.json` | PROTOTYPED | Entries are labelled previews; implementation and release evidence must be checked per product. |
| Micro browser tools | `products/micro-product-manifest.json` and listed HTML assets | PROTOTYPED | Individual functional tests, accessibility and user acceptance not established by manifest. |
| Product factory / materialization | `factory/build_factory.py`, `factory/batch_worker.py`, `factory/product_orchestrator.py`; generated production state | PROTOTYPED | Generated counts are not QC-approved customer-ready products. |
| Production orchestration | `factory/four_stage_production_orchestrator.py`, `factory/continuous_product_factory.py`, related workflows | PROTOTYPED | Repeated successful cycle, durable persistence and end-to-end public release need independent run evidence. |
| Product visual / QR generation | factory visual/QR modules; 5,000 assets reported in generated state | PROTOTYPED | Asset-by-asset uniqueness, correctness, rendering and release QC not established. |
| Product demo video / media | media factory scripts and showroom workbenches | PROTOTYPED | A script/shotlist is not a rendered, reviewed, published video. Actual media coverage and playback tests remain outstanding. |
| QC and release gates | `factory/product_qc_gate.py`, `factory/product_visual_qc_gate.py`, `generated/product-qc-gate.json` (2026-11-08T01:55:13Z) | TESTED | Deterministic QC PASS for 4,716/4,716 produced subset only; 284 catalogue identities not covered; human review, independent verification and dispatch remain separate. |
| Research source pipeline | `factory/build_factory.py`, `agents/source_agent.py`, `factory/README.md` | PROTOTYPED | Source coverage, freshness, rights, provenance and reproducible sample outputs need audits. |
| Research / writing agents | `agents/research_agent.py`, `agents/writing_agent.py`, `factory/agent-registry.json` | PROTOTYPED | Registry status labels are declarations, not proof of connected model runtime or client-grade output. |
| AI / ML / NLP | `agents/supreme_nlp*.py`, `agents/deep_learning_agent.py`, model registry and NLP workflows | PROTOTYPED | Active model/provider, runtime, benchmark dataset, latency, accuracy and safe fallback evidence not established here. |
| Evidence / provenance contracts | `agents/contracts.py`, `factory/independent_verification_engine.py` | PROTOTYPED | Independent human review and verified promotion remain at zero in the current verification snapshot. |
| Independent review ledger | `generated/independent-verification-status.json` | PROTOTYPED | 63,950 packets prepared; 0 independently verified; human review remains required. |
| API service | `server/package.json`, `server/src/`, PR #3645 | DEPLOYED (commit d94ac653… reported) | Live API health response, current deployed commit parity and full route smoke are NOT_CHECKED. |
| API authentication / owner controls | server auth and owner-only route code | PROTOTYPED | Production secret configuration, authorization tests and live owner access need verification. |
| PostgreSQL schema | `server/sql/schema.sql` and migration files | PROTOTYPED | Render DB connection, applied migration versions, backup/restore and counters NOT_VERIFIED. |
| Customer enquiry capture | PR #3645 adds consent-checked `POST /api/enquiry` and owner inbox path | DEPLOYED (specific commit d94ac653… reported) | Actual public HTTP POST, durable DB row, owner retrieval and consent record NOT_CHECKED in target environment. |
| Payment integration | Fail-closed payment webhook contract; PR #3650 remains an open proposal at snapshot | SPECIFIED / PROTOTYPED | No provider-confirmed transaction evidence; no payment is counted. |
| Order / dispatch / delivery | Production truth contract and dispatch workflow files | SPECIFIED | No released dispatch or customer-accepted delivery established by current state. |
| Income accounting / evidence | Production truth files and payment evidence proposal | PROTOTYPED | Provider event, paid order, matching amount/currency, customer consent and accepted delivery must be joined in private records. |
| Customer feedback / improvement | Customer review workflows and review-oriented showroom pages | PROTOTYPED | Persisted real customer reviews, consent, response and closed improvement loop NOT_VERIFIED. |
| Anant Studio / media storytelling | `docs/production/ANANT-STUDIO-*`, `showroom/anant-studio`-related assets and scripts | PROTOTYPED | Final rendered media, approved identity assets, publication and platform delivery proof remain separate gates. |
| Heart-View / character presentation | Character specs, rehearsal tools and QA documents | PROTOTYPED | Connected avatar/voice/lip-sync/streaming and real audience tests are not established by text briefs. |
| Email / WhatsApp | `showroom/external-integration-readiness.html` describes draft links | PROTOTYPED | No verified automated sender, inbound webhook, message delivery or reply integration. |
| Security baseline | `.github/workflows/*security*.yml`, security control-room pages | PROTOTYPED | Latest complete gate results, runtime security review and authorized penetration-test evidence not established here. |
| Backup / disaster recovery | backup workflow and continuity documentation | SPECIFIED / PROTOTYPED | Successful restorable backup in a separate private destination and timed restore drill NOT_VERIFIED. |
| Automission scheduling | numerous GitHub Actions workflow definitions | PROTOTYPED | Workflow definitions and individual runs do not prove uninterrupted 24/7 operation or external side effects. |
| Yatharth Genesis identity | PR #3653 merged; PR description records isolated Neon tests and reservation-row SELECT | TESTED (scope limited to PR evidence) | Render API deployment parity and public `/api/yatharth/verify/:accountId` response NOT_VERIFIED. No wallet, token, funds or exchange functionality is implied. |
| Etsy digital art | Research/listing concepts only; no seller integration evidenced | SPECIFIED | Seller account, GSTIN status, Payoneer, rights review, fee and listing publication pending. |
| Global prospecting / CRM | prospect and outreach workbench pages | PROTOTYPED | No automatic mass outreach; actual messages, replies and customer stages require sender/provider and customer-record evidence. |

## Priority backlog — ordered for income and platform safety

| Priority | Work item | Acceptance evidence required | State |
|---|---|---|---|
| P0 | First paid writing/research/admin pilot | Named customer, written scope/quote acceptance, provider-confirmed payment, deliverable, customer acceptance, private verified-income record | NOT_VERIFIED |
| P0 | Public enquiry-to-owner-inbox path | Public form submission, consent, HTTP result, private PostgreSQL row, owner-only retrieval test | NOT_VERIFIED |
| P0 | Payment-provider evidence gate | Provider signature/transaction verification, amount/currency match, idempotency, consent, paid order row | NOT_VERIFIED |
| P0 | Render/API/DB health parity | Live commit SHA, `/api/health`, DB-backed `/api/ready`, migration state, safe logs, counters | NOT_CHECKED |
| P1 | Public showroom smoke and product release QC | Fresh deployed URL tests, sampled product interaction tests, catalog-matched QC pass and user acceptance | NOT_VERIFIED |
| P1 | Backup and restore | Private offsite backup artifact, integrity check and successful restore drill | NOT_VERIFIED |
| P1 | Security hardening | No fake secrets, safe CORS/JWT config, rate-limit/auth checks, security gates and authorized scope | NOT_VERIFIED |
| P1 | Existing product visual PR review | Sample quality, manifest reconciliation and required checks for existing PR #2452; do not regenerate duplicate assets | OPEN / REVIEW REQUIRED |
| P2 | Independent verification | Human-reviewed source/evidence packets with reviewer identity, method, decision and reproducible record | 0 verified |
| P2 | AI/ML/NLP runtime | Declared provider/model, successful runtime trace, benchmark, quality metrics, failure/fallback tests | NOT_VERIFIED |
| P2 | Media and Anant Studio publication | Approved source assets, rendered output, playback/format QA and platform publication receipt | NOT_VERIFIED |
| P2 | Etsy listing readiness | Official onboarding eligibility, GSTIN/Payoneer prerequisites, rights-cleared files and owner-approved listing | BLOCKED / NOT_VERIFIED |

## Anti-duplication and authorization controls

- Preserve merged work. PR #3645 and PR #3653 are confirmed merged; do not recreate them.
- PR #3659 is an open four-stage production PR, not the safe-startup task. Existing safe-startup work is already represented by open PRs #3663 (draft) and #3664 (open). Do not create a duplicate safe-startup PR.
- PR #3650 remains open and proposes private exports/payment-evidence gates; do not claim its migrations are applied.
- Existing product visual PR #2452 remains a review item; do not regenerate its assets.
- This register is documentation only. It does not authorize merge, deployment, restart, migration, database write, allowlist change, secret disclosure, payment, or customer outreach.
- Any external message requires explicit owner approval for the exact recipient/content/channel. Any security test requires written domain-owner authorization and scope.
- Workflow success, generated files, a static link, an invoice, a payment intent, or a PR merge alone never proves a customer payment or accepted delivery.

## Canonical evidence sources

- [README.md](README.md) — explicit public prototype boundaries and product index.
- [PROJECT-CONTINUITY.md](PROJECT-CONTINUITY.md) — continuity and anti-duplication rules.
- [generated/continuation-ledger.json](generated/continuation-ledger.json) — prior completed/open work; snapshot last updated 2026-11-01.
- [generated/product-qc-gate.json](generated/product-qc-gate.json) — generated 2026-11-08T01:55:13.890654Z; authoritative deterministic QC scope is PRODUCED_PRODUCTS_ONLY (4,716/4,716 produced subset).
- [generated/four-stage-production-status.json](generated/four-stage-production-status.json) — generated 2026-11-08T01:55:05.451161Z; inventory and production snapshot, not deployment proof.
- [generated/live-production-state.json](generated/live-production-state.json) — older snapshot generated 2026-11-05T01:57:53.898952Z; do not use its QC 0/0 fields to override the newer QC gate.
- [generated/independent-verification-status.json](generated/independent-verification-status.json) — generated 2026-11-04T14:07:32.674830Z.
- [products/catalog.json](products/catalog.json) — product preview and QC boundaries.
- [products/micro-product-manifest.json](products/micro-product-manifest.json) — runnable micro-tool asset list; explicitly not sales/verification proof.
- [factory/agent-registry.json](factory/agent-registry.json) — declared agent roles and safeguards.
- [agents/contracts.py](agents/contracts.py) — provenance and publication eligibility contract.
- [server/README.md](server/README.md) — API foundation and explicit non-live integration boundaries.
- [showroom/external-integration-readiness.html](showroom/external-integration-readiness.html) — email/WhatsApp/UPI/PayPal/Yatharth channel evidence boundaries.
- [PR #3645](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/pull/3645) — enquiry/API changes, merged.
- [PR #3653](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/pull/3653) — Genesis identity registry, merged.
- [PR #3650](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/pull/3650) — private exports/payment evidence, open.
- [PR #3659](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/pull/3659) — existing four-stage production work, open.
- [PR #3663](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/pull/3663) and [PR #3664](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/pull/3664) — existing safe-startup proposals, open.

## Reconciliation and evidence freshness rule

When generated sources disagree, select the newest source that explicitly covers the metric and scope being reported; do not let a newer unrelated snapshot override it. Record each source timestamp independently. For QC, `product-qc-gate.json` is authoritative for its `PRODUCED_PRODUCTS_ONLY` scope. For independent verification, retain the timestamped verification-status file until a newer registry snapshot exists. For dispatch, sales and payment, require their own direct event/provider evidence; QC PASS never advances those states.

## Next review rule

Update this register only when a source, test, deployment, provider response, or customer record changes. Record the exact commit, timestamp, URL, test scope and limitation. Never upgrade a status from a workflow label or plan alone.
