# SHIRMANI HEART-VIEW — INDEPENDENT VERIFICATION REVIEW PROTOCOL

## Purpose

This protocol defines the human/audit boundary for the SHIRMANI HEART-VIEW SUPREME REASONING LAYER.

It does not alter the protected user-source layer and does not convert generated reasoning into independently established fact.

## Non-negotiable preservation rule

**Preserve first. Reason second. Verify third. Transform only as a traceable derivative.**

The protected source remains:

- `SHIRMANI-HEART-VIEW-SUPREME-REASONING-LAYER.md`

Original wording must never be replaced by a reviewer formulation.

## Verification task identity

Each review must identify the exact current task:

- task_id
- claim_id
- source_id(s)
- current_task_hash
- repository commit/ref
- review timestamp
- reviewer identity or audit identifier

A review for an older or changed task must not be silently reused.

## Required review record

A task may move from QUEUED to REVIEWED only when the reviewer records:

1. **Exact claim** — the proposition under review.
2. **Definitions** — operational meanings of important terms.
3. **Source evidence** — primary/secondary source, quotation, dataset, observation, calculation, or explicit no-source state.
4. **Evidence location** — exact path, page, line, URL, identifier, or reproducible test location where applicable.
5. **Countercase** — relevant contrary evidence, failure condition, or alternative interpretation.
6. **Reproduction/test** — independently repeated calculation, experiment, code/test, or documentary cross-check where applicable.
7. **Reasoning check** — whether the stated inference follows from the supplied evidence.
8. **Uncertainty** — what remains unresolved.
9. **Reviewer conclusion** — limited strictly to what the evidence supports.
10. **Audit trail** — reviewer action, timestamp, task hash, and repository reference.

## Status vocabulary

- **QUEUED** — awaiting independent review.
- **REVIEWED** — review completed and recorded, but promotion requirements are not necessarily satisfied.
- **VERIFIED** — all repository promotion requirements are satisfied and the review is independently auditable.
- **REJECTED** — the supplied evidence/reasoning does not support the task as currently formulated.
- **DEFERRED** — review cannot be completed because required evidence or reproduction is unavailable.
- **CHANGED_TASK** — task provenance/hash changed; a fresh review is required.

## Promotion rule

No task may be promoted to **VERIFIED** merely because:

- deterministic QC passed;
- a source record exists;
- a claim has generated evidence links;
- a reasoning record exists;
- an AI-generated formulation looks plausible;
- a previous review exists for a different task hash.

Promotion requires a complete independent review record matching the exact current task identity.

## Framework-language safeguard

Terms belonging to the user's framework may be preserved exactly as framework language. A reviewer must distinguish:

- user's original formulation;
- interpretation or derivative formulation;
- externally documented fact;
- empirical claim;
- unresolved proposition.

No philosophical proposition is to be silently presented as a scientific, historical, medical, or other empirical fact without appropriate independent evidence.

## Failure-safe behavior

If evidence is missing, contradictory, non-reproducible, or insufficient:

- do not invent evidence;
- do not invent a reviewer;
- do not invent a test result;
- do not convert CHECK to PASS;
- retain the task and its provenance;
- record the precise reason for rejection or deferral.

## Batch processing

Verification may be processed in batches, but every record must retain its own:

`task_id → task_hash → evidence → countercase → reproduction/test → reviewer → audit trail → status`

A batch summary may report counts, but it cannot substitute for the underlying review records.

## Current repository baseline

As of the current continuation checkpoint:

- verification queue: 100,200
- queue QC errors: 0
- registry reviewed: 0
- registry verified: 0
- promotion eligible: 0
- promotion gate: CHECK

These figures describe repository state only. They are not claims about the truth of the underlying propositions.

## Completion semantics

Generated artifact production may be complete while independent verification remains incomplete.

Therefore completion must be reported separately as:

- **Engineering/generated pipeline:** status of deterministic artifact production and QC.
- **Independent verification:** proportion of queue tasks with actual qualifying review records.
- **Overall research status:** not complete until the applicable verification requirements are genuinely satisfied.

## Core integrity statement

**No missing evidence, reviewer action, experiment, source, quotation, calculation, or verification result may be invented merely to increase the completion percentage.**
