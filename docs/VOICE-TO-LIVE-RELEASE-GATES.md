# Voice-to-Live: Release Gates and Evidence Checklist

**Purpose:** give the existing Voice-to-Live Evidence Console a concrete, repeatable release decision. This document does not claim any provider integration or media stage has passed.

- Operator console: [Voice-to-Live Evidence Console](../showroom/voice-to-live-evidence-console.html)
- Existing owner-provided HeyGen reference: https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7

## Release rule

A stage is **VERIFIED** only when a reviewer has inspected the actual artifact or a trusted provider/API response, recorded the evidence reference, timestamp, test-cycle ID, and result, and can repeat the check. A typed URL, screenshot of a settings page, locally calculated percentage, or a saved form is not by itself proof that a service ran successfully.

Keep these states distinct:

- **NOT TESTED** — no qualifying test evidence yet.
- **IN PROGRESS** — test started; required evidence incomplete.
- **PASS** — all acceptance checks for this stage passed and evidence is attached.
- **FAIL** — test ran and one or more acceptance checks failed.
- **BLOCKED** — a dependency, permission, credential, provider access, or safety requirement prevents a valid test.

Never convert NOT TESTED or BLOCKED to PASS to improve a dashboard percentage.

## Stage-by-stage acceptance

| # | Stage | Required evidence | Acceptance checks |
|---|---|---|---|
| 1 | Voice source & permission | Original audio asset reference, source/owner authorization, checksum where feasible | Correct authorized asset; permitted use and retention documented |
| 2 | Voice system / generation | Provider job ID or reproducible local test ID, generated audio artifact, transcript | Audio actually plays; transcript and language match the approved input; errors recorded |
| 3 | Content & dialogue | Versioned prompt/script, language, safety review, expected-answer test set | No fabricated claims; intended language and meaning retained; unsafe or unsupported answers handled |
| 4 | Authorized photo/avatar | Asset reference and permission record; avatar/provider job ID | Correct approved identity asset; no substitute image silently used |
| 5 | Rendered video | Actual output video URL/file, render/job ID, duration and timestamp | Video opens and plays end-to-end; audio track exists where expected |
| 6 | Lip-sync / media QC | Output artifact plus reviewer checklist or measurable sync report | Sampled speech aligns with mouth movement; no missing audio, severe drift, or obvious render corruption |
| 7 | Live presentation & Q&A | Live session ID/URL, test questions, transcript, response timestamps | A real session accepts a question and returns a response; disconnect/error paths are tested |
| 8 | Independent release review | Reviewer identity/role, test-cycle ID, linked evidence for stages 1–7 | Reviewer who did not produce the artifacts checks them; all release-blocking failures closed |

## Required record fields

For every stage and every cycle, record:

- cycle_id — unique identifier shared across all stages in one end-to-end attempt.
- stage_id and status — one of the states defined above.
- started_at / completed_at — ISO-8601 timestamps with timezone.
- artifact_ref — actual output file, provider job, trusted log, or test report.
- provider and provider_job_id — only when applicable and observed.
- expected_result, observed_result, failure_reason.
- reviewer and reviewed_at for any PASS / release decision.

Avoid placing API keys, passwords, private tokens, or unnecessary personal data in logs or exported reports.

## Metrics that are safe to publish

- **Evidence coverage** = stages with qualifying evidence ÷ 8 × 100.
- **Stage pass rate** = passed completed stage checks ÷ all completed stage checks × 100. Show the denominator.
- **End-to-end pass rate** = complete cycles passing all eight gates ÷ all complete cycles run × 100. Show sample size and date window.
- **Blocked count**, **failed count**, **latest successful end-to-end cycle**, and **last checked time**.
- **Automation cycle count** must come from actual runner/workflow records, not a manually incremented browser counter.

A percentage is not a quality guarantee. Do not label local-only or manually entered data as live, global, synchronized, 24/7, or provider-verified.

## Safe test sequence

1. Confirm permission and asset identity before generating media.
2. Run a small non-public test; save the exact input version and output artifacts.
3. Verify each stage independently before testing the full chain.
4. Run at least one end-to-end cycle with a fixed cycle_id; retain failed evidence as well as successful evidence.
5. Have a separate reviewer check the artifacts and provider events.
6. Publish only after all required gates pass. If any stage is NOT TESTED, FAIL, or BLOCKED, show the release as **NOT VERIFIED** and state the specific blocker.

## Current status at document creation

This checklist is a specification, not a test result. The existing browser console is a local evidence register and does not itself establish that HeyGen, voice generation, lip-sync, live Q&A, server synchronization, or 24/7 monitoring is connected. The provided HeyGen URL is retained as a reference, not treated as proof of a successful end-to-end run.

## Next engineering dependencies

- A server-side provider adapter with credentials stored only in protected secrets.
- Authenticated event ingestion for provider job states and artifact URLs.
- Durable server-side storage with access controls and audit history.
- Automated integration tests using authorized test assets.
- A separate release reviewer and a real scheduled runner whose logs feed production counters.
- User-facing privacy, consent, retention, and deletion controls before public account rollout.
