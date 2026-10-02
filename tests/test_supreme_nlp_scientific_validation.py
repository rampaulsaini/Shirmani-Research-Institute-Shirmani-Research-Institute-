import unittest
from factory.supreme_nlp_scientific_validation import classification_metrics, validate_record, canonical_hash

class ScientificValidationTests(unittest.TestCase):
    def test_metrics_are_bounded(self):
        rows=[{"expected":"a","predicted":"a"},{"expected":"b","predicted":"a"},{"expected":"b","predicted":"b"}]
        m=classification_metrics(rows)
        self.assertAlmostEqual(m["accuracy"],2/3)
        for v in m.values():
            self.assertGreaterEqual(v,0)
            self.assertLessEqual(v,1)

    def test_missing_protocol_blocks(self):
        self.assertEqual(validate_record({})["status"],"BLOCKED")

    def test_verified_requires_independent_reviewer(self):
        record={
          "claim_id":"SNLV3-001","claim":"testable claim","operational_definition":"measured outcome",
          "preregistration":{"protocol_id":"p1","locked_before_test":True},
          "dataset":{"dataset_id":"d1","dataset_hash":"a"*64,"test_split_id":"test"},
          "protocol":{"version":"1","primary_metric":"accuracy","baseline":"0.5"},
          "metrics":{"sample_count":10,"result":0.8,"uncertainty":"bootstrap"},
          "counter_evidence":{"reviewed":True,"summary":"reviewed"},
          "reproducibility":{"environment":"python","command":"unittest","result_hash":canonical_hash({"x":1})},
          "independent_review":{"status":"VERIFIED"}
        }
        out=validate_record(record)
        self.assertIn("VERIFIED_REVIEWER_MISSING",out["errors"])
        self.assertFalse(out["eligible_for_review"])

if __name__=="__main__":
    unittest.main()
