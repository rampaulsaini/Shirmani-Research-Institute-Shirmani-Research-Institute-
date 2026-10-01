import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"generated/automission-feedback.json"
x=json.loads(p.read_text(encoding="utf-8"))
assert x["feedback_mode"]=="bounded_human_review"
s=x["safety_boundary"]
assert s["automatic_source_mutation"] is False
assert s["automatic_retry"] is False
assert s["failure_group_is_not_root_cause"] is True
assert s["repair_is_not_fixed_until_retest"] is True
for item in x["feedback_items"]:
    assert item["recommended_action"]=="inspect_and_patch_then_retest"
    assert item["automatic_source_mutation"] is False
    assert item["requires_subsequent_green_run"] is True
print("Automission feedback contract: PASS")
