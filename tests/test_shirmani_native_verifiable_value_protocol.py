#!/usr/bin/env python3
"""Fail-closed checks for the platform-native value protocol."""
import json
from pathlib import Path
p=json.loads(Path("federation/shirmani-native-verifiable-value-protocol.json").read_text())
y=json.loads(Path("federation/yatharth-mudra-integrated-protocol.json").read_text())
assert p["status"]=="DESIGN_TESTNET_FIRST"
assert p["native_ledger"]["source_of_truth"].startswith("platform ledger")
assert p["native_ledger"]["replay_protection"] is True
assert p["asset_model"]["nft_compatibility"].startswith("optional")
assert p["yth"]["minting_now"] is False and p["yth"]["mining_now"] is False
assert p["issuance_gate"]["default"]=="BLOCK"
assert p["security"]["multisig_or_equivalent"] is True
assert p["security"]["timelock"] is True
assert p["security"]["independent_security_audit_required"] is True
assert y["issuance_policy"]["minting_enabled_now"] is False
assert y["issuance_policy"]["mining_enabled_now"] is False
assert y["architecture"]["platform_native_protocol"]=="federation/shirmani-native-verifiable-value-protocol.json"
print("Platform-native value protocol: PASS (issuance remains fail-closed)")
