import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from master_automission import MasterAutomission

class MasterAutomissionTests(unittest.TestCase):
    def test_register_and_route_tasks(self):
        m = MasterAutomission()
        m.register("edu-1", "education", "curriculum", "create_course")
        m.register("pub-1", "publishing", "publisher", "publish", reversible=False)
        routed = m.route()
        self.assertEqual(routed[0]["status"], "QUEUED")
        self.assertEqual(routed[1]["status"], "APPROVAL_REQUIRED")

    def test_unknown_domain_rejected(self):
        with self.assertRaises(ValueError):
            MasterAutomission().register("x", "unknown", "agent", "work")

if __name__ == "__main__":
    unittest.main()
