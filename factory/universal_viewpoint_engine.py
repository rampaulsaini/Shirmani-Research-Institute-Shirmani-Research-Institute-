#!/usr/bin/env python3
"""Deterministic UNIVERSAL_VIEWPOINT_ENGINE gate.

This engine is a processing contract, not a claim that one philosophical
viewpoint has been scientifically established as universally true.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"universal-viewpoint-engine.json"

REQUIRED=[
    "संपूर्ण संतुष्टि की निरंतरता",
    "खुद के स्थाई स्वरुप से रुबरु",
    "खुद के स्थाई परिचय से परिचित",
    "निष्पक्ष समझ",
    "खुद का निरीक्षण"
]

def validate(x):
    assert x["stage"]=="UNIVERSAL_VIEWPOINT_ENGINE"
    assert x["viewpoint"]=="हृदय का शिरोमणि स्वरुप दृष्टिकोण"
    assert all(p in x["principles"] for p in REQUIRED)
    proc=x["processing"]
    assert all(proc.get(k) for k in ("human_meaning","external_claims","comparison","verification"))
    integrity=x["integrity"]
    assert integrity["universal_fact_claimed"] is False
    assert integrity["scientific_certainty_invented"] is False
    assert integrity["human_agency_preserved"] is True
    return True

if __name__=="__main__":
    x=json.loads(OUT.read_text(encoding="utf-8"))
    validate(x)
    print("UNIVERSAL VIEWPOINT ENGINE: PASS")
