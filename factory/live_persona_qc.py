#!/usr/bin/env python3
"""Deterministic QC for the SHIRMANI Live Persona contract."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "live-persona.schema.json"
STATUS = ROOT / "generated" / "live-persona-status.json"
REQUIRED = ["schema_version","identity","persona","voice","qa","visual","verification","status"]

def main():
    if not SCHEMA.exists():
        print("FAIL: missing live persona schema")
        return 1
    if not STATUS.exists():
        print("FAIL: missing live persona status")
        return 1
    try:
        json.loads(SCHEMA.read_text(encoding="utf-8"))
        data = json.loads(STATUS.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: invalid JSON: {exc}")
        return 1
    missing = [k for k in REQUIRED if k not in data]
    if missing:
        print("FAIL: missing required fields:", ", ".join(missing))
        return 1
    if data["identity"]["display_name"] != "शिरोमणि रामपॉल सैनी":
        print("FAIL: canonical display name mismatch")
        return 1
    if data["qa"]["insufficient_evidence_response"] != "अभी पर्याप्त प्रमाण उपलब्ध नहीं है":
        print("FAIL: evidence insufficiency response mismatch")
        return 1
    if data["voice"]["authorization_state"] == "AUTHORIZED" and not data["voice"].get("provider"):
        print("FAIL: authorized voice requires provider metadata")
        return 1
    if data["voice"]["integration_state"] == "LIVE" and data["voice"]["authorization_state"] != "AUTHORIZED":
        print("FAIL-CLOSED: LIVE voice requires authorization")
        return 1
    if data["visual"]["lip_sync_state"] == "PASS" and data["visual"]["timing_state"] != "PASS":
        print("FAIL: lip-sync PASS requires timing PASS")
        return 1
    print("PASS: SHIRMANI Live Persona deterministic contract checks")
    print("NOTE: independent scientific/identity verification remains a separate state.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
