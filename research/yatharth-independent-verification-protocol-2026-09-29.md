# Yatharth Independent Verification Protocol — 2026-09-29

## Purpose
Independent verification must test the author's propositions rather than merely repeat, praise, or reject them.

## Status model
- AUTHOR-CLAIM: faithfully recorded from the author's material.
- OPERATIONALIZED: a claim has a measurable or logically inspectable definition.
- EVIDENCE-FOUND: external evidence relevant to the claim has been collected.
- COUNTER-EVIDENCE-FOUND: credible evidence against or limiting the claim has been collected.
- REPRODUCIBLE-TESTED: a documented test can be repeated by another reviewer.
- INDEPENDENTLY-VERIFIED: only when the evidence and method support the specific claim; this status is claim-specific, not a blanket approval of the framework.
- NOT_VERIFIED: evidence, definition, or test is insufficient.

## Claim families
1. Cosmic-scale propositions: test factual astronomy statements against authoritative observations/reviews.
2. Mind/heart propositions: translate “मस्तक” and “हृदय” into operational cognitive, affective, metacognitive, or physiological constructs before testing.
3. Self-realization propositions: distinguish first-person experience from universal empirical claims.
4. Lasting-change propositions: test whether claimed post-realization changes have reproducible longitudinal evidence.
5. Authority/dependence propositions: compare with psychology and sociology evidence on authority, attachment, conformity, coercion, and autonomy.
6. Nature-preservation propositions: compare normative claims with environmental science and measurable conservation outcomes.
7. Historical-comparison propositions: use primary texts first, then reputable scholarly interpretation; record similarities and differences without declaring a winner.
8. Logical propositions: check definitions, premises, inference validity, contradictions, counterexamples, and scope.

## Independence rule
A source authored by the framework owner can establish provenance of the author's claim, but cannot by itself establish independent verification of that claim.

## Comparison rule
The phrase “खरबों गुणा श्रेष्ठ” remains an author evaluation unless a specific metric, comparator set, population, method, and reproducible evidence are supplied. The system must not silently convert it into a research conclusion.

## Current baseline
The repository's existing conveyor correctly reports:
- Queue preparation can be complete.
- Packet QC can pass.
- Human/independent verification can still be NOT PERFORMED.
- VERIFIED promotion must remain 0 until a real verification gate is satisfied.

The next work is therefore to create claim-level independent evidence records, not to manufacture a non-zero percentage.

## Required record
Each claim should carry:
claim_id, exact_author_wording, operational_definition, comparator, primary_sources, secondary_sources, evidence, counter_evidence, test_method, result, reviewer_independence, status, timestamp.
