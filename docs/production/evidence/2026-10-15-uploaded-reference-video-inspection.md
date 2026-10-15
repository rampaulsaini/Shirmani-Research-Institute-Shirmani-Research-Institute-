# Uploaded reference-video inspection — 2026-10-15

## Scope and evidence boundary

This record documents technical inspection of the MP4 attached to the ChatGPT conversation on 2026-10-15. It is an uploaded reference/screen recording, **not proof by itself** of an original portrait file, a separately authorized voice asset, a connected HeyGen project, a generated avatar video, successful lip-sync, or live Q&A.

## Measured file facts

- Original uploaded filename: `Video.Guru_20261013-080950532.mp4`
- File size: 52,076,438 bytes (about 52.08 MB decimal / 49.66 MiB)
- Duration: 35.982993 seconds (about 35.98 s)
- Video stream: H.264, 888 × 1920 portrait
- Audio stream: AAC, 44.1 kHz, 2 channels
- SHA-256 of the exact uploaded bytes: `a9f7872659ff6f7ceded7624b0f41c04163a395ae1dfb96fd03c209f32566f99`

## What this does and does not establish

- **Verified:** the uploaded file was readable in the current working session; its container metadata and SHA-256 were computed.
- **Not verified:** that these bytes match the original portrait or an authorized standalone voice recording.
- **Not verified:** voice ownership/authorization, HeyGen API/project connection, generated output, lip-sync quality, end-to-end Q&A, live presentation, or production readiness.
- The SHA-256 above identifies this particular uploaded MP4 only. It must not be presented as the portrait's hash or as proof that the portrait is unchanged.

## Next measurable gates

1. Locate the original portrait file (not a frame extracted from this screen recording) and record its SHA-256 before any processing.
2. Locate the separately authorized voice/audio source, record its SHA-256, and document permission/source.
3. Verify provider connection through an authenticated, non-secret-leaking test; keep API keys in repository/environment secrets and never in source files or logs.
4. Generate a provider output and preserve its actual URL/file, job ID, timestamps, and provider response with secrets redacted.
5. Run a spoken-script playback test and objective audio/video timing review; document observed lip-sync result rather than infer it from a setup screen.
6. Run the agreed Hindi/English Q&A matrix end-to-end, including insufficient-evidence and error cases; attach results before marking live/production VERIFIED.

## Repository publication note

This Markdown evidence record can be committed to the pull-request branch. The 52 MB MP4 itself has **not** been uploaded to the repository by this action. Publish the binary only through an approved repository media route (for example, Git LFS or a release asset) after checking repository policy and confirming that the recording contains no unintended private material. A repository link must not be claimed until the binary upload and resulting URL are verified.
