# SHIRMANI RESEARCH INSTITUTE — Next Implementation Priorities

Updated: 2026-10-17

## Purpose
Turn the existing repository into a navigable, testable public service without discarding existing tools or presenting planned capabilities as shipped. This is a work plan, not a deployment or sales report.

## Priority 1 — Fix the public customer journey
- Make the public showroom the single clear starting point.
- Route commercial-service calls to action directly to services-writing-research.html, the current offer page; do not send visitors through the legacy writing-research-service-offer.html page.
- Keep the enquiry form reachable in one click.
- Check mobile layout, keyboard navigation, visible focus, heading hierarchy, link destinations, and empty/search states.
- Maintain an inventory of existing tools and product links before reorganizing; no page is deleted just because it is not in the first screen.

## Priority 2 — Record real sales, not assumptions
Track one record per prospect/order:
- prospect source and public contact URL;
- service requested and need evidence;
- date contacted, opt-out state, and next action;
- written quote and agreed scope;
- payment state: not requested, requested, verified, refunded;
- delivery link/date and customer acceptance;
- actual collected amount and transaction evidence reference.

Rules:
- Proposed prices are not market-validated rates.
- A drafted email is not a sent email.
- An enquiry is not an order.
- A payment request is not received income.
- Mark income as received only after checking the transaction in the payment provider.
- Do not invent contact addresses. Use relevant official public contact channels and respect opt-outs and applicable law.

## Priority 3 — Product-specific readiness
Each product needs its own versioned passport:
- intended user and problem solved;
- current version and status;
- what works now, what is simulated, and what remains planned;
- working demo/test instructions;
- limitations, accessibility and privacy notes;
- known issues, evidence, owner, and next action;
- proposed price, fulfilment scope and refund/support terms.

Do not label a product ready for sale until the promised function is reproducible and delivery obligations can be met.

## Priority 4 — Voice/video evidence chain
Keep these gates separate:
1. authorized source voice and consent/rights;
2. provider integration and generated audio;
3. exact script/content;
4. authorized image/avatar;
5. rendered video and lip-sync review;
6. live dialogue/Q&A test cases and failure handling;
7. provider-side job/result evidence;
8. privacy, accessibility, security and release review.

A provider URL, stored configuration, or successful job submission is not proof of successful playback or real-time Q&A. Record test date, environment, input, expected result, actual result, reviewer and evidence location.

## Priority 5 — Security and release gates
- Preserve protections; investigate false positives before changing a filter.
- Use least privilege, secret scanning, dependency review, input validation, output encoding, rate limits and safe error messages where applicable.
- Never store API keys, passwords, private customer material or voice-consent records in public source files.
- Test changes on a branch and review diffs before merge.
- Back up data and define rollback steps before production changes.
- A checklist or browser-only tool is not a penetration test or security certification.

## Measurable weekly dashboard
Report counts with links/evidence:
- public links checked / broken links found / fixed;
- products inventoried / demos actually tested / blocked;
- qualified prospects / messages sent through authorized channels / replies;
- quotes accepted / payments verified / deliveries accepted;
- voice-video gates passed / failed / pending;
- security issues found / fixed / retested.

Use zero when the verified count is zero, and unknown when records are missing. Never replace missing evidence with a guessed success percentage.

## Definition of done
A task is complete only when its changed files are reviewed, relevant tests are run, evidence is recorded, public wording matches actual capability, and the result is merged/released through the repository's normal process. This document itself does not claim that any of these actions have already occurred.