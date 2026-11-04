# Core Automission Execution Rules

**Status:** operating contract / implementation requirements  
**Priority:** first verified customer revenue, safe continuity, and preservation of completed work.

These rules govern every automated production cycle. A workflow run, merged pull request, generated record, catalogue entry, or public page is not by itself proof of a working customer service, sale, payment, delivery, or independent verification.

## 1. One source of truth for work state

Every work item must have a stable `task_id`, a clear owner/lane, a version, an acceptance test, and an evidence location. Track these states separately:

`DISCOVERED → READY → IN_PROGRESS → QC → PUBLISHED → CUSTOMER_ENQUIRY → PROPOSED → ACCEPTED → PAID → DELIVERED → CUSTOMER_VERIFIED`

A state may advance only when its required evidence exists. Never infer later states from earlier ones.

## 2. Never repeat completed work without a reason

Before creating or running a task:
- Look up its stable ID and prior result in the canonical ledger.
- Reuse a completed, passing result when its inputs and version have not changed.
- Reopen it only for a recorded defect, changed requirement/input, expired dependency, failed live check, or explicit user request.
- Record the reason, previous evidence, changed inputs, and new result.
- Make writes idempotent; retries must not create duplicate products, orders, payments, or customer messages.

A missing evidence pointer is a verification gap, not permission to rebuild the whole item. First recover or inspect the existing evidence.

## 3. Finish one bounded task before starting another

Each cycle selects one bounded, highest-priority eligible task, completes its acceptance checks, records the outcome, and only then selects the next task. Parallel work is allowed only for independent tasks with isolated outputs and no shared-state race.

If a task is blocked, record the exact blocker and continue only with an independent task that does not depend on it. Do not silently skip a failed gate.

## 4. Income-first priority

Prioritise a real, deliverable service over speculative scale:
1. Keep one clearly scoped service offer visible.
2. Provide a working demo/sample and transparent price, scope, timeline, and revision terms.
3. Capture a genuine customer enquiry through a working contact route.
4. Prepare a proposal; record customer acceptance only when received.
5. Record payment only from a verifiable transaction reference/receipt.
6. Record delivery only when the actual deliverable and dispatch evidence exist.
7. Record customer acceptance/verification only from an actual customer response.

Never send outreach, publish customer data, issue invoices, mark payments received, or claim revenue without the required human authorization and evidence. Proposed prices and targets are not revenue.

## 5. Public showroom truth contract

Show only current, working links and label each item accurately:
- **Demo available** means the linked demo opens and its advertised core action works.
- **Enquiry enabled** means the enquiry route submits to an owned, monitored destination and provides a clear confirmation.
- **Login enabled** means real authentication is connected and tested.
- **Checkout enabled** means payment is connected and test/live mode is clearly distinguished.
- **Published** means the production URL was checked after deployment.
- **Sold / Paid / Delivered** require transaction- and delivery-level evidence.

Keep catalogue inventory, production output, customer enquiries, accepted proposals, paid orders, deliveries, and independent verification as separate counters. Display zero when evidence is zero; display unavailable when the source cannot be read. Never convert workflow counts into quality percentages or income claims.

## 6. Deployment and public verification

A merge is not a deployment. A successful workflow is not a public-page test.

For every release candidate:
- Record the exact commit SHA and target environment.
- Confirm the deployment completed for that SHA.
- Request the public URL and check HTTP response, page title, critical assets, navigation, mobile layout, and primary enquiry action.
- Store timestamped test results and screenshots/log references where available.
- If the live check cannot be performed, label the release **deployment unverified**; do not claim success.

## 7. Backup, recovery, and least-risk changes

- Inspect the current branch, working state, deployment target, and existing backups before mutation.
- Prefer additive changes on a new branch and a reviewable pull request.
- Never delete, overwrite, reset, pause, restart, rotate secrets, change billing, or alter production data as an unreviewed shortcut.
- Keep credentials and private customer data out of Git, public artifacts, logs, and reports.
- Before a database migration or destructive operation, verify a recent restorable backup and document a rollback path.
- If backup status or rollback safety is unknown, stop the destructive operation and report the exact missing proof.

## 8. Automation reliability and quality evidence

Each cycle records: cycle ID, start/end timestamps, tasks selected/completed/blocked, retries, duplicate prevention, tests run/passed/failed, artifacts produced, publication checks, and actual commercial events.

Report measurable ratios only with explicit numerators, denominators, time windows, and source records. Do not invent a "quality", "uniqueness", "accuracy", or "superiority" percentage. A percentage without a reproducible measurement definition is not a metric.

Use bounded retries with backoff. Repeated failure must open a blocker and stop that task from consuming every cycle. Preserve successful prior outputs.

## 9. 24/7/365 operational report

The public report should distinguish:
- workflow cycles attempted and completed;
- concrete new outputs and reused completed outputs;
- QC pass/fail and unresolved blockers;
- deployment checks passed/failed/unverified;
- enquiries, proposals, accepted orders, payments, deliveries, and customer confirmations;
- last successful backup/restore test.

Show the last update time and data source. Missing or stale telemetry must be visibly marked stale/unavailable, not represented as live.

## 10. Definition of a successful cycle

A cycle is successful only when it has:
1. selected eligible work without duplicating completed work;
2. produced or correctly reused a concrete artifact;
3. passed its task-specific acceptance checks;
4. recorded evidence and an accurate state transition;
5. preserved the repository and production safety boundaries; and
6. published and checked the public result when publication is part of the task.

Commercial success is reported separately and requires real customer/payment/delivery evidence.

---
**Non-negotiable principle:** protect completed work, make only evidence-backed changes, and spend automation capacity on the next real bottleneck to customer value and received income.
