#!/usr/bin/env python3
"""Fail-closed checks for Yatharth Mudra protocol boundaries."""
import json
from pathlib import Path

p=json.loads(Path("federation/yatharth-mudra-protocol.json").read_text(encoding="utf-8"))
assert p["symbol"]=="YTH"
assert p["supply"]["max"]==1_000_000_000
assert p["supply"]["initial_supply"]==0
assert p["supply"]["production_minting_enabled"] is False
assert p["issuance_model"]["name"]=="Proof of Verified Contribution (PoVC)"
assert "HUMAN_APPROVAL" in p["issuance_model"]["required_sequence"]
assert p["anti_abuse"]["idempotency_key_required"] is True
assert p["anti_abuse"]["double_issuance_rejected"] is True
assert p["testnet"]["enabled_as_simulation_only"] is True
assert p["testnet"]["real_money"] is False
assert p["testnet"]["real_token_transfer"] is False
assert p["testnet"]["real_wallet_deployment"] is False
print("YTH protocol boundary: PASS (design/testnet simulation only)")
