#!/usr/bin/env python3
"""Check the deployed GitHub Pages runtime, not just the pre-deploy workspace."""
from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

BASE = os.environ.get("PAGES_URL", "").strip()
if not BASE.startswith(("https://", "http://")):
    raise SystemExit("PAGES_RUNTIME_SMOKE_FAIL: PAGES_URL must be an HTTP(S) URL")
BASE = BASE.rstrip("/") + "/"

ROUTES = (
    "",
    "showroom/public-product-showroom.html",
    "showroom-public.html",
    "generated/live-production-state.json",
    "generated/public-production-asset-overlay.json",
    "generated/public-production-index.html",
    "generated/public-production-catalog.json",
    "generated/public-production-module-index.json",
)


def fetch(route: str) -> tuple[bytes, str]:
    url = urljoin(BASE, route)
    last_error = "no response"
    for attempt in range(1, 9):
        try:
            request = Request(url, headers={"User-Agent": "SHIRMANI-Pages-Runtime-Smoke/1.0", "Cache-Control": "no-cache"})
            with urlopen(request, timeout=20) as response:
                body = response.read()
                if response.status != 200:
                    last_error = f"HTTP {response.status}"
                elif not body:
                    last_error = "empty response"
                else:
                    return body, response.headers.get("Content-Type", "")
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
        if attempt < 8:
            time.sleep(8)
    raise SystemExit(f"PAGES_RUNTIME_SMOKE_FAIL: {route or '/'} unavailable after retries: {last_error}")


responses = {}
for route in ROUTES:
    body, content_type = fetch(route)
    responses[route] = body
    print(f"ROUTE_PASS {route or '/'} bytes={len(body)} content_type={content_type}")

def read_json(route: str) -> dict:
    try:
        value = json.loads(responses[route].decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SystemExit(f"PAGES_RUNTIME_SMOKE_FAIL: invalid deployed JSON {route}: {exc}")
    if not isinstance(value, dict):
        raise SystemExit(f"PAGES_RUNTIME_SMOKE_FAIL: deployed JSON {route} must be an object")
    return value

live = read_json("generated/live-production-state.json")
overlay = read_json("generated/public-production-asset-overlay.json")
catalog = read_json("generated/public-production-catalog.json")
modules = read_json("generated/public-production-module-index.json")

for route, payload in (
    ("generated/live-production-state.json", live),
    ("generated/public-production-asset-overlay.json", overlay),
    ("generated/public-production-catalog.json", catalog),
    ("generated/public-production-module-index.json", modules),
):
    stamp = payload.get("generated_at")
    if not isinstance(stamp, str):
        raise SystemExit(f"PAGES_RUNTIME_SMOKE_FAIL: {route} has no generated_at timestamp")
    try:
        parsed = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("timezone required")
    except ValueError as exc:
        raise SystemExit(f"PAGES_RUNTIME_SMOKE_FAIL: invalid timestamp in {route}: {exc}")
    age = (datetime.now(timezone.utc) - parsed.astimezone(timezone.utc)).total_seconds()
    if age < -300 or age > 7200:
        raise SystemExit(f"PAGES_RUNTIME_SMOKE_FAIL: stale/future deployed file {route}, age_seconds={int(age)}")

target = int(os.environ.get("PRODUCT_TARGET", "5000"))
produced = overlay.get("produced_count")
overlay_rows = overlay.get("products")
if live.get("catalog_identities") != target:
    raise SystemExit(f"PAGES_RUNTIME_SMOKE_FAIL: deployed catalog target is {live.get('catalog_identities')!r}, expected {target}")
if not isinstance(produced, int) or not isinstance(overlay_rows, list) or produced != len(overlay_rows):
    raise SystemExit("PAGES_RUNTIME_SMOKE_FAIL: deployed overlay count does not match its product rows")
if live.get("public_production_assets") != produced:
    raise SystemExit("PAGES_RUNTIME_SMOKE_FAIL: deployed live status and overlay produced_count disagree")
if live.get("independent_verification_claimed", 0) != 0:
    raise SystemExit("PAGES_RUNTIME_SMOKE_FAIL: production asset count must not imply independent verification")

print(json.dumps({
    "gate": "PAGES_RUNTIME_SMOKE",
    "result": "PASS",
    "base_url": BASE,
    "routes_checked": len(ROUTES),
    "catalog_target": target,
    "public_production_assets": produced,
    "independent_verification_claimed": live.get("independent_verification_claimed", 0),
    "truth_boundary": "public HTTP reachability and JSON consistency do not establish live-avatar, payment, sales, or independent QC readiness",
}, ensure_ascii=False))
