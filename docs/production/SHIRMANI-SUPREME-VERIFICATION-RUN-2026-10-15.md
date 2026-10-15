# SHIRMANI SUPREME — Verification Run Record
**Run date:** 2026-10-15  
**Project:** SRI-PRES-001 · Voice-to-Presentation Studio  
**Existing showroom:** `showroom/shirmani-supreme-character-studio.html`  
**Run type:** Continuation of existing work; not a fresh implementation  
**Overall release state:** BLOCKED / NOT VERIFIED

## 1. Existing artifacts retained
- Existing showroom and its character charter remain the project baseline.
- Existing approved character specification, release checklist, and prior reference recording are treated as existing project materials.
- Do not replace the approved identity/character brief with a new generic brief.
- Do not request the already-provided reference recording again.

## 2. Reference recording technical inspection
- Local filename: `Video.Guru_20261013-080950532.mp4`
- Container: MP4 / ISO base media
- Duration: 35.982993 seconds
- File size: 52,076,438 bytes
- Video stream: H.264, 888 × 1920
- Audio stream: AAC, 44,100 Hz, 2 channels

These are media-container facts only. They do not prove that the video is an exported HeyGen avatar, that the portrait is the exact original photo, that the voice is authorized, or that lip-sync/live integration works. The MP4 is not committed as a binary asset by this record.

## 3. Acceptance gate results

| Gate | Result | Evidence / blocker |
|---|---|---|
| Existing showroom located | PASS | Existing HTML source fetched from repository |
| Existing character specification retained | PASS | Existing production specification files are present |
| Reference MP4 technical metadata read | PASS | ffprobe reports the metadata in section 2 |
| Original portrait identity / file hash matched | BLOCKED | Original standalone portrait and reference hash not established |
| Authorized voice asset / authorization record | BLOCKED | Standalone audio asset and provider-side authorization evidence not established |
| Provider project/API integration | NOT VERIFIED | No provider response, project ID, or successful authenticated request recorded |
| Speech recognition / test Q&A | NOT RUN | No reproducible run output supplied |
| Generated avatar video / facial movement | NOT VERIFIED | No confirmed generated output artifact identified |
| Lip-sync quality and audio/video offset | NOT RUN | Requires a known voice sample and generated output for measurement |
| End-to-end latency | NOT RUN | No timestamped end-to-end run |
| Live broadcast | NOT VERIFIED | No live session evidence |
| Production release | BLOCKED | Critical gates above remain incomplete |

## 4. Next execution sequence — continue from this point
1. Inspect the existing recording and identify whether it contains a provider-generated result or only a setup/reference screen; do not infer from filename alone.
2. Locate the standalone original portrait and authorized voice asset among already available project/session assets. Match files by SHA-256 and record provenance; preserve the portrait unchanged.
3. If either asset cannot be located, request only that missing item once. Do not ask for the existing MP4 again.
4. Verify provider connection through a real authenticated test. Never put API keys or access tokens in this repository, logs, screenshots, or chat.
5. Run a 20-prompt Q&A set covering simple Hindi, English, ambiguous questions, respectful disagreement, multilingual input, and insufficient-evidence handling. Save prompts, outputs, evidence labels, and pass/fail decisions.
6. Generate a short test presentation from the authorized portrait and voice. Retain the actual output artifact and provider job/reference ID, with secrets removed.
7. Measure lip-sync against the audio, inspect face/gaze/expression consistency, and record audio/video offset plus end-to-end latency. State the measurement method and sample size.
8. Run the complete regression checklist. Production stays BLOCKED if any critical gate fails or lacks evidence.

## 5. Evidence record format
For each test record: test ID, timestamp (UTC), input asset SHA-256, provider/model/version, prompt or stimulus, expected behavior, observed result, measured timing, evidence URI or artifact path, reviewer, and PASS/FAIL/BLOCKED. Do not log credentials or unnecessary personal data.

## 6. Reporting rule
Use only these statuses:
- **VERIFIED** — reproducible test evidence supports the claim.
- **SOURCE-BASED** — a source exists but independent verification is incomplete.
- **PHILOSOPHICAL / IDENTITY** — an authored belief or identity statement, not a scientific result.
- **INSUFFICIENT EVIDENCE** — required evidence is absent.

Never mark a workflow, checkbox, repository commit, or media metadata inspection as proof of a working live avatar. No sales, revenue, provider integration, or production-readiness claims are made by this record.
