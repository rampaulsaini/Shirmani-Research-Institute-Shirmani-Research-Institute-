import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("audit",ROOT/"factory"/"supreme_independent_verification_audit.py")
M=importlib.util.module_from_spec(SPEC); assert SPEC.loader is not None; SPEC.loader.exec_module(M)

def test_states():
    assert "VERIFIED" in M.STATES
    assert "PROMOTED" not in M.STATES
    assert not M.has_verification_evidence({"verification_state":"UNVERIFIED"})
    assert M.has_verification_evidence({"verification_state":"VERIFIED","verification_evidence":{"review_id":"example"}})

if __name__=="__main__":
    test_states()
    print("SHIRMANI Independent Verification Audit Test: PASS")
