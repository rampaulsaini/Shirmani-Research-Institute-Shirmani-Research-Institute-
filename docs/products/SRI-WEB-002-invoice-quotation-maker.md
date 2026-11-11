# SRI-WEB-002 — Invoice & Quotation Maker

- **Purpose:** prepare simple itemised quotations and invoices in a browser.
- **Workflow:** enter seller and customer details, document number/date, line items, quantities, rates, optional discount and tax percentage; preview totals; print or save through the browser's PDF printer.
- **Runtime:** browser-local only. No server upload, cloud storage, accounts, payment collection, GST portal integration, e-invoicing, accounting sync or automated numbering service.
- **Commercial use:** can be offered as a basic document-preparation utility or customised template. Tax/legal compliance and customer requirements must be checked independently.
- **Release gate:** test add/remove rows, numeric validation, discount cap, tax arithmetic, special-character escaping, print layout, mobile layout and output on supported browsers.
- **Truth boundary:** creating or printing a document is not a payment, sale, tax filing or proof of delivery.
- **Version:** 1.0 prototype.
