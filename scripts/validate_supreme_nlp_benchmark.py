#!/usr/bin/env python3
"""Contract validator for the measurable Supreme NLP benchmark."""
from pathlib import Path
import json
REPORT=Path("generated/supreme-nlp/benchmark.json")
def main():
    d=json.loads(REPORT.read_text(encoding="utf-8"))
    m=d["metrics"]
    assert {"status_accuracy","state_accuracy","reproducibility","governance_boundary","mean_latency_ms","cases"} <= set(m)
    assert m["cases"] >= 4
    assert 0 <= m["status_accuracy"] <= 1
    assert 0 <= m["state_accuracy"] <= 1
    assert m["reproducibility"] is True
    assert m["governance_boundary"] is True
    assert d["status"] == "PASS"
    print("SUPREME_NLP_MEASURABLE_BENCHMARK=PASS")
if __name__=="__main__":
    main()
