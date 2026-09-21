#!/usr/bin/env python3
"""Deterministic self-realization formulation gate.

This preserves the project's philosophical formulation without converting
phenomenological language into unsupported scientific or physiological proof.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"self-realization-formulation.json"

REQUIRED=[
    "निष्पक्ष समझ","खुद का निरीक्षण","परिभाषा स्पष्ट करना",
    "दावे और अनुभव को अलग पहचानना","स्रोत और evidence दर्ज करना",
    "countercase खोजना","स्वतंत्र verification जहाँ संभव हो"
]

def validate(x):
    assert x["stage"]=="SELF_REALIZATION_FORMULATION"
    assert x["viewpoint"]=="हृदय का शिरोमणि स्वरुप दृष्टिकोण"
    f=x["formulation"]
    assert "संपूर्ण संतुष्टि की निरंतरता" in f["continuity"]
    assert all(item in f["method"] for item in REQUIRED)
    i=x["integrity"]
    assert i["scientific_proof_invented"] is False
    assert i["physiological_proof_invented"] is False
    assert i["verification_required_for_external_claims"] is True
    return True

if __name__=="__main__":
    x=json.loads(OUT.read_text(encoding="utf-8"))
    validate(x)
    print("SELF REALIZATION FORMULATION: PASS")
