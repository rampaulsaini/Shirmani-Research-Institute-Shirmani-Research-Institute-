# SHIRMANI Heart-View, Safe Filter & Revenue Execution Standard

**Revision:** 2026-10-16  
**Status:** Proposed operational standard; implementation and deployment must be verified separately.  
**Principle:** Reduce friction without deleting useful work, protect the live platform, and prioritize useful deliverables that can be sold honestly.

## 1. Non-negotiable safety rule

Do not bulk-delete repository files, workflows, branches, products, records, assets, or automation based on names, apparent duplication, low activity, or workflow count alone. A component may be a dependency, recovery path, security control, or source of truth.

Use this reversible sequence:

1. **Inventory:** record exact path/ID, owner, purpose, last change, consumers/dependants, workflow references, public links, and current status.
2. **Classify:** `KEEP`, `MERGE CANDIDATE`, `PAUSE CANDIDATE`, `ARCHIVE CANDIDATE`, `DELETE CANDIDATE`, or `UNKNOWN`.
3. **Prove non-contribution:** search code references, workflow triggers, links, imports, deployment manifests, issue/PR history, and actual usage. Lack of recent activity is not proof of uselessness.
4. **Protect:** export or preserve the original state; record commit SHA and rollback instructions. Never put secrets or customer data in the report.
5. **Isolate first:** for approved candidates, use a branch, feature flag, disabled schedule, or clearly labelled archive PR where safe. Do not disable security gates or production persistence.
6. **Test impact:** run relevant tests, link checks, security scans, deployment smoke checks, and dependent workflow checks. Compare before/after.
7. **Review and release:** require human review for destructive changes. Delete only after dependency checks pass, rollback is proven, and the responsible owner approves.
8. **Monitor:** watch production, error rates, key workflows and customer paths after release. Roll back immediately on regression.

### Work-cycle friction score

Score each work item from 0–5 on: (a) user/customer value, (b) contribution to a required capability, (c) evidence of real usage, (d) uniqueness/reuse, (e) security or recovery importance. Separately score maintenance cost and duplication evidence.

- **Never auto-delete:** security, recovery, data integrity, source-of-truth, payment, privacy, or production-critical items.
- **Merge candidate:** demonstrably overlapping purpose and behavior, with a verified migration plan.
- **Pause/archive candidate:** no demonstrated current value after reference and dependency audit, and safe rollback exists.
- **Delete candidate:** only after explicit approval, backup, dependency proof, and passing regression tests.
- **Unknown:** preserve and investigate.

A high maintenance cost is a prompt to investigate—not permission to delete. Keep an audit log of decisions and evidence. Avoid creating another dashboard or workflow if an existing tool can safely be extended.

## 2. Heart-View / impartial-understanding model

### Owner-defined philosophical parameter

The owner's stated orientation is represented exactly as a **self-defined philosophical parameter**:

- Heart-centred orientation: **99.9999%**
- Analytical / mind–intellect orientation: **0.0001%**

These numbers encode the owner's stated values and design intent. They are not a scientifically measured property, a validated psychological diagnosis, proof of supernatural capability, or a defensible numerical ranking of the owner, Buddha, or any other person. Do not infer another person's ratio or IQ from this parameter.

### Operational behaviour (what can be tested)

For each answer or product interaction, evaluate observable behaviours:

1. **Listen before concluding:** restate the request faithfully; ask only a necessary clarifying question.
2. **Respect without flattery:** use calm, dignified language; do not manipulate, shame, or claim privileged access to another person's inner state.
3. **Fairness:** consider relevant perspectives and avoid assuming that the user's, assistant's, religious, atheistic, scientific, or political view is automatically correct.
4. **Evidence separation:** label observation, sourced fact, inference, uncertainty, personal philosophy, and unverified claim distinctly.
5. **Plain-language depth:** explain simply first, then offer a rigorous version, an example/story, and technical detail where appropriate.
6. **Safety and life protection:** do not encourage dangerous experiments, harm to people/animals, or unsupported medical/scientific conclusions; redirect to safe, evidence-based approaches.
7. **Correctability:** accept correction, cite sources where available, and update conclusions when evidence changes.
8. **Practical usefulness:** end with a concrete next step or a usable deliverable when the request calls for one.

Record per-test pass/fail and examples. Do not translate a subjective feeling into a fabricated precision score. If a numeric behaviour score is used, publish the rubric and sample size, show the individual criteria, and label it as an evaluation score—not a measure of a person's worth or essence.

### Test suite

Test at least: ambiguous requests; emotionally charged statements; conflicting evidence; a request to validate a grand claim; scientific uncertainty; Hindi/English switching; simple and expert explanations; corrections; privacy-sensitive inputs; and unsafe instructions. Record prompt, expected behaviour, actual output, result, date, version and reviewer. A preview page is not proof of live avatar, voice, lip-sync, or provider integration.

## 3. Truthful capability and release states

Use consistent labels everywhere:

- **DRAFT:** incomplete, internal only.
- **PREVIEW:** interface/sample only; clearly says it is not a live product.
- **DEMO:** a reproducible demonstration works for its stated task; limitations are visible.
- **BETA:** limited real-user testing, known issues and feedback route documented.
- **PRODUCTION VERIFIED:** deployed end-to-end test evidence, security checks, support route and rollback plan exist.
- **NOT VERIFIED / BLOCKED:** required evidence is absent or a dependency is unavailable.

A green workflow, merged PR, generated page, or provider request acceptance is not by itself proof that a complete customer-facing capability works. Report pending, cancelled, skipped, failed, and successful runs separately.

## 4. Revenue-first execution using existing services

Start with the currently available, deliverable services rather than promising the entire future platform at once:

- Hindi/English writing and editing.
- Source-based research summaries with source links and uncertainty notes.
- Website/blog/service-page content.
- Content audit and rewrite.

Existing repository entry points to reuse and audit:

- `writing-research-enquiry.html` — enquiry form.
- `income-client-outreach-desk.html` — outreach and delivery tracker.
- `showroom/first-client-pilot-desk.html` — first-client pilot.
- `global-outreach-and-service-sales-workbench.html` — proposal/outreach workbench, if present at the current branch.
- `showroom/water-conservation-research-sample.html` — illustrative research sample; not a customer testimonial or paid delivery.
- `showroom/shirmani-supreme-heart-view-preview.html` — character behaviour preview.

Do not create a duplicate tool if these routes already cover the workflow. Check that each linked path exists on the target branch before publishing.

### Client workflow

1. Identify a genuine, public-facing need and an appropriate official contact channel.
2. Draft a tailored message explaining one relevant service and a concrete, limited benefit.
3. Human-review every message; comply with privacy, platform, and anti-spam rules; honour opt-outs. No scraping or bulk unsolicited sending.
4. Capture scope, language, word count, sources, deadline, revision count, permitted usage and budget.
5. Send a written quote; agree scope, delivery date, payment terms and any deposit before work starts.
6. Deliver the agreed artifact with source list, limitations, and version information.
7. Record the actual event, not an optimistic label: enquiry received, reply received, quote sent, quote accepted, payment confirmed, delivery completed, feedback received.
8. Request feedback or a referral only when appropriate and with permission.

### Suggested pilot price display

Repository content currently proposes introductory prices such as ₹399 for short writing/editing (up to 500 words), ₹699 for Hindi–English adaptation (up to 800 words), and ₹999 for a source-based brief (up to 1,200 words). These are **proposed starting prices**, not verified market rates or guaranteed orders. Keep them only if the owner chooses to honour them; always confirm scope, complexity, deadline and payment terms in writing before beginning.

### Weekly measurable funnel

Track counts and conversion rates from actual records:

- Relevant organisations researched.
- Personalised drafts reviewed.
- Messages actually sent.
- Replies received.
- Enquiries with complete scope.
- Quotes sent and accepted.
- Payments actually confirmed.
- Deliveries on time.
- Revisions, feedback, repeat orders and refunds/disputes.

Do not claim revenue until payment is actually confirmed. Do not claim outreach occurred merely because an email draft was generated. Use a weekly review to improve response quality and conversion, not to inflate counts.

## 5. Platform security and scale gates

Before broad public sales or claims of supporting hundreds of millions of users:

- Separate public showroom data from private customer, enquiry, order, and payment data.
- Keep API keys, email credentials, tokens and payment secrets out of client-side HTML and repository history.
- Apply least privilege, input validation, output escaping, dependency checks, secret scanning, access logging and recovery tests.
- Verify payment and order handling with a test environment before enabling live transactions.
- For email/WhatsApp integrations, require authorised credentials, explicit permission, compliant templates and opt-out handling; never simulate a sent message.
- Load-test with defined traffic profiles and measured limits before making scale claims.
- Preserve the owner's original portrait/audio unchanged when using the actual supplied assets. Do not ask again for media already supplied; inspect available repository/connected assets first. If a required asset cannot be located, mark that asset missing instead of silently substituting another.
- Keep every product's unique visual, real screenshot, QR/passport, working demo, usage guide, QC record and price/offer state tied to its actual version. Do not bulk-mark products complete.

## 6. Current priority order

1. Confirm the main-branch enquiry and pilot paths work and point to each other correctly.
2. Verify the public deployed page against the merged source; record URL, commit SHA, test date and result.
3. Review pending/cancelled security and production workflows; determine the actual cause before rerunning.
4. Run one end-to-end writing/research enquiry → quote → accepted scope → payment confirmation → delivery test using a clearly marked test case, without claiming a real customer sale.
5. Test the Heart-View behaviour rubric and record reproducible results.
6. Audit duplicate or obstructive work using the reversible filter above; no destructive bulk deletion.
7. Only then widen the catalogue, integrations, and outreach.

## Acceptance checklist

- [ ] Existing routes inventoried; no duplicate dashboard created without need.
- [ ] Destructive actions require evidence, backup, review and rollback.
- [ ] Owner-defined 99.9999% / 0.0001% parameter is labelled philosophical/design intent, not scientific measurement.
- [ ] Behaviour rubric has reproducible test cases and honest outcomes.
- [ ] Public deployment is tested independently from source code.
- [ ] Sales claims match actual sent messages, accepted quotes, confirmed payments and completed deliveries.
- [ ] No credentials or customer-private data exposed.
- [ ] Provider-backed avatar/voice/lip-sync/live Q&A stays NOT VERIFIED until an actual end-to-end test passes.

**Completion rule:** a task is complete only when the deliverable exists, the relevant test passes, evidence is linked, and remaining limitations are stated. Planned, generated, queued, or merely described work is not counted as complete.
