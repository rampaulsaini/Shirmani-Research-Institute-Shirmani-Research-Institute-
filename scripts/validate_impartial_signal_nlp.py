import json
from agents.impartial_signal_nlp import build_record
rows=[{"feature":"baseline_a","value":1.0,"quality":1.0,"source":"contract-test"},
      {"feature":"baseline_b","value":0.8,"quality":1.0,"source":"contract-test"}]
r=build_record(rows,"contract-test")
assert r["governance"]["impartiality"] is True
assert r["governance"]["fail_closed"] is True
assert r["governance"]["subjective_experience_claim_allowed"] is False
assert r["governance"]["self_verification_allowed"] is False
assert r["interpretation"]["evidence_status"] == "OBSERVATIONAL"
assert len(r["fingerprint"]) == 64
print("IMPARTIAL_SIGNAL_NLP_CONTRACT_OK")
