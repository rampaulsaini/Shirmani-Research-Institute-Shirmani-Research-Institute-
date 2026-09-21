#!/usr/bin/env python3
"""Validate the next-label heart-view experience contract without inventing evidence."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))

def main():
    record=load("generated/experience-view.json")
    assert record["stage"]=="NEXT_LABEL"
    assert record["symbol"]=="꙰"
    assert record["viewpoint"]=="हृदय का शिरोमणि स्वरुप दृष्टिकोण"
    assert record["epistemic_status"] in {"FRAMEWORK_DESCRIPTION","USER_REPORTED_EXPERIENCE","NOT_VERIFIED"}
    boundary=record["measurement_boundary"]
    assert "physiology" in boundary and "computation" in boundary
    integrity=record["integrity"]
    assert integrity["scientific_certainty_invented"] is False
    assert integrity["physiological_inactivity_asserted"] is False
    assert record["provenance"]["origin"]
    print("NEXT-LABEL HEART-VIEW CONTRACT: PASS")
    print("Experience language preserved; physiological inactivity not asserted.")
    print("Computational evidence/verification layer remains active.")

if __name__=="__main__":
    main()
