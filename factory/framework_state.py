#!/usr/bin/env python3
"""Deterministic framework-state contract.

This module preserves the project's heart-view/head-view vocabulary while
keeping phenomenological statements separate from physiological measurements.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "framework-state.json"

def validate(state):
    assert state["state"] in {"HEAD_DOMINANT","BALANCED","HEART_VIEW_FRAMEWORK","UNSPECIFIED"}
    assert state["epistemic_status"] in {"FRAMEWORK_DESCRIPTION","USER_REPORTED_EXPERIENCE","EMPIRICALLY_VERIFIED","NOT_VERIFIED"}
    integrity = state.get("integrity", {})
    assert integrity.get("physiological_inactivity_claimed") is False
    assert integrity.get("empirical_status_not_invented") is True
    return True

def main():
    state = json.loads(OUT.read_text(encoding="utf-8"))
    validate(state)
    print("FRAMEWORK STATE CONTRACT: PASS")
    print("State:", state["state"])
    print("Epistemic status:", state["epistemic_status"])
    print("Head activity:", state["measurement"]["head_activity"])
    print("Heart view:", state["measurement"]["heart_view"])

if __name__ == "__main__":
    main()
