#!/usr/bin/env python3
"""Validate a product-media manifest before showroom publication.

This checks metadata integrity only. It does not prove that URLs work, QR codes
scan on a phone, media files are authentic, or demos actually show the product.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = (
    "product_id",
    "version",
    "short_description",
    "passport_url",
    "qr_url",
    "screenshot",
    "demo_video",
    "usage_guide",
)
URL_FIELDS = ("passport_url", "qr_url", "screenshot", "demo_video", "usage_guide")
MEDIA_FIELDS = ("screenshot", "demo_video", "usage_guide")


def validate_manifest(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["manifest must be a JSON object"]
    products = data.get("products")
    if not isinstance(products, list):
        return ["'products' must be a list"]

    seen: dict[str, dict[str, str]] = {field: {} for field in ("product_id",) + URL_FIELDS}
    for index, product in enumerate(products):
        label = f"products[{index}]"
        if not isinstance(product, dict):
            errors.append(f"{label} must be an object")
            continue
        for field in REQUIRED_FIELDS:
            value = product.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}.{field} is required and must be a non-empty string")
        product_id = product.get("product_id")
        if isinstance(product_id, str) and product_id.strip():
            previous = seen["product_id"].get(product_id)
            if previous:
                errors.append(f"duplicate product_id {product_id!r} at {previous} and {label}")
            else:
                seen["product_id"][product_id] = label

        for field in URL_FIELDS:
            value = product.get(field)
            if not isinstance(value, str) or not value.strip():
                continue
            if not value.startswith(("https://", "http://")):
                errors.append(f"{label}.{field} must be an http(s) URL")
            previous = seen[field].get(value)
            if previous:
                errors.append(f"reused {field} URL at {previous} and {label}: {value}")
            else:
                seen[field][value] = label

        for field in MEDIA_FIELDS:
            value = product.get(field)
            if isinstance(value, str) and value.strip() and value.upper().startswith(("BLOCKED", "NOT PROVIDED", "STORYBOARD")):
                # Explicit placeholders are permitted in drafts but must not be published.
                if data.get("release_status") == "PUBLISHED":
                    errors.append(f"{label}.{field} is a placeholder and cannot be published")

    if data.get("release_status") == "PUBLISHED":
        for index, product in enumerate(products):
            if isinstance(product, dict) and product.get("status") not in ("VERIFIED", "PUBLISHED"):
                errors.append(f"products[{index}].status must be VERIFIED or PUBLISHED for release")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="path to product-media-manifest.json")
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read valid JSON manifest: {exc}")
        return 2
    errors = validate_manifest(data)
    if errors:
        print(f"FAIL: {len(errors)} product-media manifest issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: product-media manifest metadata is internally consistent")
    print("NOTE: URL reachability, mobile QR scanning, asset authenticity, and demo playback require separate tests.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
