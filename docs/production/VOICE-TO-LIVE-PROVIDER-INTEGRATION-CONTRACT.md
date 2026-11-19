# Voice-to-Live provider integration contract

**Status:** implementation contract; not a claim that a provider is connected.
**Reference supplied by the owner:** https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7
**Related UI:** `showroom/voice-to-live-evidence-console.html` and `heart-view-preview.html`

## Goal

Connect the existing evidence workflow to a real provider adapter without conflating a saved reference URL, a browser-local evidence record, a successful API response, and a fully verified live presentation.

## Required stages and evidence

| Stage | Required machine evidence | Independent acceptance check |
|---|---|---|
| 1. Voice source & authorization | source asset ID/hash, consent/authorization record reference, allowed purpose and timestamp | confirm asset identity and permitted use; never infer consent from a URL |
| 2. Voice system | provider request/job ID, request time, response status, output asset ID, transcript/language metadata when available | play the returned audio; review intelligibility, pronunciation, clipping and identity claims |
| 3. Content/dialogue | immutable script or prompt version, test-case ID, language, source references, moderation/result metadata | run a fixed set of ordinary, ambiguous, adversarial and fallback questions |
| 4. Portrait/avatar | provider asset ID and selected avatar ID, with authorized asset reference | compare the generated character with the approved source; record deviations |
| 5. Rendered video | provider job ID, final output URL/asset ID, duration, dimensions, codec where available, completion timestamp | download or open the actual final output and play it from beginning to end |
| 6. Lip-sync/audio QC | reviewer, test-cycle ID, time-coded observations, sync score and scoring method | check several speech segments, pauses, plosives, names, facial motion, audio/video drift and captions |
| 7. Live Q&A / end-to-end | session ID, request/response timestamps, latency samples, errors, fallback events and trace/correlation ID | ask a real question through the deployed path and verify the response reaches the real presentation |
| 8. Independent release review | evidence references for stages 1–7, reviewer sign-off, known limitations and decision | reject release if any required stage is failed, missing, expired or unreviewed |

A provider's successful job state proves only that provider operation. It does not, by itself, prove voice fidelity, lip-sync quality, correct dialogue, live Q&A, or public deployment.

## Adapter boundary

Implement provider-specific calls behind a server-side adapter. The browser UI must never receive provider API secrets.

Suggested adapter operations:

- `validateConfiguration()`: report configured/missing capability names only; never return secret values.
- `createVoiceJob(input)`
- `createRenderJob(input)`
- `getJobStatus(providerJobId)`
- `getOutputMetadata(providerJobId)`
- `verifyWebhook(rawBody, signatureHeaders)`
- `recordEvidence(event)`

Use typed, versioned events. Every event should include `schemaVersion`, `provider`, `stageId`, `testCycleId`, `correlationId`, `occurredAt`, `result`, and a safe evidence reference. Include `providerJobId` when one exists. Do not log secrets, full private prompts, private audio, or raw authorization documents.

## Status model and counters

Use only these stage states:

- `NOT TESTED`: no test has been run.
- `IN PROGRESS`: a test is running or evidence is being collected.
- `BLOCKED`: configuration, permission, quota, or dependency prevents the test.
- `FAILED`: a test ran and did not meet its acceptance criteria.
- `VERIFIED`: all stage-specific acceptance checks passed and a reviewer plus evidence reference are recorded.

Publish separate counters, never one misleading blended score:

1. **Workflow evidence coverage** = stages with required evidence ÷ 8 × 100.
2. **Verified-stage rate** = stages accepted as VERIFIED ÷ 8 × 100.
3. **Test pass rate** = passed test cases ÷ executed test cases × 100; show the sample count.
4. **Provider availability** = successful provider requests ÷ eligible provider requests over a named window; report the window and denominator.
5. **Lip-sync metric** = show the actual scoring method, evaluated segments and reviewer; do not fabricate a percentage when no valid measurement exists.
6. **Commercial metrics**: enquiries, quotes, paid orders and collected revenue must remain separate; a demo or quote is not a sale.

No data means **NOT MEASURED**, not 0% quality and not 100% success. A manually entered URL must not be treated as provider telemetry.

## Security and reliability requirements

- Store provider credentials only in the deployment's secret manager/environment configuration. Never commit credentials or put them in browser JavaScript.
- Verify webhook signatures against the raw request body; reject invalid signatures and replayed event IDs.
- Apply authentication, authorization, rate limits, request-size limits and audit logging to job-creation endpoints.
- Use idempotency keys and bounded retries. Do not automatically create duplicate render jobs after an ambiguous timeout; reconcile provider job status first.
- Restrict output URLs and asset access; do not expose private media through public logs or unauthenticated endpoints.
- Add timeouts, circuit-breaker/backoff behavior, quota/error visibility, and a manual recovery path.
- Keep the existing manual evidence console available as a register, clearly labelled as manual/local unless server persistence is actually connected.
- Require an explicit human release decision; failed or missing evidence must not be silently promoted to VERIFIED.

## Minimum acceptance test plan

1. Missing credentials produce a safe `BLOCKED` result with no secret leakage.
2. Valid credentials can create a provider job in a non-production/test configuration.
3. Provider success and provider failure are both captured with correlation IDs.
4. Invalid webhook signatures are rejected; valid webhook events are idempotent.
5. Repeated requests with the same idempotency key do not create duplicate jobs.
6. An ambiguous timeout triggers reconciliation, not an unconditional second job.
7. The actual output asset can be retrieved and independently played/reviewed.
8. Voice, content, portrait, render, lip-sync and live Q&A each receive separate evidence.
9. Exported audit reports contain status, evidence references, timestamps and reviewer details but no secrets or private media.
10. A full test run produces a report that clearly separates passed, failed, blocked and not-tested cases.

## Implementation sequence

1. Inspect the current runtime, deployment target and existing secret-management conventions.
2. Select the provider API capabilities actually available to this account; do not assume that the supplied video URL grants API access.
3. Implement the server-side adapter and unit tests with mocked provider responses.
4. Add a non-production integration test and persist server-side evidence.
5. Connect the evidence console to the server read API while retaining an explicit manual mode.
6. Run the full acceptance suite and capture real provider job/output references.
7. Enable live presentation only after independent release review.

## Current evidence boundary

The owner-provided HeyGen URL is a reference link. This contract does not establish that the provider API is configured, that a final video/audio asset exists, that lip-sync has passed, that live Q&A works, or that the public site is deployed with these capabilities. Those claims require actual test-cycle IDs and inspectable evidence.
