# SRI Existing Digital Buyer Intelligence & Retention Engine
**Strategy specification — 2026-11-28**

## 1. Non-negotiable strategic direction

SRI prioritises people and organisations that already purchase and use digital products, software, AI tools, subscriptions, creative tools, research services, education products, and business platforms.

SRI does **not** prioritise educating digital-product novices, indiscriminate audience growth, vanity traffic, or unqualified mass lead generation.

The commercial proposition is to offer a relevant alternative or complementary product that demonstrably improves the buyer's outcome through:
- equal-or-better task quality, verified through comparative tests;
- a lower sustainable total cost, not an uneconomic headline discount;
- useful value additions, compatibility, onboarding, support, and clear terms;
- transparent loyalty benefits and respectful, permission-based follow-up.

**Terminology boundary:** "Existing digital buyers" means an established buyer segment in the market. A person in that segment may be new to SRI. It does not mean SRI already owns their identity, contact details, or purchase history.

## 2. Evidence and data-access boundary

SRI must not claim access to a global private buyer database unless a specific source, licence, permitted purpose, provenance, freshness, and access controls are evidenced.

Permitted discovery inputs include:
- SRI's own customers and purchase records collected with a valid basis;
- first-party enquiries and preferences voluntarily supplied by users;
- licensed datasets and partner referrals with documented permitted use;
- public business/product signals and official organisational contact routes, used within source terms and applicable law;
- opt-in communities, marketplaces, and vendor/partner programmes where outreach is allowed.

Do not scrape private profiles, infer or buy sensitive personal data, bypass platform controls, reuse leaked data, or send unsolicited bulk messages. Record source URL, collection date, permitted purpose, and contact/marketing permission separately. Provide suppression/opt-out handling and retention limits.

## 3. Core cycle

1. **Self-inspection gate:** confirm the task serves this strategy, is lawful, affordable, evidence-led, and does not create an unapproved external action.
2. **Buyer-segment discovery:** identify a market segment already paying for the relevant category.
3. **Product-use evidence:** document the job-to-be-done, current tool/category, buyer pain point, price band, and evidence source. Do not invent an individual purchase.
4. **Qualification and deduplication:** verify relevance, source quality, organisation/contact route, geography, fit, permission, and suppression status.
5. **SRI product matching:** map the need to an existing SRI product before proposing new development.
6. **Gap and value analysis:** identify a specific unmet need; define measurable improvement and compatible value additions.
7. **Build only when justified:** reuse and improve existing assets first. Create a new product only where evidence shows a meaningful gap and viable unit economics.
8. **Comparative quality gate:** test the same task against the buyer's current alternative where legally and practically possible. Record method, sample, results, limitations, and reviewer.
9. **Offer construction:** show scope, total price, savings basis, added value, delivery time, support, refund terms, and reward cost.
10. **Human-reviewed contact:** use only an authorised channel and relevant, individually reviewed communication. Respect opt-outs.
11. **Order-to-cash:** distinguish enquiry, proposal, acceptance, invoice, payment received, production, delivery, and customer acceptance.
12. **Retention:** ask for feedback, resolve defects, and offer relevant repeat/bundle/renewal benefits only with an appropriate contact basis.
13. **Learning loop:** use aggregated, minimised, permissioned feedback to improve product quality and offers.

## 4. Customer record contract

Store only fields required for the documented purpose:
- internal customer/account ID;
- individual or organisation type and country/region;
- source/provenance URL or source reference and collection timestamp;
- source permission/licence and permitted-use note;
- official contact route and contact/marketing permission status, timestamp, and evidence;
- buyer category and product/use-case evidence (label as public signal, self-declared, partner-supplied, or verified purchase);
- matched SRI product/SKU and match rationale;
- offer version, quoted price, discount/reward cost, and terms;
- interaction history, last contact, next permitted follow-up date, and channel;
- lifecycle status: researched, qualified, draft prepared, approved, sent, replied, enquiry, proposal, won, lost, paid, delivered, accepted, opted out;
- payment/delivery/acceptance evidence references;
- retention, complaint, refund, and product-feedback records.

Do not store payment-card data, passwords, unnecessary personal details, or sensitive attributes in the prospecting CRM. Restrict access by role, encrypt sensitive fields, audit access/changes, define retention/deletion, and maintain backups.

## 5. Offer quality and unit-economics gate

An offer may be released only when:
- the SRI product works for the stated use case and has reproducible test evidence;
- quality claims are comparative, scoped, and supported;
- price includes production, AI/API, payment, support, refunds, tax, and delivery costs;
- rewards and discounts leave a sustainable contribution margin;
- licensing, third-party terms, intellectual property, privacy, and country restrictions are checked;
- the customer can understand exactly what is included and excluded.

Do not promise "best", "superior", guaranteed savings, or permanent retention without supporting evidence. Never undercut below sustainable cost merely to win a sale.

## 6. Rewards and retention rules

Rewards may include repeat-purchase discounts, useful bundles, priority support, renewal benefits, and eligible referrals. Publish eligibility, expiry, exclusions, redemption, and maximum cost. No dark patterns, forced subscriptions, artificial urgency, or rewards conditional on positive reviews. A customer can decline or opt out without losing unrelated entitlements.

Follow-up cadence must be relevant, low-frequency, channel-appropriate, and permission-aware. Stop immediately on opt-out or objection.

## 7. Automission job contract

Each automission cycle receives one bounded segment/product task and must produce a durable, auditable output:
- input segment, product category, and task;
- evidence/source ledger and permission decision;
- buyer qualification and deduplication result;
- SRI product match and gap assessment;
- quality/comparison test or a clear blocked status;
- offer economics and human-review draft;
- outcome counters and evidence references;
- errors, exclusions, and next action.

Automation may research permitted public information, classify, deduplicate, draft, calculate, test, and report. It must not autonomously purchase services, send external messages, access restricted databases, publish unreviewed claims, issue refunds, or change customer permissions.

**Human approval is required** before external contact, paid commitments, price/terms exceptions, public claims, and customer-data export.

## 8. Pre-cycle self-inspection checklist

Before every run, evaluate:
- Is this work strictly aligned with existing digital buyers and relevant products?
- Are we reusing an existing SRI asset before creating another?
- Is the source lawful, current, traceable, and permitted for this use?
- Are we collecting the minimum necessary data?
- Is the offer genuinely useful and the quality claim testable?
- Is the price sustainable after all costs and rewards?
- Are consent, opt-out, country, licensing, and platform rules respected?
- Is the next action reversible and within granted authority?
- Will the output prove useful work rather than merely count a workflow run?

If any critical answer is no or unknown, mark the cycle **BLOCKED / HUMAN REVIEW**. Do not proceed by default.

## 9. Metrics — evidence, not vanity counts

Report separately:
- buyer-segment records researched (not unique customers unless verified);
- source-valid and permission-valid records;
- qualified buyer records and deduplicated organisations;
- SRI product matches and documented unmet needs;
- comparison tests run/passed/failed;
- offers drafted, human-approved, and actually sent;
- replies, qualified enquiries, proposals accepted;
- paid orders and collected revenue;
- refunds, chargebacks, support burden, delivery acceptance;
- repeat purchase rate, retention by cohort, opt-out/complaint rate;
- contribution margin after production, AI/API, payment, reward, refund, tax, and support costs.

No forecast, market-size estimate, workflow count, catalogue count, or prospect count may be reported as customers, sales, or income.

## 10. Current repository readiness boundary

The repository's current README describes multiple showroom and production utilities as browser-local prototypes and explicitly states that server sync, CRM persistence, automated outreach, checkout/payment, and live external integrations are not connected unless separately implemented and tested.

The existing First Revenue Execution Board and Production Expansion Sprint are planning documents, not evidence of prospect contact, sales, or income. This strategy supersedes generic prospecting priorities where they conflict: prioritise established digital-buyer segments and existing SRI customer retention, not digital-novice education.

Before implementation, inspect existing data models, privacy/security controls, hosting/database state, and workflow triggers. Do not create a second CRM, add paid services, enable bulk outreach, or activate recurring automations until the existing stack is tested and the owner approves the specific change.

## 11. Acceptance criteria for implementation

- [ ] Existing product catalogue and CRM assets inventoried; duplicate systems avoided.
- [ ] Data sources have provenance, licence/permission, and collection date.
- [ ] Buyer segment is based on evidence of existing digital-product use, not unsupported assumptions.
- [ ] Customer records have deduplication, access control, retention, and opt-out handling.
- [ ] Product matching reuses existing SRI assets before recommending new builds.
- [ ] Comparative quality and sustainable unit economics are recorded.
- [ ] External contact requires human approval and permission checks.
- [ ] Payment, delivery, acceptance, refund, and repeat purchase have distinct evidence states.
- [ ] Automission pre-cycle self-inspection and blocked state are tested.
- [ ] Dashboard distinguishes researched records, qualified buyers, customers, paid orders, collected revenue, and net contribution.

**Status:** strategy specification only. No buyer database, CRM integration, outreach, payment, or recurring automission is claimed live by this document.
