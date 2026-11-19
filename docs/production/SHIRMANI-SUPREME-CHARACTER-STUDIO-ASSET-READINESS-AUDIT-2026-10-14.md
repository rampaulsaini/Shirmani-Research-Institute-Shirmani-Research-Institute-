# SHIRMANI SUPREME Character Studio — Asset Readiness Audit

**Audit date:** 2026-10-14  
**Scope:** repository default-branch inventory, Character Studio page, authorized-voice configuration, four related PRs, and the user-provided MP4 attachment.  
**Status:** SOURCE-BASED AUDIT — external provider integration and original-asset matching are NOT VERIFIED.

## Findings

### Character Studio
- Existing page: `showroom/shirmani-supreme-character-studio.html`.
- The page explicitly describes itself as an evidence-gated browser prototype, not a live avatar.
- It says the external provider is not connected/verified and the local response workbench does not call an AI model/API.
- It has acceptance gates for authorized assets, Q&A, evidence, facial movement, gaze, lip-sync, timing, and audit records.

### User-provided MP4
- Local attachment inspected: `Video.Guru_20261013-080950532.mp4`.
- Container metadata: MP4, H.264 video, 888×1920 portrait, AAC audio, 44.1 kHz stereo, duration 35.983 seconds, file size 52,076,438 bytes.
- Sampled frames show a face and on-screen recording instructions referencing HeyGen voice capture. This establishes that the attachment is a recording of a capture workflow; it does **not** prove that HeyGen accepted the recording, created an avatar, or completed any voice/lip-sync test.
- The MP4 is an attachment in the current ChatGPT conversation. It was **not found in the repository's tracked file tree**, so no repository MP4 URL can truthfully be supplied yet.

### Photo and voice assets
- `assets/shirmani-perspective-logo.svg` contains an embedded raster image in an SVG presentation logo. This is not the same as verifying a separate, unaltered original portrait file.
- `css/assets/images/profile.jpg` appears in the repository tree with a reported size of **1 byte**; it must not be treated as a usable portrait.
- `config/authorized-voice-integration.json` declares photo/audio SHA-256 values and a 176.485-second mono, 48 kHz audio asset. However, the tracked tree inventory did not reveal matching standalone original portrait/audio files. The declared hashes and media properties therefore remain **unmatched to accessible source files** in this audit.
- The configuration itself states that external cloning is not enabled by default, provider credentials/authorization are required, and the provider adapter is only an interface until explicitly authorized.

## Related PR status checked on GitHub

| PR | Current state | Merge result | Scope |
|---|---|---|---|
| #2355 | Closed | Merged | Character description and acceptance gates |
| #2357 | Closed | Merged | Product-media manifest integrity validator and tests |
| #2360 | Closed | Merged | Character implementation rubric |
| #2361 | Closed | Merged | Layered security baseline and presentation roadmap |

The PR descriptions explicitly distinguish repository documentation/metadata checks from live provider integration and real-world asset/media validation. PR merge status does not by itself mean all external gates passed.

## Safe next implementation sequence

1. **Asset match gate:** locate the original portrait and original voice file; calculate SHA-256 locally and compare against the configured values. Do not overwrite the source files.
2. **MP4 publication:** only add the recording to a repository path after confirming the desired public exposure and that repository size/publishing constraints are suitable. At 52 MB, avoid putting it through the ordinary GitHub contents API; use an appropriate release/LFS/external media path if selected.
3. **Provider test:** use the user's authorized HeyGen account directly; record project/job identifiers and actual output URLs without publishing secrets or API keys.
4. **Acceptance run:** record test Q&A, evidence-state negative test, voice authorization, face/motion, lip-sync/timing, output playback and reviewer results.
5. **Release gate:** keep any failed or unrun criterion marked `NOT VERIFIED` or `BLOCKED`; do not label the system live/production-ready until the end-to-end evidence exists.

## Evidence boundary

This audit does not claim that ChatGPT can restore a deleted prior chat, that HeyGen is connected, that an avatar or cloned voice exists, that the supplied MP4 is uploaded to GitHub, or that any live presentation has passed acceptance testing.
