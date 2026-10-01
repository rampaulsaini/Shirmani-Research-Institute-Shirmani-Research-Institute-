"""Contract tests for the Supreme evidence-fusion layer."""
from __future__ import annotations
import json
from pathlib import Path
from agents.supreme_signal_fusion import ObservedSignal, fuse

def main() -> None:
    signals = [
        ObservedSignal("plant", "electrical", "x", 1.0, 1.0, "s1", "2026-10-01T00:00:00Z"),
        ObservedSignal("plant", "vibration", "y", 0.95, 1.0, "s2", "2026-10-01T00:00:01Z"),
        ObservedSignal("environment", "temperature", "z", 0.98, 0.9, "s3", "2026-10-01T00:00:02Z"),
    ]
    out = fuse(signals, {"mode": "contract_test"})
    assert out["status"] == "EVIDENCE_SUPPORTED_INTERPRETATION"
    assert 0.0 <= out["inference"]["confidence"] <= 1.0
    assert out["verification"]["status"] == "UNVERIFIED"
    assert out["verification"]["independent_verification_required"] is True
    assert out["governance"]["fail_closed"] is True
    assert out["governance"]["subjective_experience_claim_allowed"] is False
    assert out["provenance"]["signal_fingerprint"]
    empty = fuse([])
    assert empty["status"] == "INSUFFICIENT_DATA"
    assert empty["inference"]["confidence"] == 0.0
    schema = json.loads(Path("schemas/supreme-signal-fusion.schema.json").read_text(encoding="utf-8"))
    assert schema["title"] == "Supreme Signal Fusion Record"
    print("SUPREME_SIGNAL_FUSION_CONTRACT: PASS")

if __name__ == "__main__":
    main()
