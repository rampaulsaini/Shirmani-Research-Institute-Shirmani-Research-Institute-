# SHIRMANI SUPREME — Asset Onboarding & Release Gates
**Date:** 2026-10-14  
**State:** IMPLEMENTATION CHECKLIST — NOT A LIVE-INTEGRATION CLAIM

## Approved character decision
The approved character profile is the source of truth. Communication must be simple, warm, respectful, context-aware and evidence-based. The original face photo may only be proportionally resized/scaled and placed in a layout. Do not generate, redraw, retouch, recolour, beautify, reshape or substitute the face. Use only the owner's original authorised voice asset. If either asset is missing or cannot be verified, keep that capability blocked.

## Current verified repository facts
- The character profile and deterministic contract tests exist in `config/shirmani-supreme-character-profile.json` and `tests/test_shirmani_supreme_character_profile.py`.
- Pull request #2249 was merged on 2026-10-12 (merge commit `b466bfa6567f79eade07016ded123980b8ce90b7`).
- The profile says `SPECIFICATION_ONLY`; photo and voice assets are marked `NOT_VERIFIED_IN_REPOSITORY`.
- V2 authorised voice, V3 photo/avatar and V4 live presentation remain blocked until their actual assets, providers/permissions where needed, and tests are recorded.
- A storyboard is not an MP4; a mock-up is not a real product screenshot; a QR preview is not proof that the QR scans.

## Required asset intake
1. **Original photo:** owner supplies the exact original file. Record its repository path, file hash, dimensions and permission/ownership confirmation. Do not edit pixels; only proportionally scale for display.
2. **Original voice:** owner supplies an authorised recording or confirms the authorised provider asset and access method. Record consent/authorisation, format, duration, sample rate and a test-file reference. Never synthesise a replacement and label it original.
3. **Per-product assets:** unique product ID/version, product-specific cover, readable short description, QR destination/passport, actual VIP screenshot, recorded product-specific demo video, and usage guide.
4. **Privacy/security:** do not commit API keys, passwords, access tokens, private customer data, or provider credentials. Store secrets in repository/environment secret storage; document only secret names, never values.

## Release gates and measurable acceptance criteria

| Gate | Pass condition | Evidence to retain |
|---|---|---|
| G0 — Identity | Original photo/voice source and authorisation recorded; no substitution | Asset path, hash, dimensions/format, authorisation record |
| G1 — Character | Script follows the approved style and separates fact, source, philosophy and uncertainty | Versioned sample Q&A plus reviewer checklist |
| G2 — Voice | Authorised voice playback tested with permission; intelligibility and timing checked | Test input/output, provider/version, timestamp and result |
| G3 — Photo/avatar | Original image remains pixel-source-identical apart from display scaling; no generated face | Source hash comparison, screenshot and review |
| G4 — Evidence | Sourced claims cite sources; uncertain claims say “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।” | Test cases and expected/observed outputs |
| G5 — Product QR | QR resolves to the correct product passport and scans on a mobile device | Product ID, destination URL and scan-test record |
| G6 — Screenshot/demo | Actual product screenshot and recorded product-specific demo exist; no storyboard presented as video | File paths, metadata and reviewer check |
| G7 — End-to-end | Voice → context/reasoning → evidence gate → presentation → audit passes as one flow | Test report, timing, failures and run ID |
| G8 — Release | All critical gates pass; no secrets or unsupported sales claims; human approval recorded | Release checklist and commit/release identifier |

A failed critical gate blocks release. A successful workflow run proves only that the workflow ran; it does not prove the product is independently verified.

## Four capability tiers
- **V1 — Clear Script:** may be tested as a text-only prototype. Do not imply a live avatar or voice connection.
- **V2 — Authorised Voice:** blocked until the original authorised voice is available and a playback test passes.
- **V3 — Photo / Avatar:** blocked until the exact original photo is available and the selected provider/workflow passes identity and visual checks.
- **V4 — Live Presentation:** blocked until V2 and V3 dependencies plus end-to-end lip-sync, timing, accessibility, failure handling and audit tests pass.

## Product-specific media release record
For each product, record: `product_id`, `version`, `cover_path`, `original_logo_source`, `short_description`, `passport_url`, `qr_scan_test`, `vip_screenshot_path`, `demo_video_path`, `usage_guide_path`, `test_report_path`, `release_status`, and `reviewed_at`. Missing media must be labelled honestly as `NOT RECORDED` or `BLOCKED`, not counted as complete.

## Immediate next actions
1. Supply the exact original photo and authorised voice file/asset reference through an approved upload path.
2. Run the repository contract tests in CI and retain the actual run URL/results.
3. Select and configure the authorised voice/avatar provider without committing secrets.
4. Implement and test one product end-to-end before scaling the same release contract across the catalogue.
5. Record real demo MP4s and VIP screenshots per product; then verify QR scans on mobile.
6. Only after those gates pass, mark the relevant capability `VERIFIED`.

## Reporting template
- Repository change: link + commit SHA
- Automated tests: run URL + pass/fail counts
- Assets received and verified: exact paths + hashes (no private secrets)
- Voice/avatar/lip-sync: tested state and evidence
- Product media: recorded demo/screenshot/QR scan counts
- Blockers: exact missing dependency
- Sales/outreach: report only messages actually sent through an authorised channel and outcomes actually received
