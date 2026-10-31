# Voice-to-Live: measurable acceptance gates

**Project:** Shirmani Research Institute / शिरोमणि स्वरूप दृष्टिकोण  
**Protocol version:** 1.0  
**Status at authoring:** Acceptance protocol proposed; provider-backed end-to-end execution is not yet evidenced by this document.

## Purpose

Make each production stage independently testable. A workflow run, generated file, dashboard counter, preview, or successful build is not proof that external media services work or that a sale occurred.

## Required chain

1. **Authorized source assets** — record the owner-authorized photo/audio source reference, permission status, checksum where feasible, and date. Use the already supplied HeyGen reference as a reference; do not request the same photo/video again. A reference URL alone does not prove the media has been retrieved or tested.
2. **Voice system** — record provider, job/request ID, input text, output audio artifact URL or checksum, duration, language, result, and timestamp. If no provider output artifact exists, status remains NOT TESTED.
3. **Content and dialogue** — record the exact prompt/test question, expected response criteria, actual response, source/evidence references, safety review, and reviewer. Separate factual claims from philosophical or personal statements.
4. **Avatar / rendered media** — record provider job ID, selected authorized avatar/source reference, rendered video and audio artifact references, duration, resolution, and playback check.
5. **Voice identity and lip-sync QA** — review the rendered audio and video together. Record reviewer, test method, timestamp offset or synchronization defect, intelligibility result, identity/authorization check, and pass/fail. Do not mark pass from a still image or a provider job's “completed” state alone.
6. **Live presentation and Q&A** — record the session/job ID, connection state, a timestamped question and response, audio playback, latency, disconnect/recovery behavior, and human reviewer. A recorded video is not live Q&A evidence.
7. **End-to-end release** — run one traceable test from authorized input through final presentation. Store a single run ID linking all stage artifacts, a failure report, and the reviewer decision.

## Evidence status vocabulary

- **VERIFIED** — required artifact exists, is inspectable, and passed the stage's written checks.
- **FAILED** — a check ran and failed; retain the failure evidence.
- **BLOCKED** — a required credential, permission, dependency, or artifact is unavailable.
- **NOT TESTED** — no qualifying test evidence exists.
- **SOURCE-BASED** — a source or external reference is recorded but has not been independently checked.

Never convert missing evidence into a pass. Never count planned cycles as completed cycles.

## Counter definitions

- **Cycles attempted** = unique run IDs started.
- **Cycles completed** = unique runs that reached the final stage (pass or fail).
- **Stage pass rate** = passed stage checks / executed stage checks × 100. Show “N/A” if no checks executed.
- **Evidence coverage** = required stage records with inspectable evidence / required stage records × 100.
- **End-to-end pass rate** = end-to-end runs passing all required gates / end-to-end runs completed × 100. Show “N/A” when the denominator is zero.
- **Provider integration coverage** = configured and authenticated provider integrations with a successful smoke test / integrations required for the selected release × 100.
- **Commercial counters** — enquiries, quotes sent, paid orders, refunds, and net revenue must be sourced from their actual records. Builds, views, clicks, workflow runs, and generated catalog entries are not sales.

Always show numerator, denominator, measurement window, last-updated time, and evidence link next to every percentage. A percentage is a measurement of the stated check only—not a universal measure of truth, intelligence, love, or personal worth.

## Release acceptance checklist

- [ ] Owner authorization and asset provenance recorded.
- [ ] Voice output artifact can be opened and played.
- [ ] Dialogue test has a reproducible input and reviewed output.
- [ ] Rendered video and audio artifacts can be opened and played.
- [ ] Voice identity/authorization and lip-sync checks have named evidence and a reviewer.
- [ ] Live Q&A is tested in a live session, not inferred from a recording.
- [ ] One run ID links every stage from input to final presentation.
- [ ] Failed and blocked tests remain visible; no silent pass defaults.
- [ ] Public dashboard labels local/manual counters separately from provider telemetry.
- [ ] Release page has been smoke-tested after publication.
- [ ] No claim of revenue, full automation, or end-to-end success without corresponding evidence.

## Existing reference

User-provided HeyGen reference: https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7

This is a reference supplied for the project, not independent proof of current voice output, lip-sync, live Q&A, or the complete end-to-end chain.

## Current evidence boundary

The evidence console is a browser-local register unless and until a verified backend/provider integration is implemented. Local entries and counters do not automatically receive HeyGen telemetry. Do not claim 24/7/365 execution unless scheduled runs, their logs, artifact retention, alerting, and uptime are actually available and checked.
