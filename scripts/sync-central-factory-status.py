#!/usr/bin/env python3
"""Synchronize the Research Institute status from the central Omniverse-Platform repo."""
from __future__ import annotations
import base64, json, os, urllib.error, urllib.request
from pathlib import Path

CENTRAL = "rampaulsaini/Omniverse-Platform"
SOURCE_PATH = "data/public/factory-status.json"
TARGET = Path("factory-status.json")

def main() -> int:
    token = os.environ.get("ORCHESTRATOR_TOKEN", "").strip()
    current = json.loads(TARGET.read_text(encoding="utf-8")) if TARGET.exists() else {}
    if not token:
        current["orchestrator_credential_configured"] = False
        current["live_counters"] = False
        current["last_refresh_note"] = "Federation token is not configured; retained safe local status."
        TARGET.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 0

    url = f"https://api.github.com/repos/{CENTRAL}/contents/{SOURCE_PATH}?ref=main"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "shirmani-research-factory-federation",
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            payload = json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        current["orchestrator_credential_configured"] = True
        current["live_counters"] = False
        current["last_refresh_note"] = "Central status could not be verified; previous safe status retained."
        current["federation_error_type"] = type(exc).__name__
        TARGET.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 0

    if payload.get("encoding") != "base64" or not payload.get("content"):
        raise RuntimeError("central status response did not contain base64 content")
    central = json.loads(base64.b64decode(payload["content"]).decode("utf-8"))
    required = {"schema_version", "repository", "generated_at", "state"}
    if not required.issubset(central):
        raise RuntimeError("central status contract is incomplete")
    if central["repository"] != CENTRAL:
        raise RuntimeError("central status repository identity mismatch")

    synced = {
        **central,
        "research_institute_repository": "rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-",
        "central_orchestrator": CENTRAL,
        "orchestrator_credential_configured": True,
        "federation_verified": True,
        "live_counters": bool(central.get("live_cross_repository_counters", False)),
        "last_refresh_note": "Status synchronized from the central safe factory export.",
    }
    TARGET.write_text(json.dumps(synced, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
