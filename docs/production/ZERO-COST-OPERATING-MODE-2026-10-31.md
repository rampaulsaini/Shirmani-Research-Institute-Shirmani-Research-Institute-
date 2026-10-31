# Shirmani Research Institute — Zero-Cost Operating Mode

Date: 2026-10-31
Decision: ZERO-COST ONLY until the owner explicitly approves spending.

## Non-negotiable cost controls
- Do not create paid hosting, paid databases, subscriptions, domains, add-ons, or billing commitments.
- Do not enter or attach a payment method or start a paid trial that can convert to billing.
- Do not assume that a free tier is permanent, production-grade, backed up, or continuously available.
- Re-evaluate paid infrastructure only after the owner has funds and gives explicit approval.

## What can run at zero cost now
1. **GitHub Pages:** keep the existing public static showroom and service pages.
2. **Existing GitHub repository:** preserve the current catalogue and tools; use repository history and pull requests for auditable changes.
3. **Customer contact:** use the existing WhatsApp/email draft links as manual enquiry routes. They open a draft; they do not send a message automatically or create a server-side lead record.
4. **Sales records:** maintain a human-reviewed, privacy-conscious record of enquiry → agreed scope/quote → independently verified payment → delivery → customer acceptance. Never mark a stage complete without evidence.
5. **Production proof:** report only repository commits, successful workflow runs, published pages, and independently checked outputs that have actually been verified.

## Important technical boundary
GitHub Pages is static hosting. It cannot run the existing Express/Node.js API or host PostgreSQL. A static browser-only form can prepare a brief, open email/WhatsApp, or create a local draft, but it cannot provide reliable cross-device server persistence, secure accounts, payment verification, or a 24/7 worker.

Render Free may be used only for disposable experiments if available and if it requires no payment commitment. Its free database is time-limited and its free web service can sleep; neither is a dependable permanent production database/24×7 runtime. Do not represent such a test as production income infrastructure.

## Current income-first sequence
1. Keep the existing Writing & Research enquiry page and samples visible on GitHub Pages.
2. Make the service scope, deliverables, proposed price, deadline, revision limit, and payment terms explicit before accepting an order.
3. Use the existing manual contact route; do not scrape or bulk-message prospects.
4. Confirm a real customer request and written agreement before beginning paid work.
5. Verify payment independently before marking revenue or starting work under prepaid terms.
6. Deliver the agreed work and record customer acceptance.
7. Use the first genuine revenue to decide whether persistent API/database hosting is affordable.

## Status that must remain explicit
- Website: GitHub Pages static storefront (verify current live deployment separately).
- Backend API: not established as a deployed production service by this decision.
- Persistent server-side enquiries: not established.
- 24/7 workers/heartbeats: not established.
- Verified customers, payments, and revenue: report only from evidence; do not infer them from page clicks, drafts, workflow runs, or proposed prices.

This document is a zero-cost operating decision and checklist, not evidence that a customer, payment, deployment, or production worker exists.
