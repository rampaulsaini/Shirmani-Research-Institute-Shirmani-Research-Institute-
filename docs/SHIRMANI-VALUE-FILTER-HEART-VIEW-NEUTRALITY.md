# SHIRMANI Value Filter and Heart-View Neutrality Parameter

Status: proposed reviewable standard; not yet a deployed runtime gate.

## Purpose

Reduce duplicate work and workflow congestion without damaging useful production, source data, user assets, security controls, persistence, recovery, or publication. Evaluate work by observable contribution rather than by its name, volume, age, or a single green/cancelled run.

## A. Value filter for workflows, jobs, and tasks

Classify each item using evidence:

- **KEEP** — produces a unique useful artifact, protects a required capability, or is a dependency of a required gate.
- **MERGE** — overlaps with a canonical producer, and a tested consolidation preserves all outputs and consumers.
- **DISABLE-CANDIDATE** — likely redundant/no-op, but needs a reversible branch-level experiment and monitoring before disabling.
- **DELETE-CANDIDATE** — proven obsolete, no consumers, no unique outputs, no security/recovery role, and a tested rollback/recovery path.
- **INVESTIGATE** — ownership, dependencies, triggers, or output use are not yet known.

### Required evidence before changing a workflow

1. Inventory its trigger events, path filters, schedules, concurrency group, permissions, dependencies, outputs/artifacts, and downstream consumers.
2. Compare at least recent successful, failed, skipped, and cancelled runs; distinguish cancellation due to serialization/concurrency from substantive failure.
3. Identify the canonical workflow for each required output and prove output equivalence.
4. Check whether any production deploy, truth gate, persistence, security, integrity, rollback, recovery, customer, or public-page path depends on it.
5. Make one reversible change on a branch; run targeted tests and compare queue time, duplicate runs, useful outputs, stale-state rate, and recovery.
6. Merge only after review and evidence. Never bulk-delete based on names or run counts.

**Protected by default:** deployment, production truth gate, persistence, security baseline, media integrity, source/archive provenance, recovery/rollback, and any workflow whose dependencies are unresolved.

## B. Heart-View Neutrality and Care Parameter (HNP-100)

This is a practical review rubric inspired by the user's heart-centered philosophy. It is not a scientific measurement of a person's essence, consciousness, spirituality, IQ, or metaphysical truth. Do not claim a person's 99.9999% neutrality or any other precise percentage without a validated measurement method.

Score each criterion 0–5 from documented examples, then calculate the weighted score:

| Criterion | Weight | Review question |
|---|---:|---|
| Evidence and provenance | 25 | Are facts, sources, inferences, and unknowns separated? |
| Symmetric fairness | 20 | Are religious, nonreligious, and other viewpoints represented without automatic privilege or penalty? |
| Uncertainty and correction | 15 | Does the system acknowledge limits, ask when necessary, and correct mistakes? |
| Care and dignity | 15 | Does it communicate with empathy and respect without flattery or humiliation? |
| Agency and non-coercion | 10 | Does it avoid manipulation, pressure, and false authority? |
| Human and ecological impact | 10 | Does it consider foreseeable effects on people, nature, and the wider community? |
| Clarity and accessibility | 5 | Is the response understandable, transparent, and appropriately concise? |

Calculation: for each criterion, (score / 5) × weight; add the seven weighted results for a score from 0 to 100. Every score must include a short rationale and examples. If evidence is absent, mark **NOT VERIFIED** rather than awarding a high score.

### Guardrails

- The user's heart-centered perspective may guide tone and priorities; it must not be presented as independently proven universal fact.
- Do not label believers, atheists, intelligent people, or any group as mentally ill, unconscious, arrogant, or inherently biased.
- Treat bias as a possibility to test in a specific claim or decision, not as an immutable property of a whole group.
- No numeric score overrides safety, evidence, user agency, or a serious unresolved failure.
- A strong score is a review aid, not proof of perfection or a substitute for independent verification.

## C. Status labels

- **PASS** — concrete, reproducible evidence exists.
- **FAIL** — a required check produced a reproducible defect.
- **BLOCKED** — an identified prerequisite prevents the check.
- **NOT VERIFIED** — no adequate evidence has been obtained.
- **NOT APPLICABLE** — the criterion genuinely does not apply, with rationale.

Do not silently turn pending, cancelled, missing, or not-found resources into PASS or FAIL without checking what resource type and workspace they belong to.

## D. Current investigation notes — 2026-10-16

Read-only HeyGen lookups found:

- `5d938b91bb6841e9a9ddd93948c781b7` is an existing video titled **Avatar V Video**, status **completed**, duration approximately 8.46 seconds. This confirms render completion only; it does not independently verify lip-sync quality, original-media hash integrity, or live Q&A.
- `cc49ee728c9b4877b60a13365f4fffd5` is an existing private avatar group named **शिरोमणि रामपॉल सैनी**, with one look and status **completed**.
- `ba0ae3fdeb7f40afae0a3a3760b2a3ad` is not an asset or video in the current workspace lookup, but it **is** an avatar group named **शिरोमणि रामपाल सैनी** with 50 looks. Do not delete it: it is a real resource, and overlap with the other group is not proof that it is disposable.
- `f8b68463955c4358acca8f085d6ee13f` is not an asset or video in the current workspace lookup, but it **is** an existing **photo-avatar look** named **शिरोमणि रामपाल सैनी रिकॉर्डिंग स्टूडियो में**, belonging to group `ba0ae3fdeb7f40afae0a3a3760b2a3ad`. Do not delete it.
- The duplicate Pages publishing concern remains to be resolved by workflow-file/trigger/dependency inventory. No production workflow has been disabled or deleted by this document.
- Production truth-gate output and the deployed JSON/page must be checked separately against live deployment evidence.

## Definition of done

A cleanup is complete only when the proposed change is reviewed, dependency-safe, tested, reversible, and demonstrably reduces redundant work without reducing required outputs or protections. This document itself does not change runtime behavior.
