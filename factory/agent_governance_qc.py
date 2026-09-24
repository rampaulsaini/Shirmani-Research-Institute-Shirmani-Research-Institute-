#!/usr/bin/env python3
"""Runtime QC for the multi-layer AI-agent governance contract.

This validator is intentionally deterministic and fail-closed. It validates the
machine-readable policy and any supplied AgentOutput-like JSON records without
executing agent code or performing external side effects.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "schemas" / "agent-governance.json"

REQUIRED_LAYERS = {
    "intake_source",
    "reasoning",
    "evidence",
    "verification",
    "product",
    "marketing",
    "economic_transaction",
    "security_audit",
    "publishing",
    "continuity",
}
ALLOWED_STATUS = {"source-backed", "user-authored", "hypothesis", "unverified", "verified"}


def fail(message: str) -> None:
    raise SystemExit(f"AGENT-GOVERNANCE-QC: BLOCK: {message}")


def main() -> int:
    try:
        policy = json.loads(POLICY.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot read governance policy: {exc}")

    if policy.get("fail_closed") is not True:
        fail("fail_closed must be true")
    if policy.get("default_status") != "unverified":
        fail("default_status must be unverified")
    if set(policy.get("agent_layers", [])) != REQUIRED_LAYERS:
        fail("agent layer set is incomplete or contains unexpected layers")

    auth = policy.get("authorization", {})
    if auth.get("irreversible_actions") != "owner_authorization_required":
        fail("irreversible actions are not owner-authorized")
    if auth.get("financial_actions") != "explicit_integration_and_authorization_required":
        fail("financial actions are not explicitly authorized")
    if auth.get("verification_promotion") != "independent_verification_required":
        fail("verification promotion is not independently verified")

    if policy.get("provenance_required_for_claims") is not True:
        fail("claims do not require provenance")
    if policy.get("fabrication_prohibited") is not True:
        fail("fabrication prohibition is disabled")
    if policy.get("secret_handling") != "secret_store_only":
        fail("secret handling is not secret-store-only")
    if policy.get("public_surface_may_expose_secrets") is not False:
        fail("public surfaces may expose secrets")

    if "--self-test" in sys.argv[1:]:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp) / "valid-agent-output.json"
            tmp_path.write_text(json.dumps({
                "status": "verified",
                "agent_layer": "verification",
                "provenance": {
                    "source_repository": "test/repository",
                    "source_path": "source.txt",
                    "source_sha256": "a" * 64,
                    "generated_at": "1970-01-01T00:00:00Z",
                    "status": "verified"
                },
                "verification_record": {"method": "independent-test"},
                "external_side_effects": False
            }), encoding="utf-8")
            record_paths = [tmp_path]
    else:
        record_paths = [Path(p) for p in sys.argv[1:]]

    # Optional deterministic validation of generated AgentOutput-like records.
    # The validator never upgrades status and never treats missing provenance as verified.
    record_paths = [Path(p) for p in sys.argv[1:]]
    checked = 0
    for path in record_paths:
        if not path.is_absolute():
            path = ROOT / path
        if not path.is_file():
            fail(f"record does not exist: {path}")
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"invalid JSON record {path}: {exc}")

        records = payload if isinstance(payload, list) else [payload]
        for record in records:
            checked += 1
            status = record.get("status", "unverified")
            if status not in ALLOWED_STATUS:
                fail(f"invalid status {status!r} in {path}")
            layer = record.get("agent_layer")
            if layer is not None and layer not in REQUIRED_LAYERS:
                fail(f"unknown agent layer {layer!r} in {path}")
            if status == "verified":
                provenance = record.get("provenance")
                if not provenance:
                    fail(f"verified record lacks provenance: {path}")
                if not record.get("verification_record"):
                    fail(f"verified record lacks verification_record: {path}")

            if record.get("external_side_effects") and record.get("requires_human_authorization") is not True:
                fail(f"external side effects require human authorization: {path}")

    print(f"AGENT-GOVERNANCE-QC: PASS (policy + {checked} optional records checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
