# Voice-to-Live Production Acceptance Contract

**Project:** Shirmani Research Institute / शिरोमणि स्वरूप दृष्टिकोण  
**Purpose:** Make the requested chain inspectable and measurable without presenting planned work as completed work.  
**Existing reference:** https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7  
**Evidence UI:** showroom/voice-to-live-evidence-console.html

## Required end-to-end chain

Authorized voice source → Voice system → Content/dialogue → Authorized portrait/avatar → Rendered video → Lip-sync/audio QC → Live Q&A → Release review

A URL, UI control, locally entered status, or generated report is not by itself proof that an external provider executed a job.

## Acceptance gates (each gate has its own evidence)

| Gate | Required evidence | Pass condition |
|---|---|---|
| 1. Source & permission | Source asset/reference, authorization record, owner and date | Asset is authorized for this exact use |
| 2. Voice system | Actual output audio, transcript, provider/job reference and test notes | Output plays; language/pronunciation checks recorded |
| 3. Content/dialogue | Versioned prompt/script, representative questions, expected answer policy | Content reviewed for accuracy, clarity, safety and uncertainty handling |
| 4. Portrait/avatar | Existing authorized portrait/avatar reference and provider asset/job ID | Correct authorized character is used; no new user upload is assumed necessary |
| 5. Render | Actual playable media URL/file, job ID, duration/resolution and render timestamp | Entire output plays and metadata is recorded |
| 6. Lip-sync/audio QC | Timestamped reviewer checklist, sync observations/measurements, audio defects and outcome | Reviewer records pass/fail against a stated threshold; no unsupported quality percentage |
| 7. Live Q&A | Real session/job reference, test questions, answers, latency, failures/fallback and timestamp | A live session actually completes; simulated/static UI does not pass |
| 8. Release review | All prior gate IDs, reviewer identity, known limitations and release decision | Independent reviewer signs off; blocked/failed gates prevent a verified end-to-end claim |

## Counter definitions

- **Verified gates:** number of gates with evidence reference + cycle ID + reviewer + VERIFIED status, divided by 8.
- **Evidence coverage:** verified gates / 8 × 100. This measures register completeness, not universal truth or subjective worth.
- **Recorded test cycles:** count of distinct cycle IDs with at least one saved stage record. A cycle ID is not proof of an automated run.
- **Failed checks:** count of stages explicitly marked FAILED.
- **Daily production count:** count only server/CI/provider event records with timestamp, unique run ID and outcome. Browser-local edits are not a production event.
- **24/7 automation status:** NOT CONNECTED until a real scheduler/worker, durable server-side event store, monitoring, alerting and recovery path are deployed and tested.
- **External-provider status:** NOT VERIFIED until the provider response/job and resulting media/session are independently inspected.

Never fill unknown values with fabricated percentages. Show N/A, NOT TESTED, or BLOCKED where appropriate.

## Operational separation

1. **Presentation layer:** public homepage and evidence-console link.
2. **Workflow layer:** explicit stages, cycle IDs and acceptance criteria.
3. **Execution layer:** real provider/API calls or human-run tests; not implied by the presentation layer.
4. **Evidence layer:** durable, timestamped records with artifact references and reviewer.
5. **Monitoring layer:** scheduled checks, failure alerts, retry limits, audit logs and recovery procedures.
6. **Release layer:** independent quality/security review before public claims.

The existing console is browser-local and manual. It does not currently provide provider telemetry, multi-device sync, durable server storage, authentication, background scheduling or true 24/7 monitoring. These must be implemented and tested separately before they are advertised as available.

## Security and privacy requirements

- Keep provider API keys and secrets server-side; never put secrets in public HTML, client JavaScript, repository commits or downloadable reports.
- Use least-privilege credentials, secret rotation, rate limits, input validation and auditable access.
- Record consent and allowed uses for voice/portrait assets; restrict access to evidence containing personal media.
- Do not send bulk outreach or claim that emails/WhatsApp messages were sent unless an authorized integration reports success.
- Keep a human approval gate for external publishing, sales outreach, payments and destructive actions.
- Retain only necessary logs and provide a documented deletion/retention policy.

## Release checklist

- [ ] Homepage links directly to the evidence console.
- [ ] Each stage has a named test cycle and reviewer.
- [ ] Actual media artifacts are playable and referenced.
- [ ] Voice, content, portrait, render, lip-sync and live Q&A have separate results.
- [ ] Independent end-to-end run completes without silently skipping failed stages.
- [ ] Metrics are sourced from real records and label their scope/time window.
- [ ] Provider integration, server persistence, scheduler, alerts and access controls are tested before claiming 24/7 automation.
- [ ] Public status distinguishes planned, implemented, tested, verified and blocked.

## Current known status at document creation

The existing browser-local evidence register and supplied HeyGen reference are available. This alone does not prove a successful current provider render, exact voice match, lip-sync pass, live Q&A, production scheduler, or complete end-to-end run. Record those outcomes only after the corresponding tests are actually executed.
