# Income Pipeline Ledger — Shirmani Research Institute

**Purpose:** Track real client acquisition and delivery without confusing prospects, drafts, targets, or estimates with earned revenue.

**Current offer scope:** Hindi/English writing, editing, source-based research summaries, and website/blog content. Do not promise AI systems, live avatar generation, automatic outreach, payment processing, or independent scientific verification unless separately built and tested.

## Status vocabulary

- `RESEARCHED`: organisation/source identified; no contact implied.
- `DRAFT_READY`: a personalised message exists; not sent.
- `SENT`: message actually sent; record date and permitted evidence.
- `REPLIED`: actual response received.
- `QUALIFIED`: need, buyer/contact route, deadline, budget or procurement path are sufficiently understood.
- `QUOTE_SENT`: written scope and price sent.
- `ACCEPTED`: client explicitly accepted the scope in writing.
- `PAID`: payment receipt independently checked; record amount/date, never publish transaction credentials.
- `DELIVERED`: deliverables handed over with evidence.
- `CLOSED_WON` / `CLOSED_LOST`: outcome and reason recorded.

## Lead record template

Copy one row per organisation. Keep personal data minimal and store private contact details only in an access-controlled system.

| Field | Value |
|---|---|
| Lead ID | |
| Organisation / public source URL | |
| Sector / country | |
| Relevant need hypothesis (label as unconfirmed) | |
| Publicly listed contact route | |
| Service offered | |
| Personalisation / reason for fit | |
| Stage (use vocabulary above) | RESEARCHED |
| Researched on (ISO date) | |
| Contact sent on (ISO date; blank until sent) | |
| Reply date / factual summary | |
| Need confirmed? Evidence | |
| Quote reference / version | |
| Scope, word count, language, sources, revisions | |
| Agreed delivery date | |
| Accepted in writing? Evidence | |
| Payment status / amount / received date | |
| Delivery evidence / date | |
| Follow-up date / opt-out status | |
| Next action / owner | |
| Notes / uncertainty | |

## Guardrails

1. Never label a draft as sent, a target as achieved, a quote as an order, or an invoice as payment.
2. Do not infer a person's email address. Use official published contact routes and applicable contact rules.
3. Personalise outreach to a plausible need; keep it concise, relevant, truthful, and easy to decline. Respect opt-outs and do not bulk-spam.
4. Confirm deliverables, source expectations, timeline, revisions, price, and payment terms in writing before starting.
5. Keep client data private. Do not place bank details, OTPs, passwords, or unnecessary personal data in this ledger.
6. Price menus in the repository conflict. Until the canonical pricing blocker is resolved, treat all listed rates as proposals and issue a custom written quote only after scope and approved pricing are reconciled.
7. Revenue counts only when receipt evidence is checked. Keep prospect value, proposed value, invoiced value, and cash received as separate metrics.

## Seven-day pilot dashboard

These are **targets, not results or guarantees**.

| Metric | Target | Counting rule |
|---|---:|---|
| Public-source prospects researched | 20 | Unique organisations with source URL and relevance note |
| Personalised drafts prepared | 10 | Draft saved; not counted as sent |
| Outreach actually sent | Up to 10 | Count only after human review and actual send evidence |
| Qualified replies | 3 | Need and plausible next step confirmed by reply |
| Written quotes | 2 | Scope, price, deadline and terms included |
| Paid pilot orders | 1 | Written acceptance plus checked receipt |
| Deliveries | Per agreed deadline | Deliverable handoff recorded |
| Verified cash received | Actual amount only | Receipt evidence checked; no projections counted |

## Daily review

- Update stages and next-action dates.
- Review replies and opt-outs before any follow-up.
- Record blockers: price conflict, no suitable public contact route, unconfirmed need, payment uncertainty, or delivery-capacity limit.
- At the end of day seven, report counts with evidence links and state `0` where no qualifying evidence exists. Never backfill estimated outcomes as actuals.
