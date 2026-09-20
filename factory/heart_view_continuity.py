#!/usr/bin/env python3
"""Deterministic HEART_VIEW_CONTINUITY gate.

The gate preserves the project's philosophical vocabulary and continuity
language while preventing unsupported physiological or scientific upgrades.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"heart-view-continuity.json"

REQUIRED=[
    "निष्पक्ष समझ",
    "शमीकरण",
    "यथार्थ सिद्धांत",
    "उपलब्धि यथार्थ युग",
    "हृदय का शिरोमणि स्वरुप दृष्टिकोण",
    "संपूर्ण संतुष्टि की निरंतरता",
    "खुद के स्थाई स्वरुप से रुबरु",
    "खुद के स्थाई परिचय से परिचित"
]

def validate(x):
    assert x["stage"]=="HEART_VIEW_CONTINUITY"
    assert x["state"]=="HEART_VIEW_FRAMEWORK"
    assert x["epistemic_status"] in {"FRAMEWORK_DESCRIPTION","USER_REPORTED_EXPERIENCE","NOT_VERIFIED"}
    assert x["integrity"]["physiological_claims_invented"] is False
    assert x["integrity"]["evidence_upgraded"] is False
    text=" ".join([x["framework"],x["continuity"],x["viewpoint"],*x["recognition"]])
    assert all(term in text for term in REQUIRED)
    return True

if __name__=="__main__":
    data=json.loads(OUT.read_text(encoding="utf-8"))
    validate(data)
    print("HEART VIEW CONTINUITY: PASS")
