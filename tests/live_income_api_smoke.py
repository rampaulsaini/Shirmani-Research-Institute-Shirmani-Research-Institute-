#!/usr/bin/env python3
"""Read-only smoke test for the deployed income API.

Only GET requests are sent. No enquiry, account, payment, or customer data is
created, changed, or read. Run from the repository root.
"""
from __future__ import annotations

import json
import os
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

BASE_URL = os.environ.get(
    "SHIRMANI_API_BASE_URL",
    "https://shirmani-social-api-node.onrender.com",
).rstrip("/")
EXPECTED_HOST = "shirmani-social-api-node.onrender.com"


def get_json(path: str) -> tuple[int, dict]:
    url = BASE_URL + path
    last_error = "no response"
    for attempt in range(12):
        try:
            request = Request(url, headers={"Accept": "application/json", "User-Agent": "Shirmani-ReadOnly-Smoke/1.0"})
            with urlopen(request, timeout=20) as response:
                status = response.status
                payload = json.loads(response.read().decode("utf-8"))
                return status, payload if isinstance(payload, dict) else {}
        except HTTPError as exc:
            try:
                payload = json.loads(exc.read().decode("utf-8"))
            except (ValueError, UnicodeError):
                payload = {}
            return exc.code, payload if isinstance(payload, dict) else {}
        except (URLError, TimeoutError, OSError, ValueError) as exc:
            last_error = type(exc).__name__
            if attempt < 11:
                time.sleep(10)
    raise AssertionError(f"{path}: no HTTP response after retries ({last_error})")


def require_200(path: str) -> dict:
    status, payload = get_json(path)
    if status != 200:
        safe = {
            key: payload.get(key)
            for key in ("live", "ready", "status", "database", "checks", "tables")
            if key in payload
        }
        raise AssertionError(f"{path}: expected HTTP 200, got {status}; diagnostics={safe}")
    return payload


def main() -> int:
    parsed = urlsplit(BASE_URL)
    if parsed.scheme != "https" or parsed.hostname != EXPECTED_HOST or parsed.path or parsed.query or parsed.fragment:
        raise AssertionError("API base URL must be the configured HTTPS production host.")

    health = require_200("/api/health")
    if health.get("live") is not True:
        raise AssertionError("/api/health did not confirm process liveness.")

    ready = require_200("/api/ready")
    if ready.get("ready") is not True or ready.get("checks", {}).get("database") != "READY":
        raise AssertionError("/api/ready did not confirm database and security readiness.")

    platform = require_200("/v1/platform/readiness")
    if platform.get("status") != "READY_FOR_DEPLOYMENT_CHECKS":
        raise AssertionError("/v1/platform/readiness did not confirm owner and platform readiness.")

    status = require_200("/api/status")
    if status.get("database") != "READY":
        raise AssertionError("/api/status did not confirm database readiness.")
    tables = status.get("tables", {})
    for table in ("client_enquiries", "paid_orders"):
        if tables.get(table) != "READY":
            raise AssertionError(f"/api/status: required table {table} is not READY.")

    print("LIVE INCOME API SMOKE: PASS")
    print("Confirmed: process, database, security, owner-inbox configuration, enquiry table, payment-evidence table.")
    print("Scope: read-only GET requests; no customer data read, enquiry submitted, order created, or payment changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
