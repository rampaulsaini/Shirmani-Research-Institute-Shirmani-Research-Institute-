# Voice-to-Live End-to-End Test Plan

**Purpose:** verify the existing Voice → Voice System → Content/Dialogue → Authorized Avatar/Photo → Rendered Video → Lip-sync/Audio QC → Live Q&A → Release chain without confusing a reference link, mock-up, manually entered score, or browser-local record with a successful external integration.

## Current evidence baseline

- Existing HeyGen reference (provided by the owner): https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7
- The reference is a starting point only. Its presence does not prove the current provider job status, downloadable media, voice provenance, lip-sync quality, live Q&A, or end-to-end execution.
- The evidence console is a browser-local register. Unless a separate provider/API test is implemented and executed, its records are not provider telemetry, cross-device sync, or independent verification.
- Do not request the supplied reference again. Reuse it as the reference URL; record any missing artifact as a gap rather than inventing one.

## Required test cases

| ID | Stage | Procedure | Required evidence | Pass condition |
|---|---|---|---|---|
| VTL-01 | Voice source | Identify the authorized voice asset/source and permitted use. | Source/asset reference, permission basis, reviewer and date. Do not expose private credentials. | Source and use authorization are reviewable. |
| VTL-02 | Voice system | Submit a fixed short script and capture the actual generated/processed audio. | Input script hash or ID, provider/job ID where applicable, audio artifact, measured duration and reviewer. | Audio artifact exists and is intelligible; no unsupported source attribution. |
| VTL-03 | Content/dialogue | Run a fixed multilingual prompt set including normal, ambiguous and refusal/safety cases. | Versioned prompts, actual outputs/transcript, expected behavior and scored rubric. | Results are recorded against the same test set; errors are disclosed. |
| VTL-04 | Avatar/photo authorization | Verify the exact authorized avatar/photo asset used in the render. | Asset reference, authorization record and reviewer/date. | The rendered asset matches the authorized source and intended use. |
| VTL-05 | Rendered video | Trigger the real render and open the actual output artifact. | Provider job ID/status, actual video URL or artifact, render timestamp and playback result. | Actual output plays; a storyboard, screenshot, or reference URL alone does not pass. |
| VTL-06 | Lip-sync/audio QC | Review a defined sample at the beginning, middle and end; check pronunciation, clipping, audio-video alignment and captions/transcript. | Test clip/timecodes, rubric, measured score, findings, reviewer/date. | Criteria and thresholds are declared before review and all required checks pass. |
| VTL-07 | Live Q&A | Ask a fixed set of questions in the live interface and record the real responses. | Session/test ID, timestamp, prompts and responses, latency measurements, failures/fallbacks. Redact personal data. | Actual two-way interaction works; prerecorded video alone does not pass. |
| VTL-08 | End-to-end run | Run one uniquely identified test from source input through live presentation. | Shared cycle ID, links to every stage artifact, event timestamps, error log and final reviewer. | Every required stage maps to the same cycle and each stage independently passes. |
| VTL-09 | Release check | Test public route on mobile and desktop; verify accessibility, privacy notices and failure states. | Browser/device details, screenshots or test logs, reviewer and release commit. | No critical defect; unimplemented provider integrations remain clearly labelled. |

## Measurement rules

- **Evidence coverage** = stages passing the defined evidence gate ÷ total required stages × 100.
- **Quality (%)** must use a documented rubric and sample; **accuracy (%)** must use a declared test set and scoring rule. They are not universal measures of truth or intelligence.
- **Latency (ms)** is measured from timestamped events for a specified operation. State whether it is client-observed or provider-reported.
- **Error count** counts observed errors within the named test cycle and scope.
- **Cycle count** counts unique recorded test-cycle IDs; it is not a claim of 24/7 uptime or total platform automission.
- Do not substitute planned, estimated, missing, or manually typed values for measured results. Keep unknown values blank/NOT TESTED.
- A stage can be marked VERIFIED only after the actual artifact and test record have been reviewed. The evidence console's fields are an audit aid, not an independent verification engine.

## Execution record template

For every run, record:

- Test cycle ID:
- Repository commit / app version:
- Stage and operation:
- Test set / rubric version:
- Start and end timestamps, timezone:
- Actual artifact / provider job reference:
- Measured quality (%), accuracy (%), latency (ms), error count:
- Observed failures and limitations:
- Reviewer and review date:
- Status: NOT TESTED / IN PROGRESS / BLOCKED / FAILED / VERIFIED

## Release blockers

Do not claim production-ready or end-to-end complete while any required stage is NOT TESTED, while a live provider artifact is missing, or while the live Q&A test has not actually run. Provider credentials must be stored in approved secret storage, never in public HTML, repository files, screenshots, or exported reports. Use least-privilege scopes, redact personal data, and do not automate bulk outreach or purchases without review and authorization.
