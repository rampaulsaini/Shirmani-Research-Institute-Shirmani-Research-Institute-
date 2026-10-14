# Product Media Release Gate

**Status: implementation added; runtime validation is pending until CI executes.** This document specifies a fail-closed check, not a claim that the catalogue is verified.

## Manifest contract

Each product entry in a JSON file passed to `factory/product_media_release_gate.py` must include:

- Stable `product_id` and `version`
- On-image `short_description`
- Product-specific `passport_url` and identical `qr_target_url`
- `screenshot_path` with `screenshot_kind: REAL_BROWSER_SCREENSHOT`
- `demo_video_path` with `demo_status: RECORDED`
- `usage_guide_path`
- `qr_scan_test: PASS` based on a real mobile scan
- `photo_asset_status: VERIFIED` based on the authorized original image

## Fail-closed rules

The validator blocks release if a field is absent, a product ID/version repeats, a QR destination is shared or differs from the passport URL, the screenshot is not a raster image with a recognized signature, the MP4 is missing or has no ISO-BMFF `ftyp` signature, the guide is absent, the mobile QR scan has not passed, or the original photo asset is not verified.

The file-signature checks are sanity checks only; they do not establish that a video is playable, depicts the advertised workflow, or that a screenshot came from a genuine browser session. Those require review/playback evidence. A QR scan status is an evidence declaration and must be backed by a recorded test record.

Use honest labels for incomplete assets: `ILLUSTRATIVE MOCK-UP`, `STORYBOARD — NOT RECORDED`, `BLOCKED — PHOTO ASSET REQUIRED`, and `BLOCKED — VOICE ASSET REQUIRED`.

## Run

```sh
python -m unittest tests/test_product_media_release_gate.py -v
python factory/product_media_release_gate.py --manifest path/to/product-media-manifest.json --root . --report generated/product-media-release-report.json
```

Exit code is 0 only when every listed product passes. A PASS means the declared artifact contract passed these deterministic checks; it is not independent scientific verification, proof of provider integration, customer approval, sales, or income.
