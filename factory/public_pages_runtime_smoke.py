#!/usr/bin/env python3
"""Check the deployed GitHub Pages runtime, not just the pre-deploy workspace."""
from __future__ import annotations

import hashlib
import json
import os
import time
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit, urlunsplit, parse_qsl, urlencode
from urllib.request import Request, urlopen

BASE = os.environ.get("PAGES_URL", "").strip()
if not BASE.startswith(("https://", "http://")):
    raise SystemExit("PAGES_RUNTIME_SMOKE_FAIL: PAGES_URL must be an HTTP(S) URL")
BASE = BASE.rstrip("/") + "/"

ROUTES = (
    "",
    "showroom/public-product-showroom.html",
    "showroom-public.html",
    "showroom/shirmani-supreme-character-studio.html",
    "showroom/shirmani-supreme-heart-view-preview.html",
    "generated/live-production-state.json",
    "generated/public-production-asset-overlay.json",
    "generated/public-production-index.html",
    "generated/public-production-catalog.json",
    "generated/public-production-module-index.json",
)


def fetch(route: str) -> tuple[bytes, str]:
    url = urljoin(BASE, route)
    last_error = "no response"
    last_url = url
    last_status = "no response"
    last_content_type = "unknown"
    last_body_snippet = ""
    for attempt in range(1, 9):
        try:
            # GitHub Pages/CDN can briefly serve an older deployment after the
            # deploy action reports success. Give every request a unique query
            # key as well as Cache-Control so the smoke gate checks the newest
            # published representation rather than a cached JSON response.
            parts = urlsplit(url)
            query = dict(parse_qsl(parts.query, keep_blank_values=True))
            query["_shirmani_runtime_smoke"] = f"{time.time_ns()}-{attempt}"
            request_url = urlunsplit(
                (parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment)
            )
            request = Request(
                request_url,
                headers={
                    "User-Agent": "SHIRMANI-Pages-Runtime-Smoke/1.0",
                    "Cache-Control": "no-cache, no-store, max-age=0",
                    "Pragma": "no-cache",
                },
            )
            last_url = request_url
            with urlopen(request, timeout=20) as response:
                body = response.read()
                last_status = str(response.status)
                last_content_type = response.headers.get("Content-Type", "unknown")
                last_body_snippet = body[:240].decode("utf-8", errors="replace").replace("\n", " ")
                if response.status != 200:
                    last_error = f"HTTP {response.status}"
                elif not body:
                    last_error = "empty response"
                else:
                    print(
                        f"ROUTE_HTTP route={route or '/'} status={response.status} "
                        f"requested_url={request_url} final_url={response.geturl()} "
                        f"content_type={last_content_type} bytes={len(body)}"
                    )
                    return body, last_content_type
        except HTTPError as exc:
            last_url = exc.geturl()
            last_status = str(exc.code)
            last_content_type = exc.headers.get("Content-Type", "unknown")
            try:
                last_body_snippet = exc.read(240).decode("utf-8", errors="replace").replace("\n", " ")
            except OSError:
                last_body_snippet = ""
            last_error = f"HTTP {exc.code}"
        except (URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
        if attempt < 8:
            time.sleep(8)
    raise SystemExit(
        f"PAGES_RUNTIME_SMOKE_FAIL: route={route or '/'} base_url={BASE} "
        f"last_url={last_url} status={last_status} content_type={last_content_type} "
        f"body_snippet={last_body_snippet!r} error={last_error}"
    )


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
expected_live_sha256 = os.environ.get("EXPECTED_LIVE_STATE_SHA256", "").strip()
expected_live_generated_at = os.environ.get("EXPECTED_LIVE_STATE_GENERATED_AT", "").strip()
actual_live_sha256 = hashlib.sha256(responses["generated/live-production-state.json"]).hexdigest()
actual_live_generated_at = str(live.get("generated_at", ""))
print(
    "PUBLIC_STATE_FINGERPRINT "
    f"expected_generated_at={expected_live_generated_at or 'NOT_PROVIDED'} "
    f"expected_sha256={expected_live_sha256 or 'NOT_PROVIDED'} "
    f"actual_generated_at={actual_live_generated_at or 'MISSING'} "
    f"actual_sha256={actual_live_sha256}"
)
if expected_live_sha256 and actual_live_sha256 != expected_live_sha256:
    raise SystemExit(
        "PAGES_RUNTIME_SMOKE_FAIL: deployed live-production-state.json does not match "
        "the pre-upload artifact fingerprint; compare deployment ordering/artifact contents "
        f"(expected_generated_at={expected_live_generated_at or 'NOT_PROVIDED'}, "
        f"actual_generated_at={actual_live_generated_at or 'MISSING'}, "
        f"expected_sha256={expected_live_sha256}, actual_sha256={actual_live_sha256})"
    )
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
    raise SystemExit(f"PAGES_RUNTIME_SMOKE_FAIL: deployed live catalog target is {live.get('catalog_identities')!r}, expected {target}")
if overlay.get("product_count") != target:
    raise SystemExit(f"PAGES_RUNTIME_SMOKE_FAIL: deployed overlay target is {overlay.get('product_count')!r}, expected {target}")
if not isinstance(produced, int) or not isinstance(overlay_rows, list) or produced != len(overlay_rows):
    raise SystemExit("PAGES_RUNTIME_SMOKE_FAIL: deployed overlay produced_count does not match its products rows")
catalog_lanes = catalog.get("lanes")
catalog_results = catalog.get("cycle_results")
if not isinstance(catalog_lanes, dict) or not isinstance(catalog_results, int):
    raise SystemExit("PAGES_RUNTIME_SMOKE_FAIL: deployed production catalog has an unexpected schema")
if sum(value for value in catalog_lanes.values() if isinstance(value, int)) != catalog_results:
    raise SystemExit("PAGES_RUNTIME_SMOKE_FAIL: deployed production catalog lane counts do not match cycle_results")
module_rows = modules.get("modules")
if not isinstance(module_rows, dict) or modules.get("module_count") != len(module_rows):
    raise SystemExit("PAGES_RUNTIME_SMOKE_FAIL: deployed module index count does not match its modules")
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
