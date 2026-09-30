import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
paths=[
ROOT/"docs/yatharth-governance/automission-quality-gate.json",
ROOT/"docs/yatharth-governance/automission-benchmark-manifest.json",
ROOT/"docs/yatharth-governance/supreme-automission-contract.json",
]

def main():
    for p in paths:
        assert p.exists(), f"missing contract: {p}"
    q=json.loads(paths[0].read_text(encoding="utf-8"))
    m=json.loads(paths[1].read_text(encoding="utf-8"))
    s=json.loads(paths[2].read_text(encoding="utf-8"))
    assert q["status"]["independent_verified_claims"]==0 and q["status"]["live_claim"] is False
    assert m["release_policy"]["independent_verified_claims"]==0 and m["release_policy"]["live_claim"] is False
    assert s["truth_boundary"]["independent_verified_claims"]==0 and s["truth_boundary"]["live_claim"] is False
    print("Supreme release boundary: PASS (fail-closed)")
if __name__=="__main__":
    main()
