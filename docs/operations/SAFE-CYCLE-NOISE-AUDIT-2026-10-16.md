# SHIRMANI Safe Cycle-Noise Audit
**Date:** 2026-10-16  
**Status:** Initial evidence log — not a claim that the full platform has been audited.

## Non-negotiable rule
Reduce waste without reducing product capability, security, data integrity, recovery, deployment reliability, or required validation. No workflow or file is deleted or disabled by name alone.

## Evidence observed
The supplied GitHub Actions snapshot for commit `e18cb2570d7a007c0114e7d4f2a3cda08033cb96` showed:
- Successful examples: Production Persistence & Truth Gate #1636 and #1635; Resilience Watchdog #2091; Deploy GitHub Pages — Production State #1046; Public Surface Security Smoke Gate #550; Supreme Security Code Scan #688.
- Pending examples: Public Production Automission #847 and Multi-Layer Production Automission #868 (serialization queue reported).
- Cancelled example: Read-Only Security Baseline #922.
- Several workflows have overlapping-sounding names, but names and a single screenshot do not prove functional duplication.

These statuses are a snapshot supplied by the repository owner, not a fresh, complete inventory of all runs.

## Initial disposition
| Candidate / area | Initial disposition | Why | Safe next step |
|---|---|---|---|
| Production Persistence & Truth Gate | KEEP | Explicit persistence/truth protection; two successful runs were shown | Inspect workflow definition and artifacts before considering trigger deduplication |
| Deploy GitHub Pages — Production State | KEEP | User-facing deployment protection | Preserve deploy and rollback path |
| Security Baseline / Supreme Security Code Scan / Public Surface Security Smoke Gate | KEEP | Distinct security and public-surface coverage is plausible; equivalence is not established | Compare exact checks, branch-protection requirements, and outputs |
| Public Production Automission #847 | KEEP / INVESTIGATE QUEUE | Pending due to serialization in supplied snapshot | Check concurrency group, queue duration, and whether an identical run supersedes it |
| Multi-Layer Production Automission #868 | KEEP / INVESTIGATE QUEUE | Pending due to serialization in supplied snapshot | Compare trigger, artifacts, downstream consumers, and unique coverage with #847 |
| Read-Only Security Baseline #922 | KEEP / INVESTIGATE CANCELLATION | Cancelled in supplied snapshot; reason unknown | Read run/job details and concurrency settings; rerun only after confirming it is safe and still needed |
| Other similarly named workflows | NOT VERIFIED | No full workflow inventory or content-level comparison yet | Inventory all workflow files, triggers, required checks, outputs, schedules, and consumers |

## Candidate scoring (must be evidence-backed)
For each workflow, record:
1. Unique deliverable or risk covered.
2. Trigger events, path/branch filters, schedule, and concurrency group.
3. Required status-check / branch-protection use.
4. Artifacts, state changes, downstream workflow dependencies, and external side effects.
5. Typical duration, queue time, run frequency, cancellation reason, and failure consequences.
6. Whether an equivalent workflow has demonstrably identical coverage and reliable outputs.

Disposition meanings:
- **KEEP** — useful or equivalence not proven.
- **CONSOLIDATE** — duplicate work is proven and can be merged without losing checks or artifacts.
- **DISABLE-CANDIDATE** — potentially redundant; requires a reversible trial and before/after evidence.
- **DELETE-CANDIDATE** — only after dependency/required-check review, owner approval, and a tested rollback plan.

## Safe implementation sequence
1. Inventory before editing.
2. Prefer narrow `paths` / `paths-ignore`, branch filters, deduplicated triggers, sensible concurrency groups, and bounded retries over deletion.
3. Never cancel a run that is the sole protection for a release, persistence repair, integrity check, or security gate.
4. Trial changes on a separate branch; compare artifacts, status checks, queue time, and downstream results.
5. Merge only if equivalent coverage and product behavior are preserved.
6. If evidence is missing, leave the workflow untouched and mark NOT VERIFIED.

## Completion gate
The audit is complete only when every workflow is listed, every proposed change has an impact/rollback plan, targeted checks pass, and no productive capability or protection has been lost. This document alone does not satisfy that gate.
