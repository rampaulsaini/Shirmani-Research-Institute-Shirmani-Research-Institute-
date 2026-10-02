import json
from pathlib import Path
from agents.supreme_sense_nlp import analyze,to_simple_language
rows=[{"modality":"electrical","feature":"signal","value":1.0,"quality":1.0,"source":"synthetic"},{"modality":"vibration","feature":"signal","value":0.9,"quality":0.9,"source":"synthetic"},{"modality":"unknown","feature":"noise","value":4,"quality":1.0,"source":"synthetic"}]
r=analyze(rows)
assert r["status"]=="CANDIDATE"
assert r["verification"]["promotion_allowed"] is False
assert r["verification"]["independent_verification_required"] is True
assert r["interpretation"]["subjective_experience_proven"] is False
assert 0<=r["confidence"]<=1 and len(r["fingerprint"])==64
assert "प्रत्यक्ष प्रमाण" in to_simple_language(r)
json.loads(Path("schemas/supreme-sense-nlp.schema.json").read_text(encoding="utf-8"))
print("SUPREME_SENSE_NLP_CONTRACT: PASS")
