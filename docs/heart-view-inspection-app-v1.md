# SHIRMANI Heart-View Inspection App — V1 Architecture

## Purpose

A privacy-first inspection and self-understanding application built around the repository's evidence-first contract:

**purpose → consent → input → normalization → multi-angle analysis → evidence → uncertainty → human review → result → archive**

The app helps a person examine a declared purpose, reasoning, knowledge, conduct, work readiness, learning, and self-observation. It must not convert an automated score into a declaration of human worth, truth, guilt, medical status, or legal/political fitness.

## Inspection purpose must be selected first

Every session begins with one declared purpose:

- self_understanding
- education
- employment_or_skill
- role_specific_knowledge
- public_service_reflection
- research_participation

A session may record a role or office as context, but the automated system must not certify, rank, approve, reject, or predict a candidate for political/public office.

## Core inspection dimensions

1. Purpose clarity — what is being examined and why.
2. Definitions — operational definitions for important terms.
3. Reasoning — premise, inference, counterexample, uncertainty, contradiction checks.
4. Evidence literacy — source quality, provenance, reproducibility, claim/evidence distinction.
5. Knowledge & learning — demonstrated understanding, not memorization alone.
6. Communication — clarity, ambiguity detection, multilingual normalization, context preservation.
7. Consistency — compare answers across equivalent questions without hidden psychological inference.
8. Decision transparency — assumptions, alternatives, trade-offs, unresolved questions.
9. Ethical reflection — declared principles and concrete scenarios; no automated moral-worth score.
10. Practical capability — task demonstrations where appropriate.
11. Self-observation — structured reflection and user-controlled notes.
12. Accessibility — language, reading level, assistive modes, accommodations.
13. Privacy & security — data minimization, retention controls, export/delete controls, audit trail.
14. Verification state — DRAFT, CHECK, HUMAN_REVIEW, NOT_VERIFIED, or VERIFIED only when the required independent process occurred.

## Multimodal inputs

Text, audio, and ordinary user-provided documents/images may be accepted when genuinely necessary for the declared task.

### Biometric boundary

Finger-vein sensing, iris/eye recognition, facial recognition, or similar biometric processing is not part of V1 certification. The system must not infer sensitive traits, identity, emotion, deception, criminality, political preference, medical condition, intelligence, or human worth from face, eye, voice, gait, handwriting, or physiological signals.

Any future research module would require separate privacy, security, legal, scientific-validity, consent, and human-review gates and must not silently enter the public certification pipeline.

## NLP multi-angle analysis

For each substantive answer, the analysis record may include claim extraction, definition extraction, source/evidence references, premise/conclusion mapping, ambiguity candidates, alternative interpretations, counterexamples, contradiction candidates, temporal/context qualifiers, uncertainty, provenance, and reproducible checks.

The model must distinguish: USER_ASSERTION != EVIDENCE != VERIFIED_FACT.

## Human review boundary

AI agents can prepare questions, normalize language, identify missing evidence, run deterministic checks, and assemble a traceable report.

Human reviewers remain responsible for consequential certification, credentialing, employment decisions, public-office decisions, legal determinations, medical conclusions, and other high-impact decisions.

## Certificates

A certificate records the scope and process completed, not a person's intrinsic value or universal truth.

Suggested states: INSPECTION_COMPLETED, EVIDENCE_REVIEWED, HUMAN_REVIEW_COMPLETED, NOT_VERIFIED, VERIFIED_FOR_DECLARED_SCOPE.

Every certificate includes purpose, scope, date, inputs considered, excluded inputs, evidence state, reviewer/process identity, limitations, and expiry/review conditions where applicable.

## Income / sustainability layer

Income remains a first-class product concern, but inspection results must never be sold as guaranteed income or used to manufacture financial claims.

Potential products include individual subscription for self-review/history, educational/research plans, organizational workflow tooling, paid human review where lawful, and privacy-preserving report/export services. Pricing and access control remain separate from evidence and verification state.

## Scalable architecture

Web/PWA → Consent & Purpose Gate → Session Engine → NLP/Reasoning Agents → Evidence Ledger → Deterministic QC → Human Review Queue → Certificate/Report → Audit Archive

For large-scale deployment: isolate tenant data, encrypt sensitive records, minimize retention, use append-only audit events, rate-limit agents, make model/version provenance explicit, and provide user export/delete controls.

## Initial workflow set

- inspection-purpose-gate
- consent-and-privacy-gate
- question-plan-builder
- multilingual-normalizer
- claim-evidence-mapper
- reasoning-consistency-check
- counterexample-and-alternative-view
- uncertainty-and-provenance
- human-review-queue
- certificate-scope-builder
- privacy-retention-audit
- income-product-learning

## Integrity invariant

No workflow success, model output, QC pass, generated certificate, or subscription state may by itself be treated as independent proof of a person's truth, worth, fitness, or scientific fact.
