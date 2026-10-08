import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "generated" / "shirmani-live-character-v10-contract.json"
V10 = ROOT / "shirmani-supreme-live-character-v10.html"
V5 = ROOT / "shirmani-live-character-v5.html"

def test_v10_contract_and_entry_chain_are_consistent():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    page = V10.read_text(encoding="utf-8")
    entry = V5.read_text(encoding="utf-8")
    assert contract["version"] == "V10"
    assert contract["canonical_surface"] == V10.name
    assert contract["entry_chain"] == "index.html -> shirmani-live-character-v5.html -> V10"
    assert V10.name in entry
    assert contract["pipeline"] == ["Voice", "Authorized Voice", "Context", "Evidence", "Reasoning", "Answer", "Face", "Gaze", "Lip Timing", "Live", "Audit", "Improve"]
    gates = contract["gates"]
    assert gates["authorized_voice"] == "explicit authorization required"
    assert gates["avatar"] == "authorized asset"
    assert gates["independent_verification"] == "separate artifact"
    assert gates["production_ai_nlp"] == "secure server-side endpoint"
    assert "Verification: NOT_VERIFIED" in page
    assert "independently verified scientific fact" in page

def test_v10_does_not_insert_source_url_with_innerhtml():
    page = V10.read_text(encoding="utf-8")
    assert "innerHTML" not in page
    assert "createElement" in page

def test_v10_source_boundary_is_documented_as_not_evaluated():
    page = V10.read_text(encoding="utf-8")
    assert "NOT EVALUATED" in page or "NOT_EVALUATED" in page or "not automatically" in page
    assert "Verification: NOT_VERIFIED" in page
