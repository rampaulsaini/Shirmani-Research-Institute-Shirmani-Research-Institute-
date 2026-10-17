# SHIRMANI Product Uniqueness & Copy-Resistance Plan

**Status:** Implementation plan; not a claim of legal protection, patentability, or copy-proof security.  
**Goal:** Make each released product identifiable, attributable, difficult to clone wholesale, and easier to improve without harming existing useful work.

## 1. The realistic standard

No public website, image, prompt, interface, or digital product can be guaranteed impossible to copy. The practical target is layered copy-resistance: keep valuable implementation private where possible, publish only what customers need, establish provenance, apply enforceable terms, and make authentic releases verifiable.

## 2. Required layers for each product

1. **Distinct identity:** unique product ID, name, version, visual system, short description, and product-specific demo. Do not reuse generic demo media as proof.
2. **Provenance record:** record creator/owner assertions, creation date, source assets, third-party dependencies, licence terms, and the commit/release that introduced each material component.
3. **Product passport:** include version, features, limitations, supported environment, test status, licence, support scope, and upgrade history. A passport is documentation, not a security certificate.
4. **Public/private boundary:** publish the demo, usage guide and customer-facing output; keep credentials, signing keys, private datasets, unreleased source and sensitive server logic out of public pages and repositories.
5. **Access and secrets:** use least-privilege access, MFA where available, secret scanning, dependency updates, protected branches and reviewed changes. Never store API keys or customer secrets in client-side JavaScript.
6. **Authenticity checks:** use signed release manifests or checksums for downloadable artefacts where feasible; publish the official source location and version so customers can distinguish authentic releases from altered copies.
7. **Licensed use:** define permitted use, redistribution, modification, refunds, support and commercial rights before purchase. Have legal counsel review terms for the applicable jurisdictions; do not claim trademark, copyright registration or patent protection unless documented.
8. **Customer-specific traceability:** assign order IDs and versioned delivery records. Add unobtrusive watermark/provenance metadata only when appropriate and disclosed; never embed private customer data in public artefacts.
9. **Continuous improvement:** link feedback and reproducible bugs to product versions; preserve working releases, changelogs and rollback paths. Remove or filter an item only after confirming it is redundant or harmful and preserving required records.
10. **Evidence-led claims:** label each capability Planned, Implemented, Tested, Verified or Released. Keep the actual test evidence and date with the product record. A plan, screenshot or URL alone does not prove a working integration.

## 3. Release gate

A product should not be labelled “Verified” until the responsible reviewer records:

- [ ] Product ID and version are unique and consistent across the catalogue, demo and passport.
- [ ] All media/assets have a documented source and usage permission.
- [ ] No credentials, private keys or private customer data are exposed.
- [ ] Demo steps work in a clean browser/session and known limitations are visible.
- [ ] Accessibility, mobile layout and core customer journey have been checked.
- [ ] Licence, price, deliverables, support and refund/fulfilment terms are clear.
- [ ] Automated checks, manual test notes and release/rollback reference are recorded.
- [ ] Public claims match the evidence; pending items are not marketed as completed.

## 4. Practical order of execution

**P0 — Protect current work:** inventory repositories and external integrations; back up and review before any deletion; scan for exposed secrets; preserve all working product routes.

**P1 — Make the showroom understandable:** navigation, categories, consistent product cards, clear status labels, and one primary enquiry path.

**P2 — Make the first sale traceable:** customer brief, written quote, acceptance, payment confirmation, delivery record, and customer-approved feedback. Report revenue only from actual payment records.

**P3 — Protect each release:** product passport, licence terms, provenance, versioning, and authentic downloadable artefacts.

**P4 — Harden production:** least privilege, dependency and secret checks, server-side controls for sensitive operations, logging, backup/restore drills, and incident response.

## 5. Measurement

Track these numbers from actual records, not estimates presented as results:

- Share of public products with a unique ID, version, owner/source record and passport.
- Share of published products with a reproducible demo and dated QC evidence.
- Open high-severity security findings and time to remediation.
- Enquiries, written quotes, accepted quotes, confirmed payments, delivered orders, refunds and net revenue.
- Broken links, failed test cases, accessibility defects and rollback frequency.

**Non-negotiable:** never promise “impossible to copy,” “fully secure,” “globally scalable,” or “verified” without evidence that supports the exact claim.
