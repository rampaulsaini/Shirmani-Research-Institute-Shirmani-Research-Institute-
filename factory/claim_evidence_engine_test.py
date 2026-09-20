#!/usr/bin/env python3
"""Regression tests for the canonical claim/evidence normalization contract."""
from factory.claim_evidence_engine import normalize_claim


def main():
    row = normalize_claim({"id": "test:1", "claim": "एक परीक्षण दावा"})
    assert row["verification"]["status"] == "UNVERIFIED"
    assert row["status"] == "NOT_VERIFIED"

    row = normalize_claim({
        "id": "test:2",
        "claim": "एक और दावा",
        "status": "SUPPORTED",
        "verification": {"status": "UNVERIFIED", "method": "NOT_RUN"},
    })
    assert row["status"] == "NOT_VERIFIED"

    row = normalize_claim({
        "id": "test:3",
        "claim": "स्वचालित परीक्षण से सत्यापित दावा",
        "status": "SUPPORTED",
        "verification": {"status": "AUTOMATED_CHECK", "method": "REGRESSION_TEST"},
    })
    assert row["status"] == "SUPPORTED"

    print("CLAIM/EVIDENCE ENGINE TEST: PASS")


if __name__ == "__main__":
    main()
