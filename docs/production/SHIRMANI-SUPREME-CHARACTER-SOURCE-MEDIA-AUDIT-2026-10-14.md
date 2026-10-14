# Character source-media audit gate

**State:** implementation proposal; audit execution and CI status must be recorded separately.

## Why this exists
The repository contains a declared photo SHA-256 and audio SHA-256 in `config/authorized-voice-integration.json`, but a declaration is not proof that the matching original media files are present in the repository. The current public Character Studio correctly marks its photo and authorised voice as required. This audit makes that gap measurable without guessing which image is the owner's approved original.

## Run
```sh
python scripts/audit_character_assets.py
python -m unittest tests/test_character_asset_audit.py
```

The report inventories media candidates and compares their SHA-256 values with the configured source hashes. A hash match is only a file-integrity match; a human must still confirm the source, ownership/consent and intended use. Missing hash matches remain **BLOCKED**. The script does not contact HeyGen or any provider and does not generate, upload, edit or publish media.

## Release policy
- Do not treat `css/assets/images/profile.jpg` as the approved identity photo merely because it is present.
- Do not treat the supplied MP4 as the original voice recording without checking its contents and matching hash.
- Do not activate voice cloning, avatar, lip-sync or live presentation until the exact source assets, consent/authorisation and provider-side test outputs are recorded.
- This is a local repository audit, not a security certification or production readiness claim.
