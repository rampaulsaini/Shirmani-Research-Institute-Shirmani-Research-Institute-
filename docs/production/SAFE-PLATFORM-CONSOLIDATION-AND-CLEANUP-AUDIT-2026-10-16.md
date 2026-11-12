# SHIRMANI Safe Platform Consolidation & Cleanup Audit
Date: 2026-10-16
Status: Audit plan and repository-backed findings; no production file deleted.

## Non-negotiable safety rule
Remove only an item proven to be redundant, unused, unreferenced, and safe to retire. A matching title, similar styling, or repeated topic is not proof of duplication. Do not delete source assets, original media, canonical pages, customer data, security checks, workflows, or provenance. Prefer redirects/compatibility stubs and staged retirement over immediate deletion. Every destructive change must have a reviewed diff, reference search, deployment check, and rollback path.

## Verified current state
- The Heart-View preview is present on `main`: `showroom/shirmani-supreme-heart-view-preview.html`.
- The preview explicitly labels live avatar/provider capabilities as not verified.
- The income launch plan is `docs/income/VERIFIED-WRITING-RESEARCH-LAUNCH-SPRINT-2026-10-16.md`; it records pilot prices as proposals and prohibits unsupported sales/payment claims.
- `showroom-products.json` distinguishes repository-backed artifacts from external catalogue paths whose evidence is unverified.
- `factory/REPOSITORY-INTELLIGENCE-AUDIT.md` already warns against blindly duplicating automation and calls for duplicate detection, source traceability, schema validation and controlled publication.
- `README.md` documents multiple browser-local tools and their boundaries; browser-local prototypes must not be described as connected AI, live provider integrations, email senders or payment systems.

## Initial service-surface audit
These pages are similar in subject but not interchangeable based on the current evidence:

| Path | Distinct role visible in source | Initial disposition |
|---|---|---|
| `services-writing-research.html` | Hindi-first service menu with proposed starting prices and mailto CTA | Keep pending live link/reference check |
| `writing-research-services.html` | English service menu with different offer/pricing copy and enquiry links | Keep pending live link/reference check |
| `writing-research-enquiry.html` | Public client intake form | Keep; intake is a different job from service marketing |
| `showroom/writing-research-enquiry-builder.html` | Local enquiry brief builder | Keep until canonical navigation and incoming references are checked |
| `showroom/revenue-ready-writing-research-studio.html` | Service-menu/brief-generation helper | Candidate for consolidation review, not deletion |
| `showroom/first-client-deliverable-studio.html` | Drafting scaffold and human release checklist | Keep; distinct deliverable-production function |
| `products/concrete/SRI-WR-001-writing-research-enquiry-studio.html` | Product-specific enquiry studio | Candidate for a canonical-link/redirect review after reference and behavior tests |

The pages have different content, languages, prices, and/or functions. This audit therefore does **not** authorize deleting them.

## Required duplicate filter
For every proposed retirement, record:
1. Exact path, blob SHA, size, last relevant change, and owner/purpose.
2. Exact-content hash plus normalized-content similarity; report similarity as a lead, not proof.
3. Incoming references in `README.md`, JSON catalogs, HTML links, workflow scripts, sitemap/manifest files, tests and external public URLs where discoverable.
4. Whether the page owns unique behavior, accessibility support, language coverage, metadata, pricing, forms, or user-facing content.
5. Public Pages HTTP status and behavior before/after the change.
6. Replacement/canonical URL and redirect/compatibility plan.
7. Rollback commit and post-deploy smoke-test evidence.

Decision states: `KEEP`, `CONSOLIDATE`, `REDIRECT`, `RETIRE_AFTER_DEPLOY_CHECK`, or `NOT_VERIFIED`. Do not auto-delete based on filename, age, similarity score, low traffic, or a cancelled workflow.

## Production verification gates
- [ ] Confirm the deployed Pages URL for the Heart-View preview and record the exact commit.
- [ ] Confirm the current public service/enquiry pages resolve on mobile and desktop.
- [ ] Check JSON validity and required fields in `showroom-products.json`; never mark external paths verified just because they are listed.
- [ ] Review cancelled/pending workflows individually; distinguish cancellation, queueing, failure and success.
- [ ] Inspect the cancelled Read-Only Security Baseline run before deciding whether rerun is safe.
- [ ] Validate media only against an approved original asset and its actual computed hash; do not invent a reference hash.
- [ ] Keep HeyGen voice, lip-sync and live Q&A as `NOT VERIFIED` until a real end-to-end artifact/test exists.
- [ ] For paid services, distinguish proposal, enquiry, quote, written acceptance, delivery and received payment as separate states.

## Canonical product and income path
For the first measurable income lane, promote one clear entry point for Hindi/English writing and source-based research, then link the supporting enquiry form and deliverable studio. Keep existing URLs working while references are audited. Proposed prices remain proposals until confirmed in writing with a client. No outreach, order, revenue or payment is claimed by this document.

## Exit criteria
Cleanup is complete only when each retired route has an approved replacement, references have been checked, deployment tests pass, the rollback is documented, and the post-deploy verification record is linked. Otherwise retain the route and label the item `NOT_VERIFIED`.
