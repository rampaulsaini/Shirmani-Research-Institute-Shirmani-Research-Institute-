# Character source-media audit gate

**State:** implementation proposal; audit execution and CI status must be recorded separately.

## Why this exists

The repository declares photo and audio SHA-256 values in `config/authorized-voice-integration.json`, but a declaration is not proof that the matching original media files are present. The public Character Studio correctly marks the original photo and authorised voice as required. This audit makes the gap measurable without guessing which image is the approved original.

## Run

```sh
python scripts/audit_character_assets.py
python -m unittest tests/test_character_asset_audit.py
```

To include a local file supplied outside the repository (for example, a recording captured while using a video/avatar app), pass its local path. The tool hashes it read-only and reports only a redacted display path, byte count, extension and SHA-256:

```sh
python scripts/audit_character_assets.py --external-media /path/to/recording.mp4
```

Repeat `--external-media` for multiple files. The tool does not copy or upload these files. The full MP4 hash is not interchangeable with the hash of its embedded audio track; if a dedicated audio source is required, extract it separately and verify that file and its authorisation. A hash match is only a file-integrity match; a human must still confirm source, ownership/consent and intended use. Missing matches remain **BLOCKED**.

## Recording inspected for this task

The user-attached `Video.Guru_20261013-080950532.mp4` is 35.983 seconds, 888×1920 portrait H.264 video with AAC stereo audio at 44.1 kHz. Its visible frames show a mobile recording workflow with the user's face and a HeyGen recording screen/instructions; the ending returns to a recording prompt. It is evidence that a recording workflow was open, not proof that HeyGen generated an avatar, that the audio is the configured original voice file, or that a provider connection/test completed.

Local file SHA-256: `a9f7872659ff6f7ceded7624b0f41c04163a395ae1dfb96fd03c209f32566f99`.
This hash identifies the exact attached MP4 only; it does not establish ownership, consent, provider upload, or a match to the separately configured audio hash.

## Release policy

- Do not treat `css/assets/images/profile.jpg` as the approved identity photo merely because it is present.
- Do not treat the supplied MP4 as the original voice recording without checking the contents and matching hash.
- Do not activate voice cloning, avatar, lip-sync or live presentation until the exact source assets, consent/authorisation and provider-side test outputs are recorded.
- This is a local repository audit, not a security certification or production readiness claim.
