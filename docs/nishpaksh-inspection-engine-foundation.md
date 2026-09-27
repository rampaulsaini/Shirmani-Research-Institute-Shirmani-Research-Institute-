# Nishpaksh Inspection Engine — Foundation Specification

## Purpose
An evidence-first inspection application for a clearly declared target: education, role/job competency, public-service responsibilities, self-reflection, or general human-capability assessment.

The system produces a traceable assessment record. It must not infer a person's inherent worth, political preference, innocence, guilt, or universal truth from an automated output.

## Core flow
Target → Criteria → Consent/authority → Input → Normalize → Evidence → Multi-angle analysis → Counter-check → Human review → Decision record → Certificate

## Target modes
- EDUCATION — learning outcomes, comprehension, reasoning, source use and demonstrated skills.
- ROLE_COMPETENCY — requirements of a defined job/profession and evidence of capability.
- PUBLIC_SERVICE_ROLE — documented duties, qualifications and evidence review; consequential public-office use requires lawful authority and human review.
- SELF_REFLECTION — structured self-observation and reasoning exercises; never presented as a diagnosis.
- HUMAN_CAPABILITY — reasoning, communication, evidence handling, empathy and practical problem-solving; not a test of whether someone is biologically or morally human.

## Evidence hierarchy
1. Direct task performance / reproducible test
2. Primary records supplied or lawfully obtained
3. Independent corroboration
4. Secondary sources
5. Self-report
6. Unverified assertion

Every evidence item carries source, provenance, confidence, verification state and uncertainty.

## Analysis dimensions
Comprehension and language; reasoning and consistency; evidence/source literacy; quantitative and causal reasoning; counterexample handling; uncertainty calibration; problem decomposition; practical performance; communication; listening/perspective-taking; conflict handling; ethical/legal constraint recognition; time/context awareness; reproducibility; correction after feedback; provenance integrity; accessibility accommodations.

## Multimodal inputs
Future adapters may accept text, audio, video, documents and approved sensor data. Each modality is independently permissioned and logged.

### Biometric and sensor boundary
Fingerprint, vein, iris/eye, face, voice or other biometric signals must not be used as proxies for intelligence, honesty, moral worth, political suitability, or humanity. If identity authentication is needed, it must be a separate security subsystem with explicit consent or lawful authority, data minimization, retention limits, encryption and a non-biometric fallback.

Eye/gaze or facial micro-expression analysis must not be treated as reliable evidence of truthfulness or inner state unless a specific validated use case and lawful basis establish otherwise.

## Language analysis
NLP may examine literal meaning, definitions, claims versus evidence, assumptions, logical structure, ambiguity, counterclaims, consistency, source attribution and uncertainty. The original answer must remain preserved and every derived representation must have provenance.

## Certificates
No opaque universal score. Report criterion-level evidence and unresolved gaps.

Lifecycle: DRAFT → EVIDENCE_PENDING → ANALYSIS_COMPLETE → HUMAN_REVIEW → VERIFIED_FOR_TARGET → CERTIFIED. Other valid states include NOT_VERIFIED, INCOMPLETE, DISPUTED and EXPIRED.

A certificate means only that the defined criteria were reviewed to the stated evidence level at the stated time. It does not certify universal worth or universal truth.

## Governance gates
- Declare purpose, jurisdiction, target and criteria.
- Require consent or documented legal authority where applicable.
- Provide accessibility and language accommodation.
- Record conflicts of interest.
- Require human review for consequential decisions.
- Provide appeal and correction.
- Keep audit logs and model/version provenance.
- Apply retention, deletion, security and independent-validation controls.
- Never automatically deny employment, benefits, education, public office, civil rights or essential services solely from AI output.

## Subscription
Subscription is an access/service layer only. Payment status must never upgrade NOT_VERIFIED to VERIFIED.

## Privacy
Collect the minimum necessary data. Separate authentication data from assessment content where possible. Never expose credentials, payment-card data, unnecessary personal data or raw biometric templates in public evidence records.

## Scale
Design for very large populations with stateless services, queues, deterministic schemas, versioned model adapters, regional data controls, rate limiting, abuse prevention, observability and human-review queues. Large-scale readiness is an engineering target, not a claim of current capacity.

## Integrity rule
No evidence → no verification. No declared target → no assessment. No lawful authority/consent where required → no sensitive collection. No required human review → no consequential certification. No reproducible provenance → no strong claim.