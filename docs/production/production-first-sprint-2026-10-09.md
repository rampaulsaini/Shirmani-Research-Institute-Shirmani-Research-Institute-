# SHIRMANI Production-First Sprint — 2026-10-09

## Purpose

Move work from scheduled automation into concrete public product assets and customer-ready deliverables. This is a production plan and measurement contract, not a claim that all listed work has already shipped.

## Source-of-truth snapshot

Read from `generated/live-production-state.json` (generated 2026-10-07T00:33:56Z):

- Catalog identities: **5,000**
- Concrete repository assets: **1,516**
- Concrete materialization: **30.32%**
- Remaining to the current 5,000-asset target: **3,484**
- Dispatch released: **0**
- Sales claimed: **0**
- Payments claimed: **0**
- Independent verification claimed: **0**

These counts describe production state only. They do not mean 1,516 products have passed customer acceptance, are dispatched, or have sold.

## Required production chain

`INSTITUTE → FACTORY → QC/GATE → SHOWROOM → ORDER → PAYMENT → DISPATCH → CUSTOMER FEEDBACK → IMPROVEMENT`

The first four stages are not sufficient to claim a sale. Each stage must persist its own state and timestamp. Do not infer payment, dispatch, customer satisfaction, or independent verification from a workflow's green status.

## Priority A — unblock concrete production persistence

1. Keep generated product artifacts on `automation/production-state`; do not push directly to protected `main`.
2. Persist lane-sharded outputs and compact manifests; do not push a single JSONL file larger than GitHub's 100 MB limit.
3. Treat any publish/push failure as a production blocker even if asset generation succeeded.
4. Record per-run: input catalog count, created count, existing count, failed count, output paths, commit SHA, and remaining count.
5. After the next run, confirm that the canonical state branch advanced and the public index reads that persisted state.

**Acceptance:** the run creates at least one new concrete product when backlog exists, persists its artifact and manifest, and reports accurate remaining work. A successful generation step without successful persistence is not a completed production cycle.

## Priority B — concrete product definition

A catalog identity becomes a concrete product only when it has:

- A working, product-specific HTML/module route (not just a name or generic placeholder)
- A useful short description and a step-by-step usage guide
- A product-specific demo asset and VIP visual/screenshot
- A product passport with a product-specific QR route
- A price/offer state that is explicit; use “quote after scope” when no price has been approved
- QC code, gate state, and dispatch state
- A feedback route that records a review locally or through a connected backend, with its actual storage scope clearly stated

Keep asset coverage counters separate: concrete modules, QR assets, product visuals, VIP screenshots, MP4 demos, and public routes. Do not use one coverage count as a proxy for all others.

## Priority C — showroom and customer-facing revenue

The first immediately serviceable offer is **Hindi/English writing and research**:

- Writing, research summary, or website/blog content
- Confirm scope, language, word count, deadline, sources, deliverables, and budget before accepting work
- Confirm price, payment terms, and delivery date in writing before work starts
- Do not label an enquiry as a customer, an offer as a sale, or a proposal as income
- Track leads, proposals sent, replies, confirmed scopes, paid orders, delivered work, and received payments as separate counts

### Seven-day operating targets (targets, not completed results)

- 10 tailored, relevant outreach messages sent through an authorised channel
- 3 suitable proposals prepared
- 1 paid pilot target
- 100% of enquiries logged with next action and status
- 0 unconfirmed sales or income claims

If no authorised outbound integration is connected, prepare copy-ready outreach and log it as **not sent** until the user actually sends it.

## Priority D — voice-to-live presentation

Keep this as a separate product lane:

`VOICE → AUTHORISED VOICE → STT → CONTEXT/NLP → EVIDENCE STATE → RESPONSE → TTS → FACE/AVATAR → LIP-SYNC → LIVE → AUDIT`

A browser prototype is not a connected AI service, cloned/authorised voice, photorealistic lip-sync, or live broadcast. Mark each integration as `NOT_CONNECTED`, `TESTING`, or `LIVE_TEST_PASSED`. Do not mark the whole lane live while a critical gate is not passed.

## Daily production dashboard fields

- `catalog_identities`
- `concrete_modules_created`
- `concrete_modules_remaining`
- `qr_assets_ready / qr_assets_target`
- `visuals_ready / visuals_target`
- `vip_screenshots_ready / target`
- `real_mp4_demos_ready / target`
- `public_routes_reachable / target`
- `publish_status` and persisted commit SHA
- `enquiries`, `proposals_sent`, `paid_orders`, `payments_received`
- `dispatch_released`
- `customer_reviews_received` and `improvement_items_created`

## Next measurable milestone

Raise concrete repository assets from **1,516** to **1,616** (+100) while persisting every artifact and updating the public state. This is a target, not a claim that the batch has already run. Then continue in batches until the current 5,000 target is reached, while keeping module and media coverage independently measured.

## Truth and preservation rules

- Preserve immutable user-source records verbatim.
- Keep philosophical/identity statements distinct from independently verified factual claims.
- Do not claim an integration, outreach, sale, payment, dispatch, product demo, or verification is complete without its corresponding persisted evidence.
- Prefer useful, runnable products over adding more workflow names.
