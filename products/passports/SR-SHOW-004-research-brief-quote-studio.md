# Research Brief & Quote Studio — Product Passport

- **Product ID:** SR-SHOW-004
- **Version:** 1.0.0
- **Category:** Writing & Research Operations
- **Release state:** DEMO_READY (browser-only prototype)
- **Demo:** [Research Brief & Quote Studio](../showroom/research-brief-quote-studio.html)
- **Catalogue:** [products/catalog.json](../products/catalog.json)
- **Price:** Free browser demo. Writing/research services are quoted separately after scope confirmation; displayed starting rates are proposals, not validated market prices.

## What works
- Collects service type, language, word-count range, deadline, budget, goal, topic, source links and deliverable format.
- Generates a structured project scope and pre-work agreement checklist in the browser.
- Offers copy, TXT download and print/save-to-PDF actions.
- Clearly labels the output as a draft, not a contract, sent message, accepted order or payment record.

## Not implemented / limitations
- No server persistence, authentication, payment checkout, email/WhatsApp sending, CRM integration or automatic source verification.
- No product-specific MP4 demo or approved 4K product artwork is attached yet; the interactive HTML page is the reproducible demo.
- Prices and sales are not market-validated; no customer or revenue is claimed.

## Production release gates
1. Exercise every form field and test copy/download/print in desktop and mobile browsers.
2. Review accessibility, input handling and browser compatibility.
3. Add approved unique product artwork, screenshot and a narrated demo video.
4. Add server-side lead storage only with consent, privacy notice and access controls.
5. Add email/WhatsApp provider integration only after authorized credentials and end-to-end tests.
6. Configure checkout only after payment provider, refund terms, tax handling and order receipts are implemented.
7. Promote to RELEASED only after the above release gates and evidence are recorded.

## Real-income workflow
Lead → scope draft → human-approved quote → written acceptance → payment confirmation → delivery → feedback. This tool only supports the scope-drafting step; it does not claim or automate the remaining steps.
