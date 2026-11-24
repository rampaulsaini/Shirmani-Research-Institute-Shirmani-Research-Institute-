#!/usr/bin/env python3
"""Synchronize the Research Institute status from the central Omniverse-Platform repo."""
from __future__ import annotations

import base64
import binascii
import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

CENTRAL = "rampaulsaini/Omniverse-Platform"
SOURCE_PATH = "data/public/factory-status.json"
HEALTH_PATH = "data/federation/health.json"
DISPATCH_PATH = "federation/status/latest.json"
TARGET = Path("factory-status.json")
HEALTH_TARGET = Path("generated/federation-health.json")
DISPATCH_TARGET = Path("generated/federation-dispatch.json")
VALID_HEALTH_STATES = {"OPERATIONAL", "DEGRADED", "OFFLINE", "UNKNOWN"}
RESEARCH_REPOSITORY = (
    "rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-"
)


def write_unknown_health(note: str, error_type: str | None = None) -> None:
    """Always leave a parseable, fail-closed health artifact for public dashboards."""
    HEALTH_TARGET.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "repository": CENTRAL,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "state": "UNKNOWN",
        "research_institute_repository": RESEARCH_REPOSITORY,
        "central_orchestrator": CENTRAL,
        "federation_verified": False,
        "live_cross_repository_counters": False,
        "secrets_exposed": False,
        "pii_exposed": False,
        "note": note,
    }
    if error_type:
        payload["error_type"] = error_type
    HEALTH_TARGET.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_unknown_dispatch(note: str, error_type: str | None = None) -> None:
    """Write a fail-closed dispatch artifact when central evidence is unavailable."""
    DISPATCH_TARGET.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "repository": CENTRAL,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_generated_at": None,
        "state": "UNKNOWN",
        "dispatch_record_verified": False,
        "dispatch": None,
        "targets": [],
        "note": note,
    }
    if error_type:
        payload["error_type"] = error_type
    DISPATCH_TARGET.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    # Write a safe default first. A later successful fetch replaces it with
    # verified source data; every early return therefore leaves a valid artifact.
    write_unknown_health(
        "Central federation health has not yet been synchronized."
    )
    write_unknown_dispatch(
        "Central dispatch record has not yet been synchronized."
    )
    token = os.environ.get("ORCHESTRATOR_TOKEN", "").strip()
    current = json.loads(TARGET.read_text(encoding="utf-8")) if TARGET.exists() else {}

    if not token:
        current["orchestrator_credential_configured"] = False
        current["live_counters"] = False
        current["federation_verified"] = False
        current["last_refresh_note"] = (
            "Federation token is not configured; retained safe local status."
        )
        TARGET.write_text(
            json.dumps(current, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        write_unknown_health(
            "Federation token is not configured; central health remains UNKNOWN."
        )
        write_unknown_dispatch(
            "Federation token is not configured; dispatch remains UNKNOWN."
        )
        return 0

    try:
        token.encode("ascii")
    except UnicodeEncodeError:
        current["orchestrator_credential_configured"] = False
        current["live_counters"] = False
        current["federation_verified"] = False
        current["last_refresh_note"] = (
            "Federation token is malformed or contains non-ASCII characters; "
            "retained safe local status."
        )
        current["federation_error_type"] = "MalformedCredential"
        TARGET.write_text(
            json.dumps(current, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        write_unknown_health(
            "Federation token is malformed; central health remains UNKNOWN.",
            "MalformedCredential",
        )
        write_unknown_dispatch(
            "Federation token is malformed; dispatch remains UNKNOWN.",
            "MalformedCredential",
        )
        return 0

    def fetch_json(source_path: str) -> dict:
        url = (
            f"https://api.github.com/repos/{CENTRAL}/contents/"
            f"{source_path}?ref=main"
        )
        req = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "shirmani-research-factory-federation",
            },
        )
        with urllib.request.urlopen(req, timeout=20) as response:
            payload = json.load(response)

        if payload.get("encoding") != "base64" or not payload.get("content"):
            raise RuntimeError(
                f"central status response missing content: {source_path}"
            )

        return json.loads(
            base64.b64decode(payload["content"]).decode("utf-8")
        )

    try:
        central = fetch_json(SOURCE_PATH)
        required = {"schema_version", "repository", "generated_at", "state"}
        if not required.issubset(central):
            raise RuntimeError("central status contract is incomplete")
        if central["repository"] != CENTRAL:
            raise RuntimeError("central status repository identity mismatch")
    except (
        urllib.error.HTTPError,
        urllib.error.URLError,
        TimeoutError,
        UnicodeEncodeError,
        UnicodeDecodeError,
        binascii.Error,
        json.JSONDecodeError,
        RuntimeError,
    ) as exc:
        current["orchestrator_credential_configured"] = True
        current["live_counters"] = False
        current["federation_verified"] = False
        current["last_refresh_note"] = (
            "Central status could not be verified; previous safe status retained."
        )
        current["federation_error_type"] = type(exc).__name__
        TARGET.write_text(
            json.dumps(current, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        write_unknown_health(
            "Central factory status could not be verified; health remains UNKNOWN.",
            type(exc).__name__,
        )
        return 0

    synced = {
        **central,
        "research_institute_repository": RESEARCH_REPOSITORY,
        "central_orchestrator": CENTRAL,
        "orchestrator_credential_configured": True,
        "central_health_source_verified": True,
        "federation_verified": False,
        "live_counters": bool(
            central.get("live_cross_repository_counters", False)
        ),
        "last_refresh_note": (
            "Status synchronized from the central safe factory export."
        ),
    }
    TARGET.write_text(
        json.dumps(synced, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    try:
        health = fetch_json(HEALTH_PATH)
        if health.get("repository") != CENTRAL:
            raise RuntimeError(
                "central federation health repository identity mismatch"
            )
        if health.get("state") not in VALID_HEALTH_STATES:
            raise RuntimeError("central federation health state is invalid")

        health["research_institute_repository"] = RESEARCH_REPOSITORY
        health["central_orchestrator"] = CENTRAL
        health["central_health_source_verified"] = True
        health["federation_verified"] = False
        HEALTH_TARGET.parent.mkdir(parents=True, exist_ok=True)
        HEALTH_TARGET.write_text(
            json.dumps(health, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except (
        urllib.error.HTTPError,
        urllib.error.URLError,
        TimeoutError,
        RuntimeError,
        UnicodeDecodeError,
        binascii.Error,
        json.JSONDecodeError,
    ) as exc:
        write_unknown_health(
            "Central federation health export could not be verified.",
            type(exc).__name__,
        )

    try:
        dispatch_record = fetch_json(DISPATCH_PATH)
        counters = dispatch_record.get("dispatch")
        required_counters = {"attempted", "dispatched", "deferred", "failed", "invalid"}
        if dispatch_record.get("schema_version") != 1:
            raise RuntimeError("central dispatch schema version is invalid")
        if not dispatch_record.get("federation_id") or not dispatch_record.get("generated_at"):
            raise RuntimeError("central dispatch identity or timestamp is missing")
        if not isinstance(counters, dict) or not required_counters.issubset(counters):
            raise RuntimeError("central dispatch counters are incomplete")
        if any(type(counters[key]) is not int or counters[key] < 0 for key in required_counters):
            raise RuntimeError("central dispatch counters are invalid")
        targets = dispatch_record.get("targets")
        if not isinstance(targets, list):
            raise RuntimeError("central dispatch targets are invalid")
        allowed_statuses = {"dispatched", "deferred", "failed", "invalid"}
        if any(
            not isinstance(target, dict)
            or not isinstance(target.get("repository"), str)
            or target.get("status") not in allowed_statuses
            for target in targets
        ):
            raise RuntimeError("central dispatch target record is invalid")
        observed = {
            "attempted": len(targets),
            "dispatched": sum(target["status"] == "dispatched" for target in targets),
            "deferred": sum(target["status"] == "deferred" for target in targets),
            "failed": sum(target["status"] == "failed" for target in targets),
            "invalid": sum(target["status"] == "invalid" for target in targets),
        }
        if any(counters[key] != observed[key] for key in required_counters):
            raise RuntimeError("central dispatch counters do not match target records")
        dispatch_record["source_generated_at"] = dispatch_record["generated_at"]
        dispatch_record["generated_at"] = datetime.now(timezone.utc).isoformat()
        dispatch_record["repository"] = CENTRAL
        dispatch_record["dispatch_record_verified"] = True
        dispatch_record["note"] = (
            "Source dispatch record contract validated. Dispatched means GitHub accepted repository_dispatch; "
            "it does not prove receiver receipt, task execution, QC, independent review or delivery."
        )
        DISPATCH_TARGET.parent.mkdir(parents=True, exist_ok=True)
        DISPATCH_TARGET.write_text(
            json.dumps(dispatch_record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except (
        urllib.error.HTTPError,
        urllib.error.URLError,
        TimeoutError,
        RuntimeError,
        UnicodeDecodeError,
        binascii.Error,
        json.JSONDecodeError,
    ) as exc:
        write_unknown_dispatch(
            "Central dispatch record could not be verified; dispatch remains UNKNOWN.",
            type(exc).__name__,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
