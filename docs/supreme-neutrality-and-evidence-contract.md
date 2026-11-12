# SHIRMANI Supreme Neutrality & Evidence Contract

Purpose: add a strict neutrality/evidence layer to the existing AI-ML-NLP Automission stack.

## Core invariants
- No favoritism toward a person, institution, ideology, hypothesis, source, or conclusion.
- Evidence before certainty; observation, analysis, hypothesis, evidence-supported, and independently-verified are separate states.
- Preserve attribution for user, model, document, and external-source claims.
- Counter-evidence must remain visible.
- Confidence is measured/calibrated, never declared as absolute accuracy.
- Observable signals do not by themselves prove subjective experience.
- A workflow passing its own tests is not independent verification.
- Insufficient evidence blocks promotion to VERIFIED.
- Provenance, fingerprints, model/version information, and evaluation evidence are required for promotion.
- High-impact external actions require explicit human authorization.

## Interpretation ladder
SOURCE -> OBSERVATION -> ANALYSIS -> HYPOTHESIS -> EVIDENCE-SUPPORTED -> INDEPENDENTLY-VERIFIED

## NLP output contract
Separate what was observed, inferred, hypothesized, and independently verified.
For uncertain multimodal signals, use simple language that explicitly states the evidence boundary, confidence, and limitations.

## Fair comparison rule
When multiple explanations are plausible, preserve relevant alternatives plus supporting and counter-evidence. Do not label an explanation certain unless the applicable evaluation protocol establishes that status.

## Automission rule
Scheduled cycles may inspect, benchmark, detect regressions, generate evidence requests, create audit artifacts, and propose improvements.
Scheduled cycles may not silently promote unverified claims, delete counter-evidence, change governance rules, manufacture evidence, or mutate production code outside the controlled review path.

## Accuracy
Supreme accuracy is an engineering target, not a guarantee. Track calibration error, precision/recall/F1 where labels exist, abstention, false positives/negatives, cross-source agreement, replication, provenance completeness, and regression rate.
