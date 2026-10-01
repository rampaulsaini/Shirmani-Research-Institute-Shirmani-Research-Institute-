import unittest
from scripts.automission_control_plane import (
    AgentVote, UNKNOWN, DETERMINISTIC, ESCALATE_REVIEW, QUARANTINE,
    audit_record, detect_drift, recover, route_decision, validate_audit_chain,
)

class ControlPlaneTests(unittest.TestCase):
    def test_missing_evidence_fails_closed(self):
        r = route_decision(case_id="x", decision="SUPPORTED", confidence=.99, evidence_ids=[])
        self.assertEqual(r.decision, UNKNOWN)
        self.assertEqual(r.route, ESCALATE_REVIEW)

    def test_low_confidence_escalates(self):
        r = route_decision(case_id="x", decision="SUPPORTED", confidence=.69, evidence_ids=["e1"])
        self.assertEqual(r.route, ESCALATE_REVIEW)

    def test_disagreement_cannot_create_certainty(self):
        r = route_decision(
            case_id="x", decision="SUPPORTED", confidence=.95, evidence_ids=["e1"],
            votes=[AgentVote("a","SUPPORTED",.95), AgentVote("b","UNSUPPORTED",.94)]
        )
        self.assertEqual(r.decision, UNKNOWN)
        self.assertTrue(r.disagreement)

    def test_consensus_routes(self):
        r = route_decision(
            case_id="x", decision="SUPPORTED", confidence=.95, evidence_ids=["e1"],
            votes=[AgentVote("a","SUPPORTED",.95), AgentVote("b","SUPPORTED",.94)]
        )
        self.assertEqual(r.decision, "SUPPORTED")
        self.assertEqual(r.route, DETERMINISTIC)

    def test_drift_and_recovery(self):
        self.assertEqual(detect_drift({"x":100},{"x":130})["action"], QUARANTINE)
        self.assertEqual(recover(0)["action"], "RETRY")
        self.assertEqual(recover(2)["action"], QUARANTINE)
        self.assertEqual(recover(0, idempotent=False)["action"], QUARANTINE)

    def test_hash_chain_detects_tamper(self):
        d1 = route_decision(case_id="a", decision="SUPPORTED", confidence=.9, evidence_ids=["e1"])
        a = audit_record(event_id="1", component="t", model_version="m", policy_version="p",
                         input_value={"x":1}, decision=d1, latency_ms=2)
        d2 = route_decision(case_id="b", decision="SUPPORTED", confidence=.9, evidence_ids=["e2"])
        b = audit_record(event_id="2", component="t", model_version="m", policy_version="p",
                         input_value={"x":2}, decision=d2, latency_ms=3, previous_hash=a["record_hash"])
        self.assertTrue(validate_audit_chain([a,b]))
        b["decision"] = "TAMPERED"
        self.assertFalse(validate_audit_chain([a,b]))

if __name__ == "__main__":
    unittest.main()
