# SHIRMANI SUPREME Character Studio — Release Evidence Checklist

## Purpose
This checklist prevents a prototype from being described as a verified live avatar before the complete voice-to-presentation workflow has actually passed testing.

## Current recording inspected
- Local upload name: `Video.Guru_20261013-080950532.mp4`
- Container: MP4
- Duration: approximately 35.98 seconds
- Frame size: 888 × 1920 (portrait)
- Audio stream: present
- Review conclusion: the recording shows a voice-recording/capture workflow. It does not, by itself, prove that a voice model was accepted, an avatar was generated, lip-sync passed, or live presentation works.
- Hosting status: this uploaded file is available in the ChatGPT conversation only. It has not been uploaded into this repository, so no public repository MP4 URL is claimed here.

## Release gates
- [ ] Confirm the exact original portrait file and retain it unchanged; do not retouch or alter facial features.
- [ ] Confirm permission to use the voice and face assets.
- [ ] Store provider credentials only in the provider account or protected secrets; never commit API keys, one-time codes, recovery codes, or private access tokens.
- [ ] Record a successful authorized-voice upload and test output.
- [ ] Run representative test Q&A in Hindi and English.
- [ ] Test source-backed answers, personal/philosophical statements, and insufficient-evidence cases.
- [ ] Generate a real avatar video and review face consistency, gaze, facial movement, and lip-sync against the audio.
- [ ] Measure end-to-end latency and audio/video offset; preserve the test results.
- [ ] Test live presentation, stop/fallback behavior, and privacy-safe audit logging.
- [ ] Upload the approved demo MP4 to an appropriate repository media path or approved public host, then link the actual resulting URL from the showroom.
- [ ] Confirm the deployed GitHub Pages page and playable demo from a clean browser session.

## Evidence labels
- **INDEPENDENTLY VERIFIED** — a repeatable test passed and evidence is retained.
- **SOURCE-BASED** — a source exists, but independent confirmation is incomplete.
- **PHILOSOPHICAL / PERSONAL PERSPECTIVE** — a viewpoint or self-description, not automatically a scientific claim.
- **INSUFFICIENT EVIDENCE** — say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

## Current release status
**PROTOTYPE / NOT LIVE-VERIFIED.** The recording has been inspected, but the repository-hosted MP4 link and end-to-end provider evidence are not yet available. Do not claim completed integration, sales, revenue, or live capability without corresponding evidence.
