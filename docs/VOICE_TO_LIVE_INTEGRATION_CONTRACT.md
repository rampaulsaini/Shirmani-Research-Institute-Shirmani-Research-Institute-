# Voice-to-Live Integration Contract
## Shirmani Research Institute — implementation and acceptance plan

**Purpose:** turn the existing Voice-to-Live Evidence Console into a verifiable integration workflow without claiming that a local register is connected to a provider.

**Existing reference:** [HeyGen video](https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7)  
**Current evidence console:** [showroom/voice-to-live-evidence-console.html](../showroom/voice-to-live-evidence-console.html)

## 1. End-to-end chain

`Authorized voice source → Voice system → Content/dialogue → Authorized portrait/avatar → Render job → Rendered video/audio → Lip-sync/audio QC → Live Q&A → Independent release review`

Each stage has its own status and evidence. A downstream stage must not be marked verified merely because an upstream stage passed. A provider link or job ID alone is not proof of playback, voice identity, lip-sync quality, or live conversation.

## 2. Truthful status vocabulary

- **NOT TESTED** — no recorded execution evidence.
- **IN PROGRESS** — a test has started but its acceptance checks are incomplete.
- **BLOCKED** — a dependency, credential, permission, provider capability, or environment prevents execution; record the reason.
- **FAILED** — a check ran and did not meet its acceptance criteria.
- **VERIFIED** — required evidence, test-cycle ID, reviewer, timestamp, and all stage-specific checks are present and independently reviewable.

Do not convert missing evidence into a pass. Percentages in the console mean *evidence-gate coverage only*, not truth, intelligence, quality, or successful production uptime.

## 3. Stage contracts and acceptance criteria

| Stage | Required input | Acceptance evidence |
|---|---|---|
| 1. Voice source & authorization | User-authorized voice asset and documented permitted use | Asset reference/hash, consent/authorization record, source owner, reviewer |
| 2. Voice system | Approved voice asset, provider configuration | Provider/job reference, generated sample, transcript, pronunciation checklist, human voice-match review |
| 3. Content/dialogue | Approved script, questions, source material | Versioned content ID, language, factual/source review, uncertainty and refusal tests |
| 4. Portrait/avatar | User-authorized portrait/avatar asset | Asset reference, permission record, selected avatar ID, visual fidelity review |
| 5. Render | Approved content + voice + avatar | Provider job ID, terminal job status, media URL or controlled artifact reference, duration/resolution, full playback check |
| 6. Lip-sync/audio QC | Final rendered media | Timestamped reviewer checklist, audio/video alignment observations, clipping/noise/pronunciation results, defect list |
| 7. Live Q&A / full chain | Deployed session endpoint and approved knowledge source | Actual session ID, at least one recorded question and response, measured response latency, transcript, error/fallback behavior, session review |
| 8. Independent release review | Evidence from all prior stages | Reviewer sign-off, unresolved-risk list, release decision, test-cycle ID |

A percentage score must be calculated only from defined, repeatable checks. For example, lip-sync quality should use a documented sampling protocol and reviewer rubric; do not invent a numeric score when no measurement was taken.

## 4. Provider adapter boundary

Implement provider integrations behind a server-side adapter, not in public browser JavaScript.

Suggested internal operations:
- `createVoiceJob(input, idempotencyKey)`
- `getVoiceJob(jobId)`
- `createRenderJob(input, idempotencyKey)`
- `getRenderJob(jobId)`
- `getAuthorizedMedia(mediaId)`
- `openLiveSession(config)`
- `closeLiveSession(sessionId)`

These are **proposed internal interfaces**, not claims about HeyGen's actual API names. Map them to the provider's current documented API only after checking account permissions, supported features, and current terms. Keep API keys in server-side environment secrets. Never commit secrets or expose provider tokens to the browser. If no supported API entitlement exists, use the provider UI and manually record evidence rather than pretending the adapter is connected.

## 5. Evidence event schema

Each recorded event should include:
- `schemaVersion`
- `runId` and `stageId`
- `status`
- `startedAt` and `finishedAt` (UTC ISO 8601)
- `inputArtifactRefs` and `outputArtifactRefs`
- `providerName`, `providerJobId` (when applicable)
- `checks[]` with check ID, result, measured value/unit where applicable, and evidence reference
- `reviewer`, `reviewedAt`, `notes`
- `errorCode` and safe diagnostic text when blocked or failed

Use immutable run IDs and idempotency keys to prevent duplicate submissions. Do not store raw credentials, private voice data, or unnecessary personal data in the evidence log. Apply least-privilege access, retention limits, and explicit authorization for media use.

## 6. Production counters (definitions)

- **Run count:** distinct persisted `runId` values, not page refreshes.
- **Completed runs:** runs where every required stage passed.
- **Evidence coverage:** completed evidence requirements divided by all applicable requirements.
- **Failure rate:** failed executed checks divided by all executed checks; exclude NOT TESTED and report the denominator.
- **Availability:** measured from monitored probes over a stated time window; never infer 24/7 uptime from a local page.
- **Latency:** measured timestamps from actual requests; show sample count and percentile (p50/p95) when enough samples exist.
- **Quality score:** only show where a documented rubric, sample size, and reviewer/evaluation method are disclosed.

The existing browser-local console is a manual register. Its values must not be labelled as live provider telemetry, centralized monitoring, or production uptime.

## 7. Required test sequence before launch

1. **Unit tests:** status transitions, schema validation, missing evidence, duplicate run IDs, and percentage denominators.
2. **Adapter contract tests:** success, timeout, provider error, invalid credentials, rate limit, and retry/idempotency behavior using mocks.
3. **Authorized sandbox test:** one voice generation and one render with the approved assets; preserve job references and output artifacts.
4. **Media QC:** human review of full playback, pronunciation, audio integrity, avatar/portrait fidelity, and lip-sync.
5. **Live Q&A test:** multiple known questions, an unknown question, a source-conflict question, interruption/timeout, and graceful fallback. Record actual latency and transcript.
6. **End-to-end test:** follow one `runId` from source authorization through release review and verify that every stage references the same run.
7. **Security review:** secret scanning, authorization checks, upload validation, rate limits, audit-log privacy, and dependency review.
8. **Release gate:** independent reviewer approves only when all mandatory checks pass and no critical blocker remains.

## 8. Current state and honest boundary

The repository contains a browser-local evidence console and the supplied HeyGen reference link. The presence of those assets does **not** establish a successful provider API call, actual voice match, rendered-media playback, lip-sync pass, live Q&A, or complete end-to-end run. Those checks remain unverified until real execution evidence is attached.

## 9. Next implementation order

1. Keep the existing console as the evidence UI; add a versioned evidence API and persistent database.
2. Add authentication/authorization and server-side secret management.
3. Implement one provider adapter using the provider's current documented API and the account's actual permissions.
4. Persist provider callbacks/polling results and artifact references; make retries idempotent.
5. Add automated tests and an operator dashboard with clear denominators and timestamps.
6. Run the authorized end-to-end test and attach evidence before changing any stage to VERIFIED.

This document is an implementation contract, not a claim that the above integrations or tests have already been completed.
