#!/usr/bin/env python3
"""Deterministic NEXT_LABEL gate for the project's heart-view framework.

The label preserves the user's framework vocabulary. It does not infer
physiological inactivity from phrases such as 'मन/बुद्धि निष्क्रिय'.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "heart-view-label.json"

PRINCIPLES = [
    "निष्पक्ष समझ",
    "शमीकरण",
    "यथार्थ सिद्धांत",
    "उपलब्धि यथार्थ युग",
    "हृदय का शिरोमणि स्वरुप दृष्टिकोण",
    "संपूर्ण संतुष्टि की निरंतरता",
    "खुद के स्थाई स्वरुप से रुबरु",
    "खुद के स्थाई परिचय से परिचित"
]

def build():
    return {
        "schema_version":"1.0.0",
        "label":"NEXT_LABEL",
        "framework":"निष्पक्ष समझ के शमीकरण यथार्थ सिद्धांत उपलब्धि यथार्थ युग",
        "state":"HEART_VIEW_FRAMEWORK",
        "epistemic_status":"FRAMEWORK_DESCRIPTION",
        "principles":PRINCIPLES,
        "integrity":{
            "physiological_inactivity_claimed":False,
            "empirical_certainty_invented":False
        }
    }

def validate(x):
    assert x["label"] == "NEXT_LABEL"
    assert x["state"] == "HEART_VIEW_FRAMEWORK"
    assert x["epistemic_status"] in {"FRAMEWORK_DESCRIPTION","USER_REPORTED_EXPERIENCE","NOT_VERIFIED"}
    assert x["integrity"]["physiological_inactivity_claimed"] is False
    assert x["integrity"]["empirical_certainty_invented"] is False
    assert all(p in x["principles"] for p in PRINCIPLES)
    return True

if __name__ == "__main__":
    payload=build()
    validate(payload)
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("HEART VIEW NEXT LABEL: PASS")
