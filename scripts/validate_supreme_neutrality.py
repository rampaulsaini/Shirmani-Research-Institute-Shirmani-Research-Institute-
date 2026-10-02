from agents.supreme_neutrality import build_neutrality_record

rows = [
    {"modality":"synthetic","feature":"signal_a","value":1.0,"quality":1.0},
    {"modality":"synthetic","feature":"signal_b","value":0.8,"quality":0.9},
]
record = build_neutrality_record(rows, "neutrality-contract")
g, v = record["governance"], record["verification"]
assert g["neutrality"] and g["equal-treatment"] and g["evidence-first"]
assert g["subjective-experience-claim-allowed"] is False and g["fail_closed"] is True
assert v["independent_verification_required"] is True
assert record["interpretation"]["statement_type"] == "OBSERVED"
assert 0 <= record["interpretation"]["confidence"] <= 1
assert record["fingerprint"]
print("SUPREME_NEUTRALITY_CONTRACT_OK")
