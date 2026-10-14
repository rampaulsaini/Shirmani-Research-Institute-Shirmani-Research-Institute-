#!/usr/bin/env python3
"""Fail-closed release gate for product-specific media evidence.

This validates declared artifacts; it does not prove scientific claims, customer
quality, or that a provider integration works. Paths are resolved under --root.
"""
from __future__ import annotations

import argparse
import json
import re
import struct
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = (
    "product_id", "version", "short_description", "passport_url",
    "qr_target_url", "screenshot_path", "screenshot_kind",
    "demo_video_path", "demo_status", "usage_guide_path",
    "qr_scan_test", "photo_asset_status",
)
ID_RE = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,63}$")


def is_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"https", "http"} and bool(parsed.netloc)


def has_raster_signature(path: Path) -> bool:
    try:
        head = path.read_bytes()[:16]
    except OSError:
        return False
    return (
        head.startswith(b"\x89PNG\r\n\x1a\n")
        or head.startswith(b"\xff\\xd8\xff")
        or (len(head) >= 12 and head[:4] == b"RIFF" and head[8:12] == b"WEBP")
    )


def has_mp4_signature(path: Path) -> bool:
    try:
        head = path.read_bytes()[:32]
    except OSError:
        return False
    # ISO Base Media File Format commonly stores the ftyp box at byte offset 4.
    return len(head) >= 12 and head[4:8] == b"ftyp"


def validate_manifest(manifest: object, root: Path) -> dict:
    errors: list[str] = []
    products = manifest.get("products") if isinstance(manifest, dict) else None
    if not isinstance(products, list) or not products:
        return {"status": "BLOCKED", "product_count": 0,
                "errors": ["manifest must contain a non-empty products array"],
                "products": []}

    seen: set[tuple[str, str]] = set()
    seen_qr: dict[str, str] = {}
    results = []
    for index, item in enumerate(products):
        prefix = f"products[{index}]"
        item_errors: list[str] = []
        if not isinstance(item, dict):
            results.append({"index": index, "status": "BLOCKED",
                            "errors": ["product entry must be an object"]})
            continue
        for field in REQUIRED:
            if not item.get(field):
                item_errors.append(f"missing required field: {field}")

        product_id = item.get("product_id")
        version = item.get("version")
        if not isinstance(product_id, str) or not ID_RE.fullmatch(product_id):
            item_errors.append("product_id must be a stable uppercase ID (3–64 chars)")
        if not isinstance(version, str) or not version.strip():
            item_errors.append("version must be a non-empty string")
        identity = (product_id, version)
        if isinstance(product_id, str) and isinstance(version, str):
            if identity in seen:
                item_errors.append(f"duplicate product_id/version: {product_id}@{version}")
            seen.add(identity)

        passport = item.get("passport_url")
        qr_target = item.get("qr_target_url")
        if not is_http_url(passport):
            item_errors.append("passport_url must be an absolute HTTP(S) URL")
        if not is_http_url(qr_target):
            item_errors.append("qr_target_url must be an absolute HTTP(S) URL")
        if is_http_url(passport) and is_http_url(qr_target) and passport != qr_target:
            item_errors.append("QR target must exactly match this product's passport URL")
        if isinstance(qr_target, str):
            owner = seen_qr.get(qr_target)
            if owner and owner != str(product_id):
                item_errors.append(f"QR destination reused by products {owner} and {product_id}")
            seen_qr[qr_target] = str(product_id)

        if item.get("qr_scan_test") != "PASS":
            item_errors.append("mobile QR scan test must be PASS")
        if item.get("photo_asset_status") != "VERIFIED":
            item_errors.append("original photo asset must be VERIFIED; no substitute allowed")
        if not isinstance(item.get("short_description"), str) or len(item["short_description"].strip()) < 8:
            item_errors.append("short_description must contain at least 8 characters")

        screenshot = root / str(item.get("screenshot_path", ""))
        if item.get("screenshot_kind") != "REAL_BROWSER_SCREENSHOT":
            item_errors.append("screenshot must be a real browser screenshot, not a mock-up/SVG")
        elif not screenshot.is_file() or not has_raster_signature(screenshot):
            item_errors.append("real raster screenshot file missing or signature invalid")

        video = root / str(item.get("demo_video_path", ""))
        if item.get("demo_status") != "RECORDED":
            item_errors.append("demo video is not recorded; label STORYBOARD — NOT RECORDED")
        elif not video.is_file() or not has_mp4_signature(video):
            item_errors.append("actual MP4 demo file missing or ftyp signature invalid")

        guide = root / str(item.get("usage_guide_path", ""))
        if not guide.is_file() or guide.stat().st_size == 0:
            item_errors.append("usage guide file missing or empty")

        results.append({
            "product_id": product_id,
            "version": version,
            "status": "PASS" if not item_errors else "BLOCKED",
            "errors": item_errors,
        })
        errors.extend(f"{prefix} ({product_id or 'unknown'}): {e}" for e in item_errors)

    return {
        "status": "PASS" if not errors else "BLOCKED",
        "product_count": len(products),
        "passed_count": sum(p.get("status") == "PASS" for p in results),
        "blocked_count": sum(p.get("status") == "BLOCKED" for p in results),
        "errors": errors,
        "products": results,
        "note": "Manifest validation is not independent scientific verification or proof of live integration.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        report = {"status": "BLOCKED", "product_count": 0,
                  "errors": [f"cannot read manifest: {exc}"], "products": []}
    else:
        report = validate_manifest(manifest, args.root.resolve())
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output, encoding="utf-8")
    print(output, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
