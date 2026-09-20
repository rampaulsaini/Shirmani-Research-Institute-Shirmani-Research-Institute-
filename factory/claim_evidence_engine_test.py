#!/usr/bin/env python3
from factory.claim_evidence_engine import normalize_claim

def main():
    row=normalize_claim({"id":"test:1","claim":"एक परीक्षण दावा"})
    assert row["verification"]["status"]=="NOT_VERIFIED"
    assert row["conclusion"]=="NOT_VERIFIED"
    row=normalize_claim({"id":"test:2","claim":"एक और दावा",
                          "verification":{"status":"PASS","independent":False}})
    assert row["verification"]["status"]=="CHECK"
    print("CLAIM/EVIDENCE ENGINE TEST: PASS")

if __name__=="__main__":
    main()
