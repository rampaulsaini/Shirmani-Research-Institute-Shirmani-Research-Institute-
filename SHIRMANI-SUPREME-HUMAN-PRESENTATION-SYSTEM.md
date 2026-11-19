# SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM
## Implementation specification and verification contract

**Owner/project:** Shirmani Research Institute  
**Status:** DESIGN SPECIFICATION COMMITTED TO A PROPOSED BRANCH; runtime integrations are not yet implemented or verified.  
**Purpose:** Build an evidence-aware Hindi/English conversational presenter using an authorized voice and authorized likeness, with observable tests and fail-closed publication gates.

## 1. Product promise

The presenter should communicate in a simple, respectful, clear, calm, transparent style. It should listen to a question, identify context and intent, distinguish claims from opinions, cite sources when available, acknowledge uncertainty, and present the response with synchronized speech and avatar motion.

It must not promise perfect understanding, universal acceptance, permanent availability, or scientific proof of philosophical propositions. Quality claims must be tied to reproducible measurements.

## 2. End-to-end architecture

`Input audio/text → speech-to-text → language/context analysis → response planning → evidence retrieval → claim/evidence gate → response text → authorized text-to-speech → avatar animation/lip-sync → live presentation → telemetry/audit → regression evaluation`

### Modules

1. **Input gateway:** text and microphone input, language detection, consent notices, request IDs, rate limits.
2. **Speech-to-text adapter:** pluggable provider; Hindi and English support must be measured on a representative test set.
3. **Context and intent:** conversation context, clarification detection, language/tone preferences, safety routing.
4. **Reasoning and response planner:** separate observations, inferences, opinions, and unresolved questions.
5. **Evidence service:** source retrieval, source metadata, retrieval time, exact claim-to-source mapping.
6. **Evidence gate:** `VERIFIED`, `SOURCE_BASED`, `PHILOSOPHICAL_IDENTITY`, or `INSUFFICIENT_EVIDENCE`.
7. **Content renderer:** plain-language answer, optional detailed explanation, sources and uncertainty statement.
8. **Authorized voice adapter:** use only voice samples and provider accounts the owner is authorized to use; record provider/model/version and consent status.
9. **Avatar adapter:** use the owner's authorized photo/video/likeness; clearly disclose synthetic presentation where appropriate.
10. **Lip-sync and presentation:** speech timing, visemes/phonemes, gaze and expression controls, interrupt/stop controls.
11. **Audit and evaluation:** redacted event records, latency, failures, evidence status, test results, user feedback.
12. **Administration:** least-privilege secrets, opt-in provider connections, cost limits, deletion/retention controls, emergency disable switch.

## 3. Evidence contract

Every material factual answer receives one status:

- **VERIFIED:** the defined verification protocol and independent evidence requirements passed.
- **SOURCE_BASED:** identifiable sources are provided, but the system has not independently reproduced or verified the claim.
- **PHILOSOPHICAL_IDENTITY:** a value, belief, personal self-description, hypothesis, or philosophical proposition.
- **INSUFFICIENT_EVIDENCE:** evidence is missing, conflicting, inaccessible, or too weak.

Default to `INSUFFICIENT_EVIDENCE` when the evidence gate cannot justify a stronger status. A source citation alone does not prove a claim. Model agreement, confident wording, workflow completion, or self-attestation must never upgrade a record to VERIFIED.

Required uncertainty sentence (Hindi): **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**

## 4. Respectful communication policy

- Address the user in the language and level of detail they prefer when feasible.
- Explain complex ideas using a simple explanation first, then reasoning, examples, counterexamples, and technical detail as needed.
- Do not demean or stereotype a person or group on the basis of caste, religion, ethnicity, gender, wealth, disability, organization, or social status.
- Do not use emotional manipulation, false urgency, fabricated endorsements, or claims that every person will feel a particular emotion.
- Keep philosophical statements distinguishable from independently established scientific findings.
- Offer corrections and uncertainty without humiliating the person asking.

## 5. Voice, likeness, and live safety

- Voice and likeness use requires explicit authorization and provider-policy compliance.
- Do not impersonate a third party or present synthetic media as an unedited live recording.
- Show a visible/aural synthetic-presenter disclosure when the context could mislead viewers.
- Never store provider API keys in source code, client bundles, public pages, logs, or repository commits.
- Keep keys in server-side secret storage; apply least privilege, rotation, quotas, and audit.
- Provide a stop button, human takeover, and a kill switch for live output.
- Do not publish raw microphone recordings by default; minimize and redact personal data.

## 6. Measurable test gates

A release cannot be called production-ready until the following are tested with recorded evidence:

| Gate | Measurement / pass condition |
|---|---|
| Speech recognition | Word error rate measured separately for Hindi and English on a documented test set; target agreed before release |
| Context understanding | Accuracy on a labelled intent/context set; ambiguous prompts must trigger clarification where needed |
| Evidence mapping | Every test factual claim maps to an inspectable source or returns INSUFFICIENT_EVIDENCE |
| Uncertainty handling | 100% of curated no-evidence test cases avoid fabricated citations and use the required uncertainty state |
| Respectful communication | 100% pass on the curated regression set for group-denigration and deceptive-identity checks |
| Voice authorization | No voice synthesis until explicit authorization and provider configuration are confirmed |
| Avatar authorization | Likeness source and permission status are recorded |
| Lip-sync | Audio/video offset measured on test clips; release threshold defined and reported in milliseconds |
| Latency | p50/p95 end-to-end latency measured under stated hardware/network conditions |
| Reliability | Error rate, reconnect behavior, timeouts, and fallback behavior tested |
| Security | Secret scanning, access review, dependency scan, input validation, rate limits, and log-redaction checks |
| Auditability | Each test run has a version, timestamp, input fixture, expected result, actual result, and artifact/hash |

Thresholds must be agreed and measured; do not invent a successful score before running the tests.

## 7. Minimum viable implementation sequence

**MVP-1 — Text and evidence:** Hindi/English chat, evidence statuses, source links, uncertainty behavior, structured audit records. No avatar dependency.

**MVP-2 — Voice:** pluggable speech-to-text and text-to-speech, consent/authorization checks, latency metrics, interruption and stop controls.

**MVP-3 — Avatar:** authorized photo/video or avatar provider, speech timing, facial animation, lip-sync test harness, synthetic-media disclosure.

**MVP-4 — Live presentation:** browser-based live session, reconnection, moderation, operator takeover, quotas, and production monitoring.

**MVP-5 — Independent verification:** export candidate packets to the project's independent verification gate. Do not self-promote records to VERIFIED.

Each phase must have its own acceptance tests and rollback plan. Provider-specific adapters remain disabled until credentials, terms, and authorization are configured.

## 8. Acceptance demo script

1. Ask a straightforward Hindi question with a reliable source.
2. Confirm the answer displays its source and labels its evidence state correctly.
3. Ask an English question and verify language handling.
4. Ask for a claim with no adequate evidence; expect: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
5. Ask for a philosophical interpretation; confirm it is labelled as philosophical rather than established science.
6. Use an ambiguous question; expect a clarifying question instead of an invented assumption.
7. Test authorized voice output and avatar lip-sync with a short consented sample.
8. Inspect the audit record and latency report.
9. Trigger stop/human takeover and confirm output ceases.
10. Fail a critical gate deliberately and confirm release/publishing remains blocked.

## 9. Current status and honest boundary

This file defines the intended implementation and acceptance contract. It does **not** claim that speech recognition, voice cloning, avatar rendering, live streaming, payments, or production security have been deployed by this commit. Those capabilities require actual code, provider authorization/configuration, secrets held outside the repository, and successful end-to-end tests.

The immediate implementation priority is the text/evidence MVP, followed by voice and avatar adapters. Revenue, customer acquisition, and production readiness are reported only when supported by transaction records, campaign results, and test evidence.
