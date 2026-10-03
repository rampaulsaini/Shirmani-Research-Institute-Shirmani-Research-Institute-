# SHIRMANI Independent Review Packet — 2026-10-03

## Purpose

Convert the existing independent-verification queue into concrete, reproducible review tasks without changing any existing record to VERIFIED.

The repository's fail-closed rule remains authoritative: workflow success, author-authored material, generated packets, or automated comparison do not constitute independent verification.

## Review protocol

For each record:

1. Preserve the exact claim text and record ID.
2. State a measurable operational definition.
3. Use independent sources or a reproducible observation/test.
4. Record counter-evidence and alternative explanations.
5. Record the test environment and reproduction steps.
6. Record the observed result without upgrading its status automatically.
7. An independent reviewer records identity/role, date/time, and explicit decision.
8. Only the reviewer's explicit decision can permit VERIFIED.

## Review tasks

### IV-001 — Stars and galaxies change/evolve over time

Operational test:
- Compare independently sourced descriptions of stellar life cycles and galaxy evolution.
- Identify at least two independent sources not authored by this repository.
- Record the specific observational evidence supporting temporal change/evolution.
- Record relevant limitations or uncertainty.

Decision boundary:
- Evidence-supported is not the same as VERIFIED for this registry.
- VERIFIED requires the complete protocol plus an independent reviewer decision.

### IV-002 — Galaxies can collide and merge and their structures evolve

Operational test:
- Independently inspect documented observations/models of galaxy collisions, mergers, and structural evolution.
- Record the observable phenomenon, source, and reproducible analysis path.
- Record counter-evidence or limitations.

Decision boundary:
- Do not infer verification merely from the existence of NASA or other authoritative documentation.

### IV-003 — Human activity affects climate, ecosystems and biodiversity

Operational test:
- Independently inspect assessment evidence concerning anthropogenic influence and measurable impacts on climate, ecosystems, and biodiversity.
- Separate observed evidence, attribution, uncertainty, and causal interpretation.
- Record counter-evidence and limitations.

Decision boundary:
- The reviewer must explicitly state which part of the claim was tested and what remains outside the test.

### IV-004 — First-person self-knowledge and prereflective self-consciousness are established objects of philosophical analysis

Operational test:
- Independently inspect at least two scholarly sources.
- Identify the precise propositions those sources support.
- Distinguish “is a subject of philosophical analysis” from stronger claims about objective mechanisms of consciousness.

Decision boundary:
- Philosophical treatment does not automatically establish a universal scientific mechanism.

### IV-005 — Author-defined construct

Classification:
- Preserve as AUTHOR-DEFINED unless an independent testable proposition is extracted.
- Do not convert a definition into an empirical truth claim.

### IV-006 through IV-009 — Currently NOT_VERIFIED

Required next step:
- Create precise operational definitions and test protocols before any verification decision.
- For IV-009 in particular, define a common metric and comparator before making any quantitative superiority claim testable.

### IV-010 — Author-proposed protection objective

Classification:
- Preserve as AUTHOR-PROPOSED.
- If desired, create separate empirical claims about measurable effects of particular environmental or social interventions.

## Integrity requirements

- No automatic VERIFIED promotion.
- No deletion or rewriting of the canonical user-source record.
- No conflation of evidence-supported, verification-ready, and independently verified.
- Every promotion must be traceable to an explicit independent reviewer decision.
- If evidence is insufficient or contradictory, retain NOT_VERIFIED, INCONCLUSIVE, or CONTRADICTED as appropriate.

## Current queue baseline

- Queue records: 10
- Evidence-supported: 4
- Author-defined/proposed: 2
- Not verified: 4
- Independently verified: 0
- Independent verified percentage: 0%

This packet improves review readiness; it does not change those counts.
