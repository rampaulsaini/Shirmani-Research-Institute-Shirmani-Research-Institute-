"""Guard the Pages rebuild cadence against unnecessary full production cycles."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "public-production-automission.yml"
SMOKE = ROOT / "factory" / "public_pages_runtime_smoke.py"


class PublicPagesCadenceTest(unittest.TestCase):
    def test_full_build_is_hourly_and_code_push_still_deploys(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn('cron: "17 * * * *"', workflow)
        self.assertNotIn('cron: "*/5 * * * *"', workflow)
        self.assertRegex(workflow, r"(?m)^  push:\n    branches: \[main\]")

    def test_hourly_refresh_fits_runtime_freshness_window(self):
        smoke = SMOKE.read_text(encoding="utf-8")
        self.assertIn("age > 7200", smoke)
        self.assertIn("PAGES_RUNTIME_SMOKE_FAIL: stale/future deployed file", smoke)


if __name__ == "__main__":
    unittest.main()
