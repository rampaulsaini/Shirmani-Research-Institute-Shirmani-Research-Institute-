#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from factory.signal_to_nlp import interpret

def main():
    r=interpret({"signal_id":"smoke-001","observations":{
        "temperature":[20.0,21.0,22.0],
        "electrical_signal":[0.1,0.2,0.15],
        "environment":"controlled-smoke-test"}})
    assert r["signal_id"]=="smoke-001"
    assert 0 <= r["confidence"] <= 1
    assert r["evidence_level"]=="derived_pattern"
    assert len(r["provenance"]["input_hash"])==64
    guard=" ".join(r["uncertainty"]).lower()
    assert "subjective feeling" in guard and "consciousness" in guard
    print("signal_to_nlp smoke test: PASS")

if __name__=="__main__":
    main()
