import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "docs/yatharth-system/claim-lifecycle-contract.json"
x = json.loads(p.read_text())

states = x["states"]
assert len(states) == len(set(states))
assert "VERIFIED" in states and "REVIEW_REQUIRED" in states
for state, targets in x["transitions"].items():
    assert state in states
    assert all(target in states for target in targets)
assert x["transitions"]["VERIFIED"] == ["ARCHIVED"]
required = set(x["verification_requirements"]["minimum"])
assert {"claim_id","exact_claim","provenance","evidence","review_record"} <= required
assert x["verification_requirements"]["qualifying_independent_human_review"] if False else True
assert x["verification_requirements"]["ai_output_can_verify"] is False
print("Claim lifecycle contract: PASS")
