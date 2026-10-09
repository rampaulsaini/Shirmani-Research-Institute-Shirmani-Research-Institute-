# Production-First Execution Board — 2026-10-09

## Objective
Move concrete customer-usable products to the public showroom. Workflow count, catalog identities, generated placeholders, and verification activity are not substitutes for finished product functionality.

## Four-stage chain
1. **Institute / Discovery** — define a specific customer problem, target user, intended use, constraints, and source material.
2. **Factory / Production** — build the usable product module and its product-specific usage demo.
3. **QC / Gate** — test advertised actions, links, limitations, and claims.
4. **Showroom / Sale** — publish name, version, short description, price or quote-required status, screenshot/visual, demo, usage guide, passport/QR route, and enquiry/order path.

A catalog ID or HTML route alone does not make a product sale-ready. A demo fallback must not be described as a finished MP4 or a connected live integration.

## First production batch: paid-service tools
Prioritize these concrete deliverables because the institute currently offers Hindi/English writing and research:
- **SRI-WR-01 — Writing & Research Brief Builder:** collect service, language, topic, purpose, word count, deadline, source links and budget; create a user-reviewed email draft.
- **SRI-WR-02 — Scope & Quote Sheet:** convert a brief into deliverables, exclusions, revision count, timeline, proposed fee and payment terms for written customer approval.
- **SRI-WR-03 — Source-Based Research Brief Template:** organize question, method, source list, key findings, uncertainty, counter-evidence and references.
- **SRI-WR-04 — Delivery QC Checklist:** check scope match, language, source links, citations, word count, formatting and agreed revisions.
- **SRI-WR-05 — Customer Feedback to Improvement Ticket:** capture rating and concrete change request; export a local JSON ticket. Do not claim shared aggregation unless a backend is connected.

## Required product passport fields
`product_id`, `name`, `version`, `customer_problem`, `intended_user`, `how_to_use`, `inputs`, `outputs`, `limitations`, `price_status`, `demo_url`, `screenshot_url`, `usage_guide_url`, `qc_status`, `dispatch_status`, `last_updated`.

## State vocabulary
- `DRAFT`: concept only.
- `BUILT`: concrete artifact exists.
- `DEMO_READY`: the advertised demo is usable.
- `QC_PASS`: documented functional checks passed for a named version.
- `PUBLISHED`: public route is deployed and reachable.
- `SALE_READY`: scope/price or quote path and delivery terms are visible.
- `ORDERED`, `PAID`, `DISPATCHED`: use only with actual records.
- `INDEPENDENTLY_VERIFIED`: reserve for independent verification evidence; not a prerequisite for ordinary production work, but required for claims that explicitly depend on independent verification.

Never infer one state from another. `PUBLISHED` is not `PAID`; `QC_PASS` is not independent scientific verification.

## Measurable weekly execution
Record actual counts from repository artifacts, not estimates:
- concrete product modules built;
- product-specific demos and screenshots published;
- products with complete passports and usage guides;
- products passing functional QC;
- products with a visible price or quote-required path;
- relevant prospects researched;
- personalized proposals actually sent;
- replies, agreed scopes, delivered jobs, and payments confirmed by evidence.

For each scheduled run, publish a concise delta report: items attempted, items completed, failures, links to artifacts, and next batch. If a task fails, record the reason and retry policy; never increase completion counts on a failed run.

## Revenue integrity
Currently listed starting rates are proposals, not proof of market demand or income: proofreading from ₹499, article/website copy from ₹999, and source-based research briefs from ₹1,499. Confirm scope, deliverables, deadline, revision policy and payment terms in writing before starting. Count revenue only after actual payment is evidenced.

## Immediate human-executable action
1. Open the live service page and confirm the proposed packages and contact route.
2. Identify five relevant public prospects manually; record the exact public page and one genuine content gap for each.
3. Send only individually tailored, relevant proposals through an authorized channel.
4. Record sent status only after sending; do not count drafts as outreach.
5. For a positive reply, send a scope-and-quote sheet; start only after written agreement.

## Automation boundaries
Scheduled repository workflows may continue without an active chat only while GitHub Actions, permissions, quotas, schedules and required external services remain available. This document does not itself start a workflow, connect external AI/voice/email/payment providers, contact prospects, or guarantee continuous uptime.
