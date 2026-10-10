# SRI Public Product Production Sprint — 2026-10-10

Status: proposed implementation plan; not a claim that production or sales have occurred.

## Goal
Prioritize concrete products that a customer can inspect, test, understand, request, and eventually purchase. Production work comes before expanding the catalogue count.

## First release lane: Hindi/English Writing & Research
1. Confirm scope, language, audience, word count, deadline, sources, budget and revision terms.
2. Produce an actual agreed deliverable (outline, research summary, or website/blog draft).
3. Record the artifact path, version, delivery date, limitations and source list.
4. Publish a product-specific demo/example that contains no private customer data.
5. Publish an accurate usage guide and screenshot for the same version.
6. Offer a transparent quote and enquiry route. No payment or sale is recorded until the transaction actually occurs.
7. Collect customer feedback through an actual available channel and turn actionable feedback into a versioned issue.

## Required product record
- Product ID, name, version, category and intended audience
- Problem, required inputs, concrete outputs and limitations
- Artifact URL, demo URL, screenshot URL and usage-guide URL
- Price or explicit quote required label; dated offer terms
- QC state and a link to the actual test report
- Passport URL and QR destination (only after the passport URL exists)
- Enquiry/order route and fulfillment conditions
- Feedback count and versioned improvement issue

Unknown values must remain NOT_READY or null. Never invent product URLs, videos, QC codes, reviews, customers, sales, income or independent verification.

## Four production stages
1. Institute / Research: define customer problem, sources, acceptance criteria and specification.
2. Factory / Build: create the actual usable artifact and its product-specific demo/guide.
3. QC / Release gate: run documented checks and record pass/fail evidence. QC must not replace production work.
4. Showroom / Sale: expose the artifact, accurate description, version, price/quote, demo, guide, passport and enquiry route. Mark sold only after a real paid order is recorded.

## Automation and security
- Scheduled workflows may continue without a user chat only when repository schedules, permissions/secrets, and successful executions are verified.
- Never store API keys, passwords, private customer content or voice credentials in public files or logs.
- External email, WhatsApp, checkout, payment, avatar/voice, MP4 rendering and QR generation are not considered live until a real authorized integration passes an end-to-end test.
- Do not mass-contact organizations without a lawful, relevant outreach basis, sender authorization, rate limits, opt-out handling and an auditable message log.
- Public reviews can inform product improvements, but private data should be removed and feedback must not be represented as independent scientific verification.

## Weekly measurable outcomes
Report counts from durable artifacts: concrete product pages added, working demos tested, guides and screenshots linked, QC reports passed/failed, quotes sent through an actual channel, paid orders recorded, deliverables completed, feedback items triaged and fixes released. Do not use workflow-run counts as a proxy for finished products.

## Acceptance gate for a showroom-ready product
A product is showroom-ready only when the public listing opens and includes a real artifact/demo, version, intended use, inputs/outputs, limitations, guide, product-specific visual, price or quote status, and a working enquiry path. MP4, QR, QC and order/payment states must each be truthful and separately tracked.
