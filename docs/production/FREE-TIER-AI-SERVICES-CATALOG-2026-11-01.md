# Free-Tier AI Services — Commercial Productization Plan

Date: 2026-11-01
Owner direction: use free plans and open-source software only. Do not subscribe, purchase credits, add paid APIs, or imply that a time-limited trial is a permanent free plan.

## Objective

Package practical, demonstrable services for retailers and small businesses. Sell defined human-reviewed outcomes, not vague promises of autonomous AI. Begin with one repeatable retail pilot and record the enquiry, agreed scope, payment evidence, delivery, and customer acceptance separately.

## Free-only operating rules

1. Use a provider only while its documented free plan or open-source licence permits the intended use.
2. Distinguish permanently free from free trial, free monthly allowance, open source, and self-hosted software.
3. No paid API calls, paid telephony minutes, paid email sending, paid model tokens, or paid hosting.
4. Never place private customer data, API keys, credentials, or phone lists in public repositories or browser code.
5. Do not scrape Google Maps, bulk-harvest contact details, spam prospects, fabricate reviews, or promise search rankings.
6. Human review is required before publishing marketing copy, replying to sensitive customer enquiries, or changing business listings.
7. A free hosted service may sleep, throttle, or impose usage limits. Do not sell uptime or 24/7 call answering until a measured, funded production setup exists.
8. Keep an auditable demo and a written scope for each customer.

## Product 1 — Retail AI Voice Assistant (browser demo first)

**Customer problem:** A shop misses common questions about opening hours, location, products, stock, delivery, returns, and contact details.

**Sellable deliverable:** A branded web-based voice-and-text assistant trained only on customer-approved shop information; FAQ answers; fallback to staff contact; conversation transcript export with consent; simple setup and handover guide.

**Free-first implementation:**
- Pipecat open-source framework for a real-time voice pipeline, subject to local/self-hosted runtime and compatible free components.
- Start with a browser demo and text fallback. Use browser-native speech capabilities where available; do not assume identical support on every device/browser.
- Local/open-source speech and language components may be evaluated, but model quality, hardware needs, language coverage, and commercial licences must be checked before each deployment.
- Phone-number calling, carrier minutes, hosted inference, and reliable 24/7 service are out of scope under a strict zero-spend rule unless a genuinely free allowance is verified.

**Acceptance test:** 20 owner-approved FAQ test prompts; correct answer or safe handoff; Hindi/English checks as agreed; no invented prices or stock; microphone denial still leaves text mode usable.

**Boundary:** Prototype/demo is not a production telephone agent and must not be advertised as one.

## Product 2 — Google Maps & Local Presence Setup

**Customer problem:** Customers cannot easily find accurate shop details, hours, service area, products, photos, and contact details.

**Sellable deliverable:** Google Business Profile setup/cleanup checklist, category and service descriptions, approved photos, opening-hours review, map/location link, review-response templates, and a monthly owner-operated update pack.

**Free-first implementation:**
- Google Business Profile is free for eligible businesses.
- Google Maps share/embed links may be used where appropriate; avoid a paid Maps API dependency.
- Google Search Console is free for website search visibility monitoring.
- Never create fake listings, fake reviews, or claim ranking guarantees.

**Acceptance test:** Owner confirms profile ownership; business name/address/phone/hours match source documents; map link opens; customer approves all public copy.

## Product 3 — AI SEO & Website Visibility Pack

**Customer problem:** The business website has unclear pages, weak metadata, missing local information, or indexing problems.

**Sellable deliverable:** Baseline site audit, page titles/descriptions, service and FAQ copy, structured-content recommendations, sitemap/robots review, Search Console setup guidance, and a prioritized 30-day action report.

**Free-first implementation:**
- Google Search Console and official Google Search Central guidance.
- Open-source/local crawlers and scripts where practical.
- Claude Free or other user-accessible free assistants for drafting only within their free usage limits; human review and fact checking required.
- No paid SEO platform, paid AI API, backlink package, guaranteed rank, or guaranteed traffic claim.

**Acceptance test:** Deliver before/after crawl evidence, list of changed URLs, valid metadata checks, and Search Console ownership/indexing status where available. Ranking changes are not guaranteed.

## Product 4 — HubSpot Free CRM & Enquiry Pipeline

**Customer problem:** Leads and follow-ups are lost across calls, social messages, and email.

**Sellable deliverable:** Free CRM setup, contact/deal stages, enquiry intake fields, task reminders, a simple lead dashboard, and staff handover instructions.

**Free-first implementation:**
- HubSpot Free CRM only within its current free feature limits.
- AI features are limited; do not describe advanced paid customer-agent functionality as included.
- Keep consent and retention rules; import only customer-authorized records.

**Acceptance test:** One test lead moves from new → contacted → qualified → quote sent → won/lost; access permissions and export are checked.

## Product 5 — AI Content & Voice Studio

**Customer problem:** Retailers need short product descriptions, social posts, FAQs, announcements, and voice-ready scripts.

**Sellable deliverable:** Monthly batch of owner-approved product copy, captions, short scripts, FAQ answers, and optional audio assets only where a genuinely free tool can produce them within its terms.

**Free-first implementation:**
- Anthropic built-in document skills are available on Claude Free when the required code/file capabilities are enabled, subject to usage limits.
- Prepare portable Agent Skills instructions so workflows can be reused across compatible assistants.
- Superpowers is an open-source development workflow/plugin, but Claude Code itself is not included in Claude Free. Do not promise the full Claude Code automation path on a Free-only account.
- Any separate “Voice Studio” service must be checked for its exact provider and current free limits before selecting it.

**Acceptance test:** Customer approves wording, brand tone, facts, language, and usage rights; generated audio is checked for pronunciation and consent/voice rights.

## Product 6 — Agent Workflow & Operations Blueprint

**Customer problem:** A small business wants repeatable task assignment, review, and evidence without expensive automation.

**Sellable deliverable:** Workflow map, role/task templates, approval checklist, daily operating report, and a local proof-of-concept using open-source components where feasible.

**Free-first implementation:**
- Paperclip is open-source agent orchestration software; it is not itself a free AI model or free cloud hosting. A working installation still needs a machine/runtime and a model/provider. Use local models only where hardware and licence permit.
- Superpowers can provide structured development practices such as planning, test-driven development, debugging, and verification in compatible coding-agent environments.
- No claim of independent autonomous operation or zero-cost cloud execution.

**Acceptance test:** One workflow completes end-to-end in a controlled test, records its outputs, asks for human approval at defined gates, and has a documented recovery path.

## Tool status and purchasing exclusions

| Named item | Free-only decision |
|---|---|
| Anthropic Skills / Claude | Use the Claude Free plan and portable skills only within available features and usage limits. |
| Superpowers | Open-source skill framework; Claude Code requirement means full plugin workflow is not assumed on Claude Free. |
| Paperclip | Open source; self-hosted/local runtime only. Model/compute costs must remain zero. |
| Pipecat | Open-source voice-agent framework; local/browser demo first. |
| HubSpot | Free CRM tier only; exclude paid AI customer-agent features. |
| Google Business Profile | Free, subject to eligibility and verification. |
| Google Search Console | Free. |
| Google Maps Platform APIs | Do not depend on metered APIs. Use free Business Profile and share/embed links; any API free cap is not a guarantee of zero billing. |
| Instantly AI | Its 14-day free trial is temporary and then service access stops unless paid; exclude from ongoing free-only production. |
| “Voice Studio” | Exact provider/product not identified; do not activate until name and free-tier terms are confirmed. |
| “PP master”, “ECCE”, “Uplift AI” | Exact products/spellings not confidently identified; keep pending, do not invent integrations or claim free access. |
| “Hubstop” | Interpreted as HubSpot; confirm if a different product was intended. |

## Recommended first retail pilot

Build one demonstrator for a single shop with:
1. A one-page public service/demo page.
2. Approved business FAQ and location/contact information.
3. Text assistant plus optional browser voice input/output.
4. Google Business Profile and map-link checklist.
5. Basic SEO audit report.
6. HubSpot Free enquiry pipeline or a private, consent-based equivalent.
7. A clear handoff to a human for stock, orders, complaints, refunds, and sensitive questions.

The first paid scope should be a fixed, small setup deliverable. Do not promise live phone answering, bulk outbound email, guaranteed SEO ranking, or continuous uptime under the zero-spend plan.

## Sales evidence required

For each pilot, store:
- customer-approved requirements and consent;
- demo URL and dated test cases;
- agreed scope, exclusions, and quote;
- payment verified from the actual payment account/provider record;
- delivery manifest and customer acceptance.

A demo, enquiry, quote, or payment link is not revenue. Revenue is counted only after a real payment is verified.

## Open questions that must be resolved before implementation

- Exact product identity/URL for “PP master”, “ECCE”, “Uplift AI”, and the intended “Voice Studio”.
- Whether “Hubstop” means HubSpot.
- Whether the first retail demo should be Hindi-only or Hindi + English.

## Source references

- Anthropic Skills and Free plan: https://support.claude.com/en/articles/12512176-what-are-skills
- Claude plan comparison: https://claude.com/pricing
- Superpowers: https://claude.com/plugins/superpowers
- Paperclip: https://github.com/PaperclipAI/paperclip
- Pipecat: https://github.com/pipecat-ai/pipecat
- HubSpot Free CRM: https://www.hubspot.com/products/crm
- Google Business Profile: https://business.google.com/in/business-profile/
- Google Search Console: https://search.google.com/search-console/about
- Google Maps Platform pricing: https://developers.google.com/maps/billing-and-pricing/overview
- Instantly free trial terms: https://help.instantly.ai/en/articles/13941298-instantly-free-trial
- Google guidance on third-party SEO claims: https://developers.google.com/search/docs/fundamentals/third-party-seo

