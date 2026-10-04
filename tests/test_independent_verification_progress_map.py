import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/generate_independent_verification_progress_map.py"
OUT_JSON = ROOT / "generated/independent-verification-progress.json"


def test_target_capacity_is_distinct_from_instantiated_queue():
    ns = runpy.run_path(str(SCRIPT))
    ns["main"]()

    report = json.loads(OUT_JSON.read_text(encoding="utf-8"))
    authoritative = report["authoritative"]
    instantiated = report["instantiated_review_layer"]

    assert report["authoritative_target"] == 100200
    assert authoritative["registered_target_capacity"] == 100200
    assert authoritative["target_capacity_is_not_instantiated_queue"] is True
    assert authoritative["queued"] == 100200
    assert authoritative["reviewed"] == 0
    assert authoritative["verified"] == 0

    assert instantiated["claim_records"] == 10
    assert instantiated["instantiated_queue_records"] == 10
    assert instantiated["review_slots"] == 10
    assert instantiated["verified"] == 0

    assert instantiated["review_slot_coverage_percent"] == 100.0
    assert instantiated["verified_percent_of_instantiated"] == 0.0
    assert authoritative["verified_percent"] == 0.0
    assert authoritative["remaining_to_target"] == 100200
    assert report["policy"]["scales_must_not_be_conflated"] is True
    assert report["policy"]["independent_reviewer_decision_required"] is True
