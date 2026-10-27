# Voice-to-Live Release Gates and Daily Production Reporting

**Status:** specification / acceptance contract. This document is not evidence that any external provider is connected or that a live test has passed.

## Purpose

Connect the existing Voice-to-Live Evidence Console and Heart-View rehearsal workflow to a reproducible release decision. Keep every critical stage independently measurable. Never infer provider health, voice identity, lip-sync quality, sales, revenue, or production output from a page view, a workflow starting, or a manually entered status.

## Required pipeline

1. **Voice source and authorization** — identify the exact original audio asset, its owner/authorization, checksum, format, and consent scope.
2. **Voice system** — retain provider job/reference, generated audio, transcript, language, pronunciation review, and failure logs. Do not expose API keys or private provider identifiers in public pages.
3. **Content and dialogue** — retain the prompt/test case, response, source references, language, and uncertainty/fallback result.
4. **Authorized portrait / character** — identify the exact user-provided image and authorization. Do not retouch or alter facial identity; layout scaling is not an identity transformation.
5. **Rendered presentation** — retain playable output, provider job, timestamp, duration, resolution, and integrity checksum where possible.
6. **Lip-sync and audio QC** — record measured method, test sample, reviewer, observed offset/drift, clipping/pronunciation findings, and pass/fail threshold. A screenshot or visual impression alone is insufficient for a timing claim.
7. **Live Q&A / end-to-end** — record a real request and response, timestamps, latency, transcript, output media, fallback/error behavior, and reviewer. Test a normal prompt, ambiguous prompt, source-required factual prompt, and insufficient-evidence prompt.
8. **Release review** — independent reviewer confirms all critical evidence references are accessible, correspond to the same test cycle, and support the declared result.

## Evidence schema

Every stage record must include:
- `stage_id`, `status` (`NOT TESTED`, `IN PROGRESS`, `BLOCKED`, `FAILED`, `VERIFIED`)
- `test_cycle_id`, `tested_at_utc`, `reviewer_role`
- `evidence_reference` and a short description of what the evidence actually proves
- `result`, `measurement`, `threshold`, and `limitations`
- `failure_reason` and next action when blocked/failed

A stage is counted as verified only when the evidence reference, cycle ID, reviewer, test result, and acceptance criteria are all present. The UI's status selection is a claim awaiting review—not independent verification. An inaccessible link, placeholder, empty field, or unrelated artifact does not pass a gate.

## Production reporting: 24/7/365

Report actual recorded events by date and UTC timestamp. Separate:
- scheduled cycles, started cycles, completed cycles, failed cycles, blocked cycles, and retried cycles;
- successful tests from successful production output;
- demo views from demos actually delivered;
- outreach drafted from messages actually sent;
- inquiries from qualified leads, proposals, orders, paid orders, refunds, and net receipts;
- gross revenue from costs, fees, and net income.

Each metric needs a defined numerator, denominator, period, data source, last-updated time, and collection status. If telemetry is not connected, label the metric **MANUAL / LOCAL RECORD** or **NOT CONNECTED**. No record is not the same as a verified zero. Never manufacture 100% quality, accuracy, cycle continuity, revenue, or customer counts.

Recommended calculations:
- stage evidence coverage = stages with accepted evidence / required stages × 100;
- cycle completion rate = completed cycles / (completed + failed cycles) × 100; report blocked and in-progress separately;
- demo-to-order conversion = paid orders / qualified demos × 100, only where the same attribution window and source are defined;
- net receipts = received payments − refunds − recorded transaction fees; costs must be shown separately before claiming profit.

## Security and privacy release gates

- Keep provider tokens, secrets, private media URLs, and customer contact lists out of public HTML, Git history, logs, and exported public reports.
- Use least-privilege credentials, server-side secret storage, authorization checks, rate limits, audit trails, and secret scanning before provider integration.
- Test access-control boundaries, upload validation, injection/XSS, unsafe URL handling, webhook signatures, replay protection, and data deletion/retention behavior.
- Store only data needed for the service. Require explicit authorization for face/voice use and disclose AI-generated presentation where relevant.
- Never bypass protected branches or repeatedly retry a prohibited direct push. Publish through a reviewed pull request and required CI.

## Release decision

- **PASS:** all critical stages pass with reproducible evidence and independent review.
- **BLOCKED:** a required external integration, asset, credential, test, or reviewer is missing.
- **FAIL:** a test ran and did not meet its stated threshold.
- **NOT TESTED:** no valid test evidence exists.

A partial pass must name the exact stages passed and remaining. The complete chain stays **NOT VERIFIED** until the real end-to-end test passes. The existing browser-local evidence register is useful for manual audit, but is not server telemetry, cross-device synchronization, or an always-on monitor.

## Execution order

1. Inspect current evidence console and current automation publisher; preserve existing working routes.
2. Resolve the protected-main publisher workflow through the reviewed PR path and inspect asset-path assumptions before accepting generated counters.
3. Run link-integrity, HTML/JS checks, mobile smoke test, and evidence-register persistence/export checks.
4. Execute the provider-side voice and avatar workflow with already-supplied authorized materials; record actual output references without asking for the same supplied recording again.
5. Run stage-by-stage QC and the end-to-end live Q&A matrix.
6. Connect production telemetry only after access controls, secret handling, and source-of-truth definitions are reviewed.
7. Publish a dated daily report and a sales report only from recorded events; clearly identify missing integrations and manual entries.
