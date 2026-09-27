# Nishpaksh Inspection App — architecture v1

## Objective
Build an evidence-first inspection application in which a person first declares what the inspection is for, then receives a purpose-specific process. The system records observations, evidence, reasoning, uncertainty, review and appeals.

The application is not an automated authority that decides who is fit to be a minister, PM, CM, judge, employee, student or any other consequential role.

## Purpose selector
1. Self / human understanding
2. Education / learning
3. Employment / work role
4. Public-service role
5. Organizational role
6. Research claim / theory

The selected purpose becomes part of the inspection record; a changed scope starts a new inspection or records an explicit scope change.

## Inspection pipeline
Purpose → Consent → Scope → Questions → Evidence → Multi-angle analysis → Countercases → Human review → Certificate of record → Appeal/archive

## Evidence-first questions
Questions distinguish fact claims, personal experience, value propositions, hypotheses, predictions, interpretations and source-dependent claims. AI coherence is never treated as proof.

## Multi-angle language analysis
For important statements the agent may separately record literal meaning, definitions, context, ambiguity, assumptions, evidence requested, supporting evidence, counterevidence, alternative interpretations, logical dependencies, uncertainty and reproducibility path. Original wording is preserved.

## Optional sensing research
Camera, microphone, eye-tracking, finger-vein or other sensor modules may be researched as separate experimental measurements. They must not infer truthfulness, character, political preference, intelligence, health or eligibility, and must not determine certificate outcomes.

## Human review
Consequential certificates require qualified human review appropriate to the purpose. The reviewer sees original answers, evidence, provenance, AI analysis, countercases, uncertainty and audit history, then records a reasoned decision or requests more evidence.

## Certificate model
The certificate is a process/evidence record, not a universal certificate of a person's worth or truth.

It can document completion of a scope, presented documents, recorded evidence states and human review. It must not silently state legal eligibility, medical fitness, political suitability, personal truthfulness or universal scientific proof.

## AI-agent architecture
- PurposeAgent — validates inspection scope.
- QuestionAgent — generates questions from approved templates.
- LanguageAgent — performs multi-angle semantic analysis.
- EvidenceAgent — indexes evidence and provenance.
- CountercaseAgent — searches for disconfirming evidence and alternative interpretations.
- ReasoningAgent — checks logical consistency and unsupported jumps.
- PrivacyAgent — minimizes sensitive collection and enforces retention.
- AdversarialQC — tests prompt injection, fabricated evidence, contradictions and bypasses.
- CertificateAgent — composes records only from completed gates.
- AuditAgent — records execution and provenance.

## Status vocabulary
REGISTERED → EVIDENCE_PENDING → HUMAN_REVIEW → ISSUED
Side states: DISPUTED / EXPIRED / REVOKED / NOT_VERIFIED / DEFERRED

## 850-crore-scale engineering target
The design should be capable of global scale, but scale is an engineering target, not a claim of current capacity.

Requirements: multilingual UTF-8 records, regional data-residency controls, tenant isolation, consent ledger, encrypted sensitive storage, append-only audit events, idempotent queues, rate limiting, disaster recovery, accessibility, low-bandwidth mode, offline-first evidence capture where lawful, cryptographic provenance, model/version registry and appeal/correction workflows.

## Governance gates
Before production use in education, employment, public service or other high-impact settings: jurisdiction-specific legal review, privacy review, security threat model, accessibility review, bias/performance evaluation, human oversight, appeal/correction, retention/deletion controls and independent audit where appropriate.

## Integration with Shirmani Research Institute
Research chain: Source → Normalize → Claim → Evidence → Formulation/Test → Verification → QC → Publication → Archive
Inspection chain: Purpose → Consent → Observation → Evidence → Analysis → Human Review → Certificate Record
AI/workflow success never becomes independent verification merely because a workflow passed.

## First implementation milestone
Implement the schema and deterministic validation first. Then build a non-production prototype UI around SELF_AS_HUMAN and RESEARCH_CLAIM, followed by purpose-specific templates. Production use for consequential roles remains gated by human review and jurisdiction-specific controls.
