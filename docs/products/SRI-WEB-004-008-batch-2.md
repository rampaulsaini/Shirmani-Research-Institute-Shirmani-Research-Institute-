# SRI-WEB-004–008 — Batch 2

Five browser-local web app prototypes added for product validation.

| ID | Product | Main use | Data handling |
|---|---|---|---|
| SRI-WEB-004 | Lead Desk | Lead pipeline, consent flag, follow-up date, CSV/JSON export, click-to-open WhatsApp draft | Browser localStorage |
| SRI-WEB-005 | Stock & Margin Calculator | Inventory quantity, unit cost, selling price, gross margin | Browser localStorage |
| SRI-WEB-006 | Social Content Planner | Content calendar, caption drafts, status, CSV/JSON export | Browser localStorage |
| SRI-WEB-007 | Income & Expense Book | Manual income/expense ledger, totals, CSV export | Browser localStorage |
| SRI-WEB-008 | Resume Builder | Resume draft, live preview, print/save as PDF | No persistent storage |

## Important limits

- These are standalone browser tools, not hosted SaaS products.
- No remote CRM, shared team database, automatic reminders, WhatsApp API, social publishing, payment gateway, tax filing or bank verification is connected.
- Lead follow-up opens a prefilled WhatsApp draft only after a user click and only when the consent flag is set; it does not send automatically.
- Local browser storage may be cleared and is not a backup. Export backups where available; do not store sensitive personal data.
- Inventory margin is a simplified gross estimate; it excludes operating costs, tax, returns and shipping.
- Ledger entries are manual and are not independently verified bank transactions.
- Resume claims must be truthful and checked by the user.

## Validation status

Static source review only at PR creation. No cross-browser, accessibility, mobile-device, security penetration, or real-customer acceptance test is claimed. Do not describe these as production SaaS or as generating income until hosted delivery, operational controls, customer acceptance and actual payment evidence exist.
