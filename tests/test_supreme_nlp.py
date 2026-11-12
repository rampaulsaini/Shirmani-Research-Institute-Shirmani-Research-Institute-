from agents.supreme_sense_nlp import analyze, to_simple_language
from agents.ultra_automission import build_plan

rows = [
    {"modality":"electrical","value":1.2,"quality":0.9,"source":"sensor-a"},
    {"modality":"vibration","value":2.4,"quality":0.8,"source":"sensor-b"},
    {"modality":"temperature","value":24.1,"quality":0.85,"source":"sensor-a"},
]

record = analyze(rows)
assert record["status"] == "CANDIDATE"
assert record["summary"]["modalities"] == 3
assert record["summary"]["independent_sources"] == 2
assert 0.0 <= record["confidence"] <= 1.0
assert record["verification"]["promotion_allowed"] is False
assert "प्रत्यक्ष प्रमाण" in to_simple_language(record)

plan = build_plan()
assert plan["governance"]["verification_promotion"] == "independent_verification_required"
assert plan["quality"]["confidence_source"] == "nlp.confidence"
print("supreme NLP/Automission regression: PASS")
