# Blog Claim Verification Methodology

## Purpose

This repository treats the author's blog/source text as source material, not as automatic proof.
The research pipeline must preserve the author's wording while independently evaluating claims.

## Canonical pipeline

Blog/source -> source snapshot -> paragraph/sentence units -> atomic claims -> claim classification -> evidence -> counter-evidence -> reproducibility -> independent review -> audit -> final status.

## Claim classes

- FACTUAL_CLAIM
- SCIENTIFIC_CLAIM
- HISTORICAL_CLAIM
- EVENT_OR_ALLEGATION
- PERSONAL_EXPERIENCE
- PHILOSOPHICAL_PROPOSITION
- DEFINITION
- PREDICTION
- NON_FALSIFIABLE
- GENERAL_CLAIM

## Final statuses

- VERIFIED
- PARTIALLY_VERIFIED
- SUPPORTED
- DISPUTED
- CONTRADICTED
- UNVERIFIED
- PERSONAL_EXPERIENCE
- PHILOSOPHICAL_PROPOSITION
- DEFINITION
- PREDICTION
- NON_FALSIFIABLE

## Evidence rule

A claim may be promoted to VERIFIED only when the review record contains:
1. the exact source claim and source locator;
2. a stable source hash;
3. definitions/interpretation used for verification;
4. appropriate primary or high-quality independent evidence;
5. relevant counter-evidence or alternative explanations;
6. reproduction/test evidence where applicable;
7. uncertainty and limitations;
8. an independent reviewer/audit record.

Generated reasoning, automated QC, search results, or the author's own assertion are not independent verification by themselves.

## Special handling

### Personal experience
First-person experiences are preserved as testimony. They are not converted into universal factual claims merely because they are sincerely reported.

### Philosophical propositions
Definitions such as “Shiromani Form” or “continuity of complete satisfaction” are recorded as the author's conceptual framework. Their internal consistency may be examined separately from empirical truth.

### Scientific claims
Claims about mind, time, consciousness, biology, physics, or other empirical mechanisms require domain-appropriate evidence and operational definitions.

### Historical/event claims
Claims about people, organizations, events, dates, followers, finances, expulsions, or statements require independent documentary or corroborating evidence where available. Serious allegations remain attributed to the source until corroborated.

### Universal/absolute claims
Claims such as “everyone,” “no one in history,” “always,” “never,” “permanent,” or quantitative comparisons such as “trillions of times deeper” require unusually explicit definitions and evidence.

## Completion metric

Research completion is measured from the actual blog-derived atomic claim inventory, not from a pre-existing synthetic queue.

VERIFIED / total source-derived claims × 100

Other statuses remain visible and are not silently counted as verified.

## Three-track reporting

Every research report should keep these distinct:
1. Source track: what the author says.
2. Evidence track: what independent evidence establishes.
3. Difference track: where the source claim and evidence agree, differ, or remain unresolved.

## Fail-closed principle

No automation may self-certify its own generated output as VERIFIED. Automation can extract, classify, search, organize, QC, and prepare review packets. Promotion to VERIFIED requires the independent review/audit gate.

## Source preservation

The original wording must remain recoverable through:
- canonical URL;
- retrieval timestamp;
- source hash;
- document/paragraph/sentence locator;
- exact source text;
- normalized text only as a secondary representation.

The normalized representation must never replace the preserved original.

## Research objective

The goal is neither to prove nor disprove the author's worldview in advance. The goal is to make each claim inspectable, attributable, reproducible where possible, and explicit about uncertainty.