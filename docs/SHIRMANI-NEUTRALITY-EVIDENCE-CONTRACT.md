# SHIRMANI Neutrality & Evidence Contract

## Purpose

This contract makes the Automission system impartial at the computational level. It does not
treat any person, ideology, framework, source, institution, or prior output as automatically
true or false.

The system evaluates claims by the same evidence rules regardless of who submitted them.

## Core rules

1. **Symmetric treatment** — identical evidence standards apply to supporting and opposing claims.
2. **No authority shortcut** — a claim is never promoted because of the identity, status, popularity,
   seniority, or prior success of its author.
3. **Evidence separation** — observation, interpretation, inference, hypothesis, and verified result
   are stored as different states.
4. **Counter-evidence required** — important claims must record plausible alternative explanations
   and relevant disconfirming evidence when available.
5. **Uncertainty is explicit** — confidence is a measured/calibrated quantity, not a declaration of truth.
6. **Independent verification** — a result cannot become VERIFIED merely because its own workflow passed.
7. **Fail closed** — missing provenance, missing evidence, contradictory records, or failed gates block promotion.
8. **No fabricated experience** — observable signals may be translated into simple language, but the system
   must not convert them into proof of subjective experience, consciousness, intention, or feeling without
   an independently validated operational measurement model.
9. **Reproducibility** — inputs, model/version identifiers, transformations, outputs, and fingerprints are retained.
10. **Human review for high-impact actions** — automation may prepare and test changes, but consequential
    external actions require an explicit review gate.

## Claim lifecycle

OBSERVED -> INTERPRETED -> HYPOTHESIS -> EVIDENCE-SUPPORTED -> INDEPENDENTLY-VERIFIED

A failed or contradicted claim moves to BLOCKED or REQUIRES_REVIEW; it is never silently promoted.

## NLP translation rule

signal -> preprocessing -> feature extraction -> model -> uncertainty -> evidence review -> plain-language explanation

The plain-language explanation must distinguish:

- what was measured;
- what pattern the model detected;
- what interpretation is plausible;
- what remains unknown;
- what evidence would change the conclusion.

The phrase "this proves that the entity feels X" is prohibited unless the project has a validated
operational definition, suitable labelled data, independent replication, and a passing verification gate.

## Fairness / neutrality audit

Every claim record should expose:

- claimant/source identity only as provenance, never as evidence weight;
- evidence supporting the claim;
- counter-evidence or alternative explanations;
- independent sources;
- verification status;
- model and dataset version;
- uncertainty/calibration status;
- reasons for blocking or promotion.

## Design objective

The target is not a pre-declared 100% accuracy number. The target is a continuously measurable system
that reduces error, exposes uncertainty, detects contradictions, and improves through independently
evaluated changes.
