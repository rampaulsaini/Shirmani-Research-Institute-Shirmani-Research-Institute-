# SHIRMANI — Measurable Production Chain & First Revenue Sprint
Version: 1.0
Date: 2026-10-09
Status: IMPLEMENTATION SPECIFICATION — proposals are not claims of completed production, sales, or income.

## Operating rule
Production is the primary work. QC, dispatch eligibility, and independent verification are downstream states. A scheduled workflow is not a finished product. A product counts as concrete only when its usable artifact exists and is linked from a public interface.

## One complete measurable chain
Institute research → product specification → factory build → concrete artifact → product-specific visual/demo/usage guide → QC and release gate → product passport + QR route → public showroom listing → offer/price and order/enquiry route → customer feedback → quality improvement → versioned release.

Each stage must emit a durable artifact or a clearly named blocker. Do not mark a stage complete merely because a workflow ran.

## Product state machine
- IDEA: opportunity recorded; no deliverable yet.
- SPECIFIED: audience, problem, inputs, outputs, limits, and acceptance checks written.
- BUILDING: implementation in progress.
- CONCRETE: usable file/page/tool exists and has a stable path.
- MEDIA_READY: product-specific screenshot/visual, demo script/video, and usage guide linked.
- QC_PASS: defined checks passed; store the QC report and gate code.
- SHOWROOM_READY: public listing, price/offer (or “quote required”), passport, and enquiry/order path visible.
- DISPATCH_READY: fulfillment steps and terms are explicit.
- SOLD: only after a real paid order is recorded through an authorized payment/order channel.
- IMPROVEMENT_QUEUED: feedback has been triaged into a versioned backlog.
- VERIFIED: reserved for independently checked claims/results; never inferred from workflow success.

## Minimum product record
Every product record should include: `product_id, name, version, family, problem, audience, inputs, outputs, limitations, artifact_url, visual_url, demo_url, usage_guide_url, passport_url, qr_url, price_inr_or_quote, offer_terms, qc_code, gate_status, dispatch_status, created_at, updated_at, feedback_count, improvement_issue_url`.
Unknown fields remain `null` or `NOT_READY`; never invent a URL, QC pass, customer, sale, or review.

## Priority work lanes
1. **Revenue-first services** — Hindi/English writing, source-based research summaries, website/blog content.
2. **Concrete browser tools** — Yatharth Learning Studio, Evidence-First Answer Builder, Digital Product Passport Maker, Voice-to-Presentation Planner; label integrations honestly.
3. **Product media** — product-specific screenshot/visual, short demo, usage guide, passport and QR route.
4. **Showroom** — searchable category, concrete deliverable, clear price/quote, limitations, enquiry/order route.
5. **Voice/live presentation** — authorized voice provider, speech recognition, contextual Q&A, evidence gate, TTS, face/avatar, lip-sync, end-to-end test. Do not claim live capability until integrations and tests actually pass.
6. **Feedback loop** — capture reviews only from real users, triage issues, ship versioned improvements.

## First revenue sprint: service offers to test
These are **proposed starting prices**, not established market rates or guaranteed sales. Confirm scope and price with each customer before work starts.

- **Quick writing/editing — ₹499 pilot**: up to 500 words or equivalent edit; one revision; customer supplies topic and any required sources.
- **Research summary — ₹999 pilot**: concise summary based on up to 3 customer-approved/public sources, with source links and explicit uncertainty notes.
- **Website/blog content — ₹1,499 pilot**: one page or one post up to 1,000 words, one revision, agreed brief and delivery date.

Before accepting an order, agree in writing on scope, deliverables, sources, word limit, delivery date, revisions, price, payment timing, and allowed use. Do not promise legal/medical/financial advice, guaranteed rankings, guaranteed results, or independent verification that was not performed.

### Enquiry-to-delivery checklist
1. Receive the brief through the published enquiry page or an explicitly authorized contact channel.
2. Clarify objective, audience, language, source material, word limit, deadline and budget.
3. Send a written scope/price confirmation; wait for customer approval.
4. Confirm payment terms using a real payment route; do not treat a draft as a payment.
5. Produce the agreed deliverable and cite sources where relevant.
6. Run a quality checklist; deliver the file/link.
7. Request optional honest feedback; do not fabricate testimonials.
8. Record order status and revenue only from actual confirmed records.

## Weekly public metrics
Publish counts with timestamp and source artifact:
- ideas recorded
- specifications completed
- concrete artifacts produced
- media-ready products
- QC pass / QC blocked
- showroom-ready listings
- enquiry briefs received
- quotes accepted
- paid orders confirmed
- revenue confirmed (INR)
- deliveries completed
- real reviews received
- improvements shipped
- voice/live gates passed / blocked.

Always show numerator and denominator. Example: `media_ready = 12 / 30 (40%)`. If the underlying manifest is unavailable, show `UNKNOWN`, not a guessed percentage.

## Voice → live presentation acceptance gates
1. Speech-to-text test with consented sample audio.
2. Context and intent test set with expected answers.
3. Evidence/source handling and insufficient-evidence tests.
4. Authorized voice provider configured and access secured.
5. Text-to-speech output test.
6. Avatar/face asset usage rights confirmed.
7. Lip-sync timing test with measured drift.
8. End-to-end latency and failure recovery test.
9. Respectful communication regression suite.
10. Live demo published with known limitations.
Any critical failure blocks the “production-ready” label; the remaining product lanes continue.

## Independent operation and security
Scheduled jobs may continue without a chat message only when the repository workflow is enabled, permissions are sufficient, schedules are valid, and runs succeed. Never expose API keys in code, artifacts, or logs. External email/social posting/payment actions require real provider integration, appropriate credentials, and explicit authorization. A plan or workflow file alone does not prove that an external action occurred.

## Definition of complete
The chain is complete for a given product only when the artifact is usable, public route resolves, visual/demo/guide/passport are linked or explicitly marked not applicable, QC state is recorded, offer/order path is clear, and customer feedback can be captured. The whole platform is not “100% complete” until counts are calculated from the live registry and each target has a defined denominator.
