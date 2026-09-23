#!/usr/bin/env python3
"""Synchronize the Research Institute status from the central Omniverse-Platform repo."""
from __future__ import annotations
import base64, json, os, urllib.error, urllib.request
from pathlib import Path

CENTRAL = "rampaulsaini/Omniverse-Platform"
SOURCE_PATH = "data/public/factory-status.json"
HEALTH_PATH = "data/federation/health.json"
TARGET = Path("factory-status.json")
HEALTH_TARGET = Path("generated/federation-status.json")

def main() -> int:
    token = os.environ.get("ORCHESTRATOR_TOKEN", "").strip()
    current = json.loads(TARGET.read_text(encoding="utf-8")) if TARGET.exists() else {}
    if not token:
        current["orchestrator_credential_configured"] = False
        current["live_counters"] = False
        current["last_refresh_note"] = "Federation token is not configured; retained safe local status."
        TARGET.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 0

    def fetch_json(source_path: str):
        url = f"https://api.github.com/repos/{CENTRAL}/contents/{source_path}?ref=main"
        req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "shirmani-research-factory-federation",
    })
        })
        with urllib.request.urlopen(req, timeout=20) as response:
            payload = json.load(response)
        if payload.get("encoding") != "base64" or not payload.get("content"):
            raise RuntimeError(f"central status response missing content: {source_path}")
        return json.loads(base64.b64decode(payload["content"]).decode("utf-8"))

    try:
        central = fetch_json(SOURCE_PATH)
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

    try:
        health = fetch_json(HEALTH_PATH)
        if health.get("repository") != CENTRAL:
            raise RuntimeError("central federation health repository identity mismatch")
        if health.get("state") not in {"OPERATIONAL", "DEGRADED", "OFFLINE", "UNKNOWN"}:
            raise RuntimeError("central federation health state is invalid")
        health["research_institute_repository"] = "rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-"
        health["central_orchestrator"] = CENTRAL
        health["federation_verified"] = True
        HEALTH_TARGET.parent.mkdir(parents=True, exist_ok=True)
        HEALTH_TARGET.write_text(json.dumps(health, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
        HEALTH_TARGET.parent.mkdir(parents=True, exist_ok=True)
        HEALTH_TARGET.write_text(json.dumps({
            "schema_version": 1, "repository": CENTRAL, "state": "UNKNOWN",
            "research_institute_repository": "rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-",
            "central_orchestrator": CENTRAL, "federation_verified": False,
            "secrets_exposed": False, "pii_exposed": False,
            "note": "Central federation health export could not be verified.",
            "error_type": type(exc).__name__,
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
