#!/usr/bin/env python3
import json
from pathlib import Path

spec = json.loads(Path("federation/research-paper-evidence-intake-spec.json").read_text(encoding="utf-8"))
source = json.loads(Path("federation/research-paper-source-intake.json").read_text(encoding="utf-8"))
claims = json.loads(Path("generated/research-paper-claims.json").read_text(encoding="utf-8"))["claims"]

assert spec["source"] == "federation/research-paper-source-intake.json"
assert spec["claims"] == "generated/research-paper-claims.json"
assert len(claims) == 5
assert spec["fixed_values"]["verification_status"] == "UNVERIFIED"
assert spec["fixed_values"]["independent_verification_required"] is True
assert spec["fixed_values"]["promotion_status"] == "BLOCKED_PENDING_INDEPENDENT_VERIFICATION"
assert source["verification_status"] == "UNVERIFIED"
print("Research Paper evidence intake contract: PASS")
