# Nishpaksh Understanding AI — Platform Specification

**Project:** Shirmani Research Institute  
**Framework:** Nishpaksh Samaj / Yatharth Siddhant  
**Status:** Specification; prototype and independent review remain pending.

## Purpose
Build an accessible, multilingual platform that helps people examine a clearly stated question against transparent criteria, review evidence, identify uncertainty, and produce an explainable report. It supports learning and informed human decisions; it does not declare intrinsic worth, humanity, moral purity, mental state, or universal truth.

Preserve framework vocabulary such as निष्पक्ष समझ, शमीकरण, यथार्थ सिद्धांत, हृदय दृष्टिकोण, and मस्तक दृष्टिकोण as attributed concepts. Do not silently convert them into empirical facts.

## Assessment modes
1. **Self-reflection:** voluntary private prompts; reflective, never diagnostic.
2. **Education and skills:** curriculum-aligned questions, practical tasks, and published rubrics.
3. **Employment:** role-specific competencies, work samples, accommodations, and human review.
4. **Public-service learning:** educational scenarios about duties, transparency, conflicts of interest, and service delivery. Results are informational, not appointment, legal finding, or fitness verdict.
5. **Research/claims review:** claim, definitions, sources, evidence, countercases, method, uncertainty, and independent verification.

Every assessment states its purpose, population, rubric version, data collected, limitations, review path, and retention period before collection.

## Assessment dimensions
Use only relevant, documented criteria: factual knowledge and source literacy; reasoning steps; distinguishing fact, interpretation, hypothesis, and opinion; evidence quality and provenance; relevant duties or curriculum; practical performance against a published rubric; acknowledgement of uncertainty and counterevidence; accessibility, language comprehension, and context.

**Biometric boundary:** Do not infer personality, honesty, compassion, intent, intelligence, mental health, or character from facial appearance, eye movement, voice, gait, fingerprints, finger-vein patterns, or other biometrics. Biometric inputs are excluded from scoring and eligibility decisions. If identity verification is legally necessary for a separate process, it must be purpose-limited, consent-based, access-controlled, and independent of assessment scores, with a practical alternative where possible.

## Evidence and result contract
Each result records assessment ID, rubric version, response/evidence references, criterion-level explanation, scoring method, missing-data and uncertainty markers, AI model/version where used, timestamp, reviewer role, appeal status, and provenance. Statuses: DRAFT, IN_REVIEW, REVIEWED, NOT_VERIFIED, WITHDRAWN.

A passing workflow, model output, generated certificate, or successful upload is not independent verification. Missing evidence never becomes a positive result. Certificates attest only to a specific assessment, rubric, date, and scope. The system must never certify whether someone is human or inherently fit for public office.

## Agent architecture
- **Intake:** validate purpose, consent, language, and required fields.
- **Language:** preserve originals; flag low-confidence translations.
- **Rubric:** select only approved, versioned rubrics.
- **Evidence:** extract candidate claims and link to supplied/approved sources; never invent citations.
- **Reasoning assistant:** show arguments, counterexamples, and uncertainty; no final high-impact decisions.
- **Scoring:** deterministic, rubric-bound scoring where possible; retain criterion calculations.
- **Bias/accessibility auditor:** test differential outcomes, accommodations, and language coverage.
- **Human review queue:** route consequential results to authorized reviewers; record disagreement.
- **Privacy/retention worker:** enforce deletion schedules, access controls, and audit logs.
- **Publication:** publish only approved, privacy-reviewed artifacts.

Agents require least privilege, bounded retries, idempotency keys, rate limits, and recovery/dead-letter handling. Configuring a model or passing a workflow does not prove an external model ran.

## Fairness, privacy, and safety
Minimize data; default to private/local processing for low-risk reflection. Consent must be informed and revocable for optional data. Never expose personal responses in public artifacts. Production requires encryption in transit/at rest, role-based access, and access logs. Provide correction, export, deletion, and appeal mechanisms. Test accessibility and language quality with representative participants.

Do not use this system as a mandatory gate for voting, public rights, legal status, essential services, or recognition of a person's humanity. Public officials, judges, candidates, and other high-impact roles must not be automatically ranked or certified. Any lawful institutional use requires a transparent role-specific process, independent governance, human accountability, and legal review.

## Subscription and livelihood
Keep essential reflection, accessibility, and basic learning resources free or in a clear no-cost tier. Paid plans may offer optional advanced tools, institutional workspaces, storage, or human-reviewed services. Disclose price, renewal, cancellation, refunds, and deliverables before payment. Never promise income, employment, certification, or social outcomes. Keep financial records separate from assessment scores.

## Global-scale readiness
Serving 8.5 billion people is an ambition, not a verified forecast or current capability. Roll out progressively: accessible prototype; opt-in pilot with synthetic/test data; independent security/privacy/accessibility/fairness review; limited production with monitoring; regional scaling only after measured load, cost, support, and language tests. Design for low bandwidth, mobile, localization, RTL scripts, portability, and graceful degradation. Do not claim global readiness until tested.

## Acceptance gates
- [ ] Every assessment has a declared purpose and versioned rubric.
- [ ] Fact, interpretation, hypothesis, and opinion are distinguished.
- [ ] Scores are reproducible from recorded inputs.
- [ ] Missing evidence remains NOT_VERIFIED.
- [ ] No biometric-derived trait affects a score.
- [ ] High-impact outcomes require accountable human review and appeal.
- [ ] Consent, retention, export, deletion, and access controls are tested.
- [ ] Tests cover invalid input, missing evidence, duplicate jobs, retries, and recovery.
- [ ] Public claims distinguish prototype, pilot, production, and independent verification.

## Initial implementation sequence
1. Review this specification against the existing evidence contract.
2. Build an accessible static self-reflection/skills prototype using synthetic examples.
3. Add deterministic rubric scoring and a machine-readable result schema.
4. Add tests and workflow gates; keep external AI and biometric integrations disabled pending review.
5. Pilot with informed volunteers and revise from documented feedback.
