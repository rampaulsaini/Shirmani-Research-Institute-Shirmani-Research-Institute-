#!/usr/bin/env python3
"""Validate the public Yatharth feature-status contract without external dependencies."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/yatharth-system/feature-status-registry.json"
ALLOWED = {"LIVE", "BETA", "ARCHITECTURE", "RESEARCH", "REVIEW_REQUIRED", "DISABLED"}
REQUIRED = {
    "public_platform", "accounts_profiles", "social_publishing", "marketplace",
    "freelancing", "employment", "education", "yatharth_ai", "yatharth_ai_music",
    "research_institute", "independent_verification", "automission",
    "governance_control_plane", "nature_protection", "digital_store",
    "yatharth_economy", "yatharth_justice",
}

def fail(message):
    raise SystemExit("STATUS CONTRACT FAILED: " + message)

if not REGISTRY.exists():
    fail(f"missing registry: {REGISTRY}")

try:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
except json.JSONDecodeError as exc:
    fail(f"invalid JSON: {exc}")

if data.get("truth_rule") != "architecture_is_not_deployment":
    fail("truth_rule must remain architecture_is_not_deployment")

domains = data.get("domains")
if not isinstance(domains, dict):
    fail("domains must be an object")

missing = sorted(REQUIRED - set(domains))
if missing:
    fail("missing required domains: " + ", ".join(missing))

invalid = sorted((name, value) for name, value in domains.items() if value not in ALLOWED)
if invalid:
    fail("invalid capability status: " + repr(invalid))

verification = data.get("verification")
if not isinstance(verification, dict):
    fail("verification must be an object")

verified = verification.get("independent_verified_claims")
if not isinstance(verified, int) or isinstance(verified, bool) or verified < 0:
    fail("independent_verified_claims must be a non-negative integer")

if verification.get("rule") != "increase only after qualifying independent human review is recorded":
    fail("verification rule changed unexpectedly")

if domains.get("independent_verification") != "REVIEW_REQUIRED" and verified == 0:
    fail("independent verification cannot advertise a stronger state while verified count is zero")

print(f"STATUS CONTRACT OK: {len(domains)} domains; independent_verified_claims={verified}")
