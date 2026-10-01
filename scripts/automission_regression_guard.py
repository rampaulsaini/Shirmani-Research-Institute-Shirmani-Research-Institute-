import json, os, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
current=ROOT/"automission-benchmark-report.json"
baseline=ROOT/"docs/yatharth-governance/automission-baseline.json"

def main():
    cur=json.loads(current.read_text(encoding="utf-8"))
    if not baseline.exists():
        print("No baseline: regression comparison is unavailable; fail-closed.")
        raise SystemExit(2)
    base=json.loads(baseline.read_text(encoding="utf-8"))
    if base.get("fixture_sha256") != cur.get("fixture_sha256"):
        print("Baseline fixture differs from current fixture; explicit baseline refresh required.")
        raise SystemExit(2)
    cm=cur["metrics"]; bm=base["metrics"]
    rules={
      "accuracy": cm["accuracy"]-bm["accuracy"] >= -0.02,
      "f1_macro": cm["f1_macro"]-bm["f1_macro"] >= -0.02,
      "brier_score": cm["brier_score"]-bm["brier_score"] <= 0.02,
      "provenance_completeness": cm["provenance_completeness"]-bm["provenance_completeness"] >= 0.0,
      "coverage": cm["coverage"]-bm["coverage"] >= -0.05,
    }
    print(json.dumps({"baseline":base.get("commit_sha","unknown"),"current":cur.get("fixture_sha256"),"checks":rules},indent=2))
    if not all(rules.values()):
        raise AssertionError("CRITICAL_REGRESSION")
    print("Automission regression guard: PASS")
if __name__=="__main__":
    try: main()
    except (AssertionError, FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Automission regression guard: FAIL: {e}",file=sys.stderr); raise
