# SHIRMANI RESEARCH INSTITUTE — Income Next Action
**Prepared:** 2026-10-16  
**Status:** READY FOR HUMAN REVIEW — not sent; no customer or income is implied.

## Evidence boundary
The repository already contains a writing/research enquiry page, illustrative portfolio, and Outreach & Income Workbench. These assets do not prove traffic, enquiries, sales, or payment. The currently supported offer is Hindi/English writing, source-based research summaries, and website/blog content.

Entry points: `writing-research-enquiry.html`, `writing-research-portfolio.html`, `outreach-income-workbench.html`, `production-progress-map.html`.

## Pilot offer to test
Prices below are the **existing proposed prices in the workbench**, not verified market rates:
1. Hindi ↔ English Writing Polish — ₹499; up to 800 words, one revision; target 2 business days after scope confirmation.
2. Source-based Research Brief — ₹1,499; up to 5 sources and about 1,200 words; target 3 business days after scope confirmation.
3. Website / Blog Draft — ₹999; up to 1,000 words, one revision; target 3 business days after scope confirmation.

Confirm complexity, source access, taxes, deadline, revisions, payment method and final quote in writing before accepting an order. Do not promise certified translation, legal/medical advice, or independent verification unless qualified and actually performed.

## Client outreach email — draft only
**Subject:** Hindi/English writing and source-based research support — Shirmani Research Institute

Hello,

Shirmani Research Institute is opening a small pilot for Hindi/English writing, editing, source-based research summaries, and website/blog content.

We help turn a defined topic or existing draft into clear, audience-focused material. Research briefs can include a source list, key findings, limitations, and open questions. We do not invent citations or present unverified claims as established facts.

Pilot examples:
- Writing polish (up to 800 words): proposed ₹499
- Research brief (up to 5 sources, about 1,200 words): proposed ₹1,499
- Website/blog draft (up to 1,000 words): proposed ₹999

These are indicative pilot prices, subject to scope and source availability. Before work begins, we confirm deliverables, final price, deadline, revisions, and payment terms in writing.

If relevant to your team, reply with the topic, audience, language, desired length, deadline, source links, and approximate budget. We can then send a scoped proposal.

Regards,  
Shirmani Research Institute  
Hindi/English Writing & Research

*Draft only: no email has been sent, and no recipient, sale, or income has been verified.*

## Targeting plan
Begin with 30 relevant organizations, not a mass blast to 195 countries:
- 10 education/training providers
- 10 small businesses or agencies with visible website/blog content needs
- 10 research/community organizations publishing public reports

Contact only organizations where a public official contact channel and relevance can be verified. Personalize based on an observable need. Respect opt-outs and applicable anti-spam/privacy rules. Do not scrape private addresses or send bulk mail without compliant consent and deliverability controls.

## 14-day experiment
| Measure | Target | Evidence |
|---|---:|---|
| Qualified prospects researched | 30 | Organization, official contact URL, fit reason, research date |
| Personalized messages sent | Up to 30 after human review | Sent timestamp, channel, recipient, message copy |
| Replies | Measure; do not assume | Reply record/status |
| Qualified enquiries | Measure; do not assume | Completed enquiry brief |
| Written quotes issued | Measure; do not assume | Quote, scope, date and expiry |
| Paid orders | Measure; do not assume | Customer confirmation and payment evidence |
| Revenue received | ₹0 until evidence exists | Payment record; separate booked value from cash received |

Review at day 7 and 14. If there are no qualified replies after 15 carefully targeted messages, revise the segment, samples, or offer before sending more. Sent messages, clicks, drafts, and commits are not revenue.

## Email communication system — minimum viable design
Do not begin with an autonomous mass-mailer. Implement in stages:
1. **Draft:** create a personalized email from a verified public business need and approved offer.
2. **Human approval:** show recipient, source URL, message, and opt-out status; do not send without explicit approval.
3. **Send:** use an authorized email provider/account and approved API or connector. Keep credentials in provider-managed secrets, never repository files.
4. **Record:** log message ID, timestamp, organization, legal basis/consent status, campaign, delivery/bounce/reply, and opt-out; restrict personal-data access.
5. **Suppress:** stop further contact after opt-out, hard bounce, or do-not-contact flag.
6. **Measure:** report sent, delivered, replies, qualified enquiries, quotes, paid orders, and revenue received separately.
7. **Audit:** retain test logs and a kill switch; fail closed if authorization, source, or suppression checks are missing.

### Release gate
- [ ] Sending account/provider connected and authorized
- [ ] Internal test email delivered and recorded
- [ ] Public-contact/source evidence stored per prospect
- [ ] Opt-out and suppression behavior tested
- [ ] No secrets committed to Git
- [ ] Enquiry → quote → payment record tested end-to-end

Until required tests have evidence, email automation status is **BLOCKED / NOT VERIFIED**.

## Current result
This plan prepares a controlled income experiment and email-system specification. It does not deploy a backend, connect an email account, contact prospects, create a sale, or prove income.
