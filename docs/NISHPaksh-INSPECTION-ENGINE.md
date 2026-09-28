# Nishpaksh Inspection Engine

## Purpose
A neutral, evidence-first inspection layer for self-observation, education, role-based assessment, institutional/public-role workflows and research claims.

## Core routing
Target selection happens before subscription/inspection: self, education, role, public-office, research. The target controls the rubric and required evidence. It does not decide a person's worth, humanity, mental state, political suitability or legal eligibility.

## Evidence contract
input → normalize → claim → source → evidence → formulation → countercase → verification → uncertainty → human review → certificate/record

A certificate, when implemented, means only that the defined inspection process was completed and its stated checks passed. It must never silently mean “person is truthful” or “person is fit for office.”

## AI/ML/NLP modules
1. NLP normalization: language detection, segmentation, terminology and ambiguity extraction.
2. Claim parser: separates factual claims, interpretations, questions and values.
3. Evidence linker: attaches sources, provenance and evidence state.
4. Multi-angle consistency: checks internal contradictions and missing assumptions.
5. Countercase generator: produces testable alternative cases; it does not declare a winner.
6. Reasoning/formulation: reproducible logic, calculations and test records.
7. Verification router: sends eligible records to independent human verification.
8. Privacy layer: data minimisation, consent, retention and deletion controls.
9. Certificate layer: process-completion certificates with scope, timestamp, evidence references and verification state.

## Biometric boundary
Finger-vein, eye, face and voice sensing are optional future adapters only. Raw biometric identifiers are not part of the MVP record. No biometric signal is treated as proof of truth, character, intelligence, health or eligibility.

## Scale architecture
Static/PWA client → regional/API gateway → queue → stateless NLP workers → evidence/provenance store → verification queue → audit/event log → publication layer. Use idempotency keys, bounded payloads, encryption, rate limits, regional data controls and human escalation for high-impact decisions.

## Status semantics
NOT_VERIFIED is the safe default. VERIFIED requires independent verification. Automation success is not scientific or legal verification.
