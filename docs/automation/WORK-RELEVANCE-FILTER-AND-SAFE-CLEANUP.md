# SHIRMANI Work-Relevance Filter & Safe Cleanup Policy

**Status:** implementation specification; not evidence that repository files, workflows, emails, or production services have been deleted or changed.
**Priority:** reduce low-value cycle work without harming active products, data, security, revenue work, or production.

## 1. Non-negotiable safety rule

**Filter first; quarantine second; delete only after evidence and approval.** Never mass-delete files, workflows, secrets, records, branches, artifacts, or customer data based only on low activity, duplicate-looking names, old timestamps, cancelled runs, or an automated score.

- The policy is non-destructive by default.
- A cancelled workflow is not automatically useless; investigate its cause and whether a required gate was skipped.
- Preserve production, security, backup, deployment, revenue, compliance, audit, accessibility, and recovery controls unless a verified replacement exists and an authorised reviewer approves the change.
- Never remove the last known-good build, unique source asset, original media, evidence record, rollback route, or required secret reference.
- Do not put credentials, private client data, personal contact details, or secret values in public repository records.

## 2. Relevance score (0–5)

Score every proposed task, automation, product, workflow, and recurring report:

| Dimension | 0 | 1 |
|---|---|---|
| User/customer value | No identifiable outcome | Direct, measurable outcome |
| Cycle-time contribution | Adds delay or repeats work | Removes a real bottleneck |
| Evidence quality | No observable result | Produces verifiable evidence |
| Safety/continuity | Introduces unmitigated risk | Preserves or improves recovery/security |
| Reuse/maintainability | Creates isolated overhead | Reusable, owned, documented component |

**Score = sum across five dimensions (maximum 5)** where each dimension is scored 0 or 1. The binary rubric intentionally keeps the first version simple and auditable.

- **4–5: KEEP / PRIORITISE** — clear value, evidence, and safe ownership.
- **2–3: REVIEW / MERGE** — inspect for consolidation; keep any unique useful behaviour.
- **0–1: QUARANTINE CANDIDATE** — no automatic deletion. Verify dependency, ownership, history, and replacement first.
- **Any security, production, legal, backup, or revenue-control role:** mandatory human review regardless of score.

A score is triage, not proof that an asset is safe to remove.

## 3. Dependency and impact gate

Before disabling or deleting any item, record:
1. Exact repository path, workflow name/ID, resource ID, and current state.
2. Last successful run/use and the commits, products, pages, or workflows that depend on it.
3. Whether it is a unique source, security gate, deployment path, rollback mechanism, or audit record.
4. A verified replacement and side-by-side acceptance evidence, if applicable.
5. Backup/restore or revert procedure, expected blast radius, and test result.
6. Human approver, decision date, and rollback owner.

If any field is unknown, mark **BLOCKED — KEEP**.

## 4. Safe cleanup lifecycle

1. **Discover:** read-only inventory and dependency scan.
2. **Classify:** KEEP, MERGE, QUARANTINE CANDIDATE, or BLOCKED.
3. **Propose:** create a change list with rationale and impact for review.
4. **Quarantine:** where technically safe, disable only the redundant schedule or move the asset to a clearly named archive branch; do not alter production entry points.
5. **Observe:** run relevant regression, deployment, security, and revenue acceptance checks.
6. **Approve:** require explicit human approval before destructive changes.
7. **Delete:** remove only the approved exact targets, one bounded batch at a time.
8. **Verify:** prove critical routes and metrics are unchanged; retain an audit note and recovery instructions.

Never auto-delete from a GitHub Actions workflow. Automated cleanup may produce a report or proposed patch only.

## 5. Automission stop/continue rules

- Stop and alert on unexplained production failures, missing backups, permission changes, secret exposure, integrity mismatch, or evidence gaps.
- Continue only when the next action is bounded, reversible, authorised, and contributes to a named outcome.
- Do not create a new workflow when an existing workflow already supplies the same evidence and ownership.
- Deduplicate by function and acceptance criteria, not by similar names.
- Treat queued, pending, skipped, cancelled, failed, and successful runs as distinct states.
- Do not rerun cancelled jobs until their cause and side effects are understood.
- Cap concurrent runs and respect repository concurrency groups; do not cancel a required security or deployment gate merely to speed up the queue.
- Every automation must have an owner, purpose, trigger, inputs, outputs, failure path, retention policy, and measurable acceptance test.

## 6. Minimum success metrics

Track per week:
- repeated or duplicate tasks removed from the queue;
- median time from request to accepted result;
- percent of tasks with a named user/customer outcome;
- false-positive quarantine recommendations;
- production/security regressions (target: zero);
- rollbacks and recovery time;
- successful outcomes with linked evidence.

Do not optimise only for fewer workflows. The objective is less wasted cycle time with no loss of protection or product capability.
