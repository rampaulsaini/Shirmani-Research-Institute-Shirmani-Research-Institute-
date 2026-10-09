# SRI-OPS-001 — Client Brief Builder

**Purpose:** turn a prospective Hindi/English writing or research enquiry into a structured scope brief before quoting.

## Included in this prototype
- Service, language, audience, topic, word-count, deadline, sources, budget, deliverables, and constraints fields.
- Generates a plain-text scope summary and supports copy/download.
- Includes an explicit pre-acceptance checklist for scope, citations, timeline, revisions, price, payment, and confidentiality.
- Responsive, single-file HTML; input stays in the current browser page and is not sent to a server.

## Customer test
1. Open `products/concrete/SRI-OPS-001-client-brief-builder.html` in a modern browser.
2. Submit with the topic or deliverables empty; required-field validation should block generation.
3. Fill both required fields and generate the brief.
4. Confirm all entered values and the written pre-acceptance checklist appear.
5. Download the .txt and inspect it; test Copy on HTTPS or localhost.
6. Repeat on a narrow mobile viewport.

## Honest release state
- **Status:** prototype; manual browser acceptance pending.
- **QC / dispatch:** not approved / NO.
- **Pricing:** not set. No price, order, sale, income, customer contact, or delivery is claimed.
- **Not included:** server persistence, email/WhatsApp sending, checkout/payment, source verification, AI inference, automatic quoting, legal contract generation, actual MP4 demo, or captured VIP screenshot.
- **Known limitations:** dates are captured as requested dates without calendar/business-day validation; budgets are free text; generated output is a draft and requires human review.

## Release checklist
- [ ] Desktop and mobile browser test
- [ ] Required-field and special-character tests
- [ ] TXT download and copy tests
- [ ] Accessibility / keyboard pass
- [ ] Actual product screenshot captured after browser QA
- [ ] MP4 demo recorded against the final tested build
- [ ] Product passport / QR target checked
- [ ] Approved price, offer, terms, and order path configured
- [ ] QC acceptance recorded before dispatch is changed from NO
