# SRI-WRITE-006 — First Client Deliverable Studio

**Status:** browser-local working prototype; human review required  
**Primary use:** prepare a structured first-draft pack for Hindi/English writing, website/blog content, research summaries, explanatory articles, translation/editing, and proposals.

## Current working features
- Client brief inputs: topic, objective, audience, language, length, deadline, budget, source URLs, constraints and revision allowance.
- Produces a structured deliverable pack with draft outline, source notes, scope/terms checklist and next actions.
- Copy output, download TXT, print / save PDF.
- Human release checklist for scope, commercial terms, factual checking, rights, proofreading and delivery record.
- Responsive, self-contained HTML; no build step or external JavaScript dependency.

## Explicit limitations
- No connected LLM, automatic web research, independent fact verification, server persistence, email/WhatsApp sending, invoicing, checkout, payment processing or client CRM.
- Generated content is a scaffold, not a completed paid client deliverable. All facts, citations, terms and source rights require human review.
- The browser page does not claim sales, income, customer endorsements, certification or guaranteed outcomes.

## Acceptance tests
1. Submit is blocked by native required validation if topic/objective are empty.
2. A complete brief generates a structured output including every entered field.
3. Copy action gives success only when clipboard write succeeds; errors show manual-copy guidance.
4. TXT export downloads the generated text.
5. Print action opens the browser print dialog for PDF saving.
6. Release checklist updates its count when checkboxes change.
7. Mobile layout uses responsive grid and readable controls.
8. No secret, external credential, or customer data is transmitted by this page.

## Release next steps
- Open the HTML locally and test on mobile/desktop.
- Check console and all controls; correct any defect before publishing.
- Add a product-specific actual screenshot and recorded demo only after they are genuinely captured.
- Publish with price basis, enquiry route, terms and support path. Do not call a storyboard a video or a draft a verified research report.
