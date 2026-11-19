# SRI-WEB-009–013 — Batch 3

Five browser-local small-business prototypes created for early customer discovery.

| ID | Product | Purpose | Data boundary |
|---|---|---|---|
| SRI-WEB-009 | Product Catalog Maker | अपने उत्पाद, SKU, श्रेणी, कीमत और उपलब्धता की सूची बनाएं; CSV/JSON में export करें। | Browser localStorage |
| SRI-WEB-010 | Order Tracker | ग्राहक के ऑर्डर, रकम और fulfillment status का स्थानीय रिकॉर्ड रखें। | Browser localStorage |
| SRI-WEB-011 | Service Job Card | काम प्राप्ति, समस्या, अनुमानित खर्च और मरम्मत की स्थिति दर्ज करें। | Browser localStorage |
| SRI-WEB-012 | Customer Feedback Desk | ग्राहक प्रतिक्रिया और testimonial प्रकाशित करने की अलग अनुमति दर्ज करें। | Browser localStorage |
| SRI-WEB-013 | Dispatch Register | पार्सल संदर्भ, courier, tracking ID और delivery status व्यवस्थित करें। | Browser localStorage |

## Shared limitations
- Standalone HTML prototypes; no hosted SaaS backend, user accounts, team sharing, cloud backup or payment gateway.
- Records are stored in the current browser only. Users should export backups and avoid sensitive personal information.
- CSV/JSON exports are operator-generated; no automatic external sharing occurs.
- Status, proof references and customer-entered values are manual and not independently verified.
- No claims of customer adoption, sales, payment, delivery verification or income.

## Validation
Source-level review only. No browser/device, accessibility, penetration, API, customer acceptance or production deployment test is claimed. Do not merge or market as finished paid SaaS until release gates and real customer validation are completed.
