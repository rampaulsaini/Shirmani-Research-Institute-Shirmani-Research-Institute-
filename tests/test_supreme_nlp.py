from agents.supreme_nlp import Signal, translate, make_record
from agents.automission_engine import run_cycle, publish_gate


def test_signal_translation_is_conservative():
    r = translate([Signal("voltage", 1.0, "mV"), Signal("voltage", 1.05, "mV")])
    assert 0 <= r.confidence <= 1
    assert "प्रत्यक्ष प्रमाण" in " ".join(r.limitations)


def test_record_is_hashed():
    r = make_record([Signal("temperature", 25.0, "C")])
    assert len(r["record_sha256"]) == 64


def test_publish_requires_independent_verification():
    r = run_cycle({"evidence": ["sensor:001"]})
    ok, errors = publish_gate(r)
    assert not ok
    assert "NOT_INDEPENDENTLY_VERIFIED" in errors
