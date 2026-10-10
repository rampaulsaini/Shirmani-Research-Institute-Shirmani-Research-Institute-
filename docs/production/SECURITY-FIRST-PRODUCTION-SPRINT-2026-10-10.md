# Security-First Production Sprint — 2026-10-10

## Purpose
Prioritize security hardening and tangible product production together. This is a plan, not a claim that infrastructure has been scanned, secured, or that sales have occurred.

## Repository baseline
- Repository: `rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-`; default branch: `main`; public repository.
- Existing public surfaces include a production-first map, public product showroom, security command center, client service desk, writing/research offer, product-launch kit builder, and voice-to-presentation prototypes.
- The writing/research service page lists proposed pilot rates: proofreading up to 1,000 words ₹299; short article/product copy ₹599+; source-organized research brief ₹999+; research-to-presentation outline ₹799. These are proposed prices, not market validation, orders, or income.
- Browser-local prototypes must not be described as hosted AI, automatic outreach, live video generation, checkout, or shared cloud storage unless those integrations are implemented and tested.

## Layer A — Security hardening
1. Inventory every workflow in `.github/workflows/`; classify triggers, permissions, third-party actions, write operations, deployment credentials, and external effects.
2. Use least-privilege workflow/job permissions; default to `contents: read`, granting write permissions only to the job that needs them.
3. Pin third-party Actions to reviewed full commit SHAs and document update cadence.
4. Never print secrets, tokens, environment dumps, or authenticated URLs in logs. Rotate credentials suspected of exposure and store them only in GitHub Secrets/Environments.
5. Require explicit approvals for production deployments and external outreach where repository settings support them.
6. Prevent untrusted pull-request code from receiving privileged secrets; review `pull_request_target` patterns and shell interpolation of untrusted input.
7. Enable dependency and secret scanning where available; triage findings by severity and exploitability.
8. Review HTML/JS for unsafe DOM sinks, remote script dependencies, untrusted URL handling, and accidental collection of private customer data.
9. Keep exportable manifests/backups for product records and document restore steps.
10. Publish a dated status with evidence and unresolved risks. A checklist is not a penetration test or security certification.

## Layer B — Production lanes
Move each product through:
`IDEA → SPECIFIED → BUILT → DEMO_READY → QC_REVIEW → PUBLISHED → ORDERABLE`

Every product record should contain:
- stable product ID and distinct name;
- intended user, problem, supported uses, limitations and usage instructions;
- concrete executable artifact or explicit service deliverable;
- product-specific screenshot/image and demo video/script (never claim an MP4 exists unless rendered);
- version, changelog, price/currency, offer expiry if applicable, licence/refund terms;
- QR destination pointing to a stable public product passport or guide;
- QC checklist and dispatch gate code;
- customer feedback field and linked improvement ticket;
- current state and evidence URL.

A name, placeholder card, workflow run, or rough module is not a built product. A product is not orderable until scope, price, delivery, contact route and fulfilment terms are visible.

## Layer C — First real income path
Start with deliverables that can actually be produced: Hindi/English editing, short articles/product copy, source-organized research briefs, and research-to-presentation outlines.

1. Build a prospect list only from official public organisation contact pages and relevant public business contacts.
2. Record organisation, official source URL, relevance, public contact route, date checked and reason for fit.
3. Draft a specific, respectful message offering one concrete deliverable; no spam, fabricated relationship, or false claims.
4. Human-review each recipient and message before sending. Do not automate email/WhatsApp until an authorized provider, consent/compliance rules and delivery logging are implemented.
5. Confirm scope, price, deadline, revisions and payment terms in writing before work begins.
6. Track researched prospects, reviewed messages, messages actually sent, replies, qualified enquiries, quotes, accepted quotes, delivered jobs, invoices and cleared payments separately.
7. Count revenue only when a real payment record exists; clicks, workflow runs, messages and proposals are not revenue.

## Layer D — Measurable production dashboard
Report separate counts for:
- products with executable artifacts;
- products with product-specific demo, screenshot, passport and guide;
- products that passed QC;
- products publicly published;
- products with complete order/fulfilment terms;
- official prospects researched;
- messages reviewed and actually sent;
- replies, qualified leads, accepted proposals, delivered jobs and payments received;
- security findings open/fixed/accepted with rationale;
- successful/failed automation runs, distinct from production outputs.

Do not fabricate percentages. If a denominator or source record is missing, display `UNKNOWN`.

## Layer E — Release gates
- **Security:** no known critical exposed secret or unresolved untrusted-code privileged path for the release.
- **Product:** working artifact and product-specific instructions/demo evidence exist.
- **Claims:** feature and quality claims match what was actually tested.
- **Commercial:** price, deliverables, delivery window, revision and payment terms are clear.
- **Publication:** no private data, credentials, misleading testimonial, fake review or unsupported guarantee.
- **Continuity:** queue cursor and result artifacts are saved so scheduled runs can resume safely.

## Immediate next actions
1. Inspect workflow files and classify permissions/triggers before changing deployment behavior.
2. Produce a workflow security inventory with path, risk, evidence, fix and owner.
3. Finish one existing concrete writing/research product's public passport, usage guide, demo script and screenshot.
4. Keep service offer and enquiry route prominent on the public homepage.
5. Build a small official-source prospect list and review messages manually.
6. Record actual results on the public production board after each completed step.

## Limitations
This document does not itself change GitHub security settings, execute a penetration test, send external messages, create video files, connect payment processing, or prove revenue. Each requires a separate implementation and evidence.
