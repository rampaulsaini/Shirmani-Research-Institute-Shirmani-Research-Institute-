# SHIRMANI Impartial Understanding & Human Presentation — v1

Status: **design specification; implementation and independent validation pending**.
Purpose: make the institute's heart-centred / impartial-understanding philosophy operational as a transparent, auditable review process, and define the evidence gates for avatar presentation.

## 1. Principle

Treat "heart-centred understanding" as a user-defined ethical design aspiration: care, clarity, humility, fairness, non-harm, and attention to people, animals, and the environment. Do not present metaphysical, spiritual, psychological, or historical interpretations as experimentally established facts without appropriate evidence.

The proposed 99.9999% / 0.0001% split is a **philosophical target label only**. It is not a probability, accuracy measure, IQ measure, clinical measure, or proof of impartiality. The default evaluation is unweighted and evidence-based until a public protocol, representative test set, and independent validation exist.

## 2. Response review pipeline

1. **Clarify** the user's goal and intended audience.
2. **Classify claim type**: evidence-based, interpretation, user-philosophy/identity, or insufficient evidence.
3. **Collect evidence**: record source URLs/IDs and what each source supports. No source means no VERIFIED status.
4. **Check counterviews**: identify credible alternative explanations or stakeholder perspectives where relevant.
5. **Check impact**: consider people, animals, environment, privacy, consent, and foreseeable misuse.
6. **State uncertainty** in plain language. Separate observation, inference, and value judgement.
7. **Self-review**: pass, revise, or insufficient evidence.
8. **Audit**: retain model/version, timestamp, evidence references, and review result without collecting unnecessary personal data.

## 3. Evidence states

- `VERIFIED`: the specific claim passed the defined checks with directly relevant evidence; this is not a guarantee of universal truth.
- `SOURCE_BASED`: credible source material exists, but the claim is not independently verified.
- `PHILOSOPHICAL_IDENTITY`: a person's self-description, values, or worldview; respect it without falsely treating it as a measured scientific result.
- `INSUFFICIENT_EVIDENCE`: evidence is missing, weak, conflicting, or not comparable. Fail closed; never silently upgrade this state.

## 4. Human-presentation chain

`Voice → Authorized Voice Integration → Test Q&A → Content/Evidence → Authorized Photo/Face → Lip-sync → Live Presentation`

Each stage has its own pass/fail record. Only use voice, face, and avatar assets with the subject's authorization and the provider's permitted workflow. Clearly disclose synthetic or AI-generated presentation where people could reasonably mistake it for a live human. Do not describe a generated video as live interactive Q&A.

### Stage gates

| Gate | Minimum evidence | Fail condition |
|---|---|---|
| Voice | Provider connection status, consent/authorization record, sample playback | No authorization, failed playback, or unknown source |
| Voice Q&A | Fixed test prompts, captured answers, latency/error notes | Fabricated answers or missing logs |
| Content/evidence | Sources, claim-type labels, uncertainty note | Unsupported claim presented as verified |
| Photo/face | Authorized asset reference and visual review | No consent or wrong identity/asset |
| Lip-sync | Test clip, audio/video review, timing and artifact notes | Wrong speech, major sync error, or unreviewed output |
| Live presentation | Real session ID, request/response trace, interruption/error test | Only a prerecorded clip, simulated success, or missing trace |
| End-to-end | One correlated test ID covering all stages and timestamps | Any skipped stage or missing proof |

## 5. Metrics (measure first; do not invent baselines)

Record per test: `test_id`, stage, input fixture, expected result, actual result, pass/fail, elapsed time, error, evidence link, reviewer, timestamp, and build/provider version. Report pass rate only as passed tests / executed tests, and show the denominator. Report latency as measured values (median and p95) only when the sample size is stated. Unrun tests are `NOT_RUN`, not pass.

## 6. Security and privacy

- Keep provider API keys in server-side secret storage; never place them in public HTML, source control, client bundles, logs, or demo output.
- Use least-privilege provider scopes, key rotation, rate limits, abuse controls, and audit logging.
- Minimise stored voice/face data; define retention and deletion paths before production.
- Escape untrusted content and validate provider responses. Do not allow user text to become system instructions.
- Production readiness requires a reviewed threat model, automated tests, deployment checks, and a successful real provider test. A passing workflow alone is not proof of a working public integration.

## 7. Acceptance checklist

- [ ] Schema validation added to CI.
- [ ] Unit tests cover missing evidence, conflicting sources, counterview omitted, and unsupported certainty.
- [ ] A philosophical identity statement is never relabelled as scientific verification.
- [ ] Avatar consent and synthetic-media disclosure are documented.
- [ ] Each provider stage has a real test log or is explicitly marked `NOT_RUN`.
- [ ] Public deployment is checked at the deployed URL and commit.
- [ ] Independent evaluation is described as pending until actually completed.

## 8. Limitations

This document defines a design contract, not a functioning AI model, scientific proof, provider integration, legal opinion, or production certification. No HeyGen/LiveAvatar live session or end-to-end test is claimed by this document.
