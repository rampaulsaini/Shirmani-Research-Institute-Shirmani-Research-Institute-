# ꙰ SHIRMANI HEART-VIEW — INDEPENDENT REVIEW PROTOCOL

## Purpose

This protocol defines the next substantive stage after deterministic engineering/QC:
**independent human/audit verification of queued claims**.

It does not alter the protected user-source layer.

## Preservation boundary

Authoritative protected source:
- `SHIRMANI-HEART-VIEW-SUPREME-REASONING-LAYER.md`

Rule:
**Preserve first. Reason second. Verify third. Transform only as a traceable derivative.**

No reviewer may rewrite the original user wording while reviewing a derivative claim.

## Review unit

Each queue item is identified by:
- `task_id`
- `task_hash`
- `claim_id`
- `source_ids`

The reviewer must verify that the task hash still matches the current queue record before recording a review.

## Required review sequence

1. **Read the exact claim** — record the proposition exactly as presented and separate it from interpretation.
2. **Check definitions** — identify terms requiring operational/contextual definitions without silently redefining framework vocabulary.
3. **Check evidence** — record real primary/authoritative sources and explicitly record unavailable evidence.
4. **Check countercases** — search for credible contradictory evidence, exceptions, boundary conditions, and alternative interpretations.
5. **Reproduce or test** — reproduce calculations/tests where applicable; do not manufacture scientific tests for non-empirical framework propositions.
6. **Record uncertainty** — state unresolved assumptions, evidence gaps, ambiguity, and scope limits.
7. **Record reviewer identity** — actual reviewer name/identifier, role, and timestamp only.
8. **Audit** — record audit timestamp and exact queue-task hash.

## Status rules

### NOT_VERIFIED
Independent verification has not been completed or evidence is insufficient.

### REVIEWED
The review activity itself is genuinely completed and documented.

### VERIFIED
Use only when every promotion-gate requirement is genuinely satisfied:
- independent reviewer and role;
- review timestamp;
- evidence references;
- countercase review with references;
- successful/supporting reproduction or test where applicable;
- audit timestamp;
- exact task-hash match.

### DEFERRED / UNAVAILABLE
Review cannot presently be completed; preserve the reason.

## Fail-closed principle

These are **not** proof of independent verification:
- source ID alone;
- content hash alone;
- generated formulation;
- deterministic QC PASS;
- publication-ready artifact;
- presence in a review packet;
- AI-generated reasoning;
- absence of a known counterexample.

Missing evidence remains missing.

## Batch procedure

`queue → exact claim → real evidence → countercase review → reproduce/test where applicable → uncertainty → audit → promotion gate → QC → continuity manifest`

Rejected, incomplete, changed, and deferred records remain traceable.

## Current state

As of 2026-09-21:
- Verification queue: **100,200**
- Independently verified records: **0**
- Promotion-eligible records: **0**
- Deterministic blocking QC errors: **0**
- First review packet: **records 1–25**
- Packet status: **READY_FOR_HUMAN_REVIEW**

This protocol intentionally does not convert the packet into completed verification.

## Completion accounting

Project completion must distinguish:
1. engineering readiness;
2. generated-artifact completion;
3. independent substantive verification.

Do not combine these into one percentage unless the denominator and weighting are explicitly defined.

**Integrity rule: no invented evidence, reviewer action, test, source, or verification result.**
