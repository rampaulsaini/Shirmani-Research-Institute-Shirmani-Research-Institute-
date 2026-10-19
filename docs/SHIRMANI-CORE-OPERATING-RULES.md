# SHIRMANI Core Operating Rules — Evidence, Continuity, and Revenue

**Status:** Proposed operating contract; this document does not claim that the controls below are already implemented.
**Owner:** Shirmani Research Institute
**Principle:** Preserve first. Inspect existing evidence second. Change only a demonstrated gap. Verify once with reproducible evidence. Continue forward.

## 1. No-repeat work ledger

Every task must have a stable task ID and one of: `NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, `READY_FOR_REVIEW`, `VERIFIED`, `FAILED`, `DEFERRED`.

Before starting:
1. Read the existing task ledger, latest successful run, artifacts, relevant commit/PR, and prior verification result.
2. If the same revision already passed the required test, reuse that evidence; do not rerun expensive or external tests without a reason.
3. Reopen a completed task only when its source revision changed, evidence expired, a regression was reported, or an independent check requires it. Record the reason.
4. Do not ask the owner to upload an asset again when its existing repository/authorized service reference is available. Never fabricate an asset reference.

## 2. Truthful production counters

Counters must be computed from dated, machine-readable records—not hand-written success claims.

Report UTC timestamp and reporting window, workflow cycles attempted/succeeded/failed/skipped, deployment state, smoke-test state, backup/restore-test state, open blockers, product demos, qualified inquiries, proposals accepted, payments confirmed, and deliveries accepted.

For every percentage, show numerator, denominator, and formula. Example: `successful_runs / completed_runs × 100`. If the denominator is zero or the data source is unavailable, display `N/A`, not 0% or 100%. Distinguish:
- workflow heartbeat from a successful production build;
- successful build from deployed public content;
- prepared verification packets from independently verified claims;
- demo views/inquiries from paid revenue;
- code checks from real customer acceptance.

Daily/24×7 reporting is only truthful when scheduled collection, retention, failure alerting, and timestamp freshness are actually operational.

## 3. Change safety and completion gate

- Inspect the current default branch and open PRs before creating another fix for the same issue.
- Keep changes narrow, reviewable, and traceable to a concrete failing test or user-facing defect.
- Preserve protected source files and original user-provided media; make derivative copies for edits.
- Never delete a filter, test, workflow, or file solely because it slows a cycle. First prove what it protects, identify dependencies, and replace it with a tested non-blocking alternative if appropriate.
- Do not force-push, merge a failing PR, publish secrets, or weaken security checks to manufacture a green status.
- A task is complete only when its acceptance criteria pass and evidence links, commit SHA, test output, and deployment result are recorded. If an external service or credential is unavailable, mark it `BLOCKED` with the exact missing dependency.

## 4. Backup, restore, permissions, and alerts

- Use least-privilege tokens and workflow permissions; never place credentials in source, logs, or public artifacts.
- Back up important source/configuration and required generated state to a separately recoverable destination. Record timestamp, scope, retention, and checksum.
- Test restoration into a disposable location; a successful backup upload alone is not a restore test.
- On failed critical production/deployment/security checks, preserve logs and artifacts, notify the configured owner/channel, and stop dependent publication steps.
- Retries must be bounded and idempotent. A retry is not a substitute for root-cause analysis.

## 5. Public interface information architecture

Organize the homepage from top to bottom in a clear visitor journey:
1. Plain-language purpose and a small set of primary actions.
2. Services/products with real demos, capabilities, limitations, and evidence.
3. Heart-View preview and research/library material grouped by topic.
4. Account creation/sign-in only when a real, secure authentication backend exists.
5. Customer inquiry, proposal, payment, delivery, and support paths.
6. Transparent production dashboard, dated evidence, privacy, accessibility, and contact/help.

Use responsive layouts, readable Hindi/English labels, consistent cards, search/categories where needed, and working links. Never display a decorative login form as working authentication. Do not claim a page is live based only on a merged PR.

## 6. Revenue-first validation

Prioritize one small, deliverable service over an unbounded catalog:
1. Publish a working demo with clear scope, price/quote process, turnaround, and limitations.
2. Capture consent-based customer inquiries and track their source and status.
3. Send a proposal and record explicit customer acceptance.
4. Confirm payment from a trusted payment record; never infer payment from a button click.
5. Deliver the agreed artifact/service and record customer acceptance or a documented issue.

Report each stage separately. Do not report projected, pending, or unpaid amounts as received revenue. Keep customer data minimal and access-controlled.

## 7. External services and user media

For HeyGen or any external provider, distinguish API/configuration checks, generated-video availability, actual playback, voice authorization, audio quality, lip-sync assessment, live-question/answer exchange, and end-to-end result. Each requires its own evidence; do not repeatedly request media already available at the authorized link. Do not claim live Q&A works without a real round-trip test.

## 8. Research and high-confidence claims

Keep the owner's original formulations intact and distinguish them from summaries, hypotheses, interpretations, and independently tested claims. Numerical ratios or scientific statements are not measured facts unless a defined method, dataset, calculation, and independent reproducibility evidence support them. Preserve uncertainty and counter-evidence; never invent reviewer identities, tests, results, citations, or verification percentages.

## 9. Agent and automation guardrails

Automation should continue only through finite, observable, restart-safe jobs with explicit inputs, timeouts, bounded retries, and durable checkpoints. Do not claim a permanently autonomous agent or independent awareness. Every scheduled cycle must leave a timestamped result, and failures must remain visible. No workflow may delete user content or spend money without explicit authorization.

## 10. Definition of done

A production change is done only when all applicable checks are true:
- [ ] Existing state and previous evidence were inspected first.
- [ ] The exact change and reason are traceable to a commit/PR.
- [ ] Relevant automated tests pass; failures and skipped checks are visible.
- [ ] Public deployment was independently opened and checked where applicable.
- [ ] Security, permission, backup, and restore implications were addressed.
- [ ] Counters use real records and disclose denominators.
- [ ] User-facing wording is understandable and does not overstate capability.
- [ ] Revenue claims are supported by actual payment and delivery records.
- [ ] The ledger records the next incomplete task so completed work is not restarted without cause.

**Non-negotiable:** No invented success. No unnecessary repetition. No destructive cleanup without proof. No publication presented as verified until the deployed result is tested.
