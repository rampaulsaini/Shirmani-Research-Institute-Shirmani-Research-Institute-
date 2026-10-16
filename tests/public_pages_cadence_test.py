"""Guard the Pages rebuild cadence against unnecessary full production cycles."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "public-production-automission.yml"
SMOKE = ROOT / "factory" / "public_pages_runtime_smoke.py"
LEGACY_PUBLISHERS = (
    ROOT / ".github" / "workflows" / "github-pages.yml",
    ROOT / ".github" / "workflows" / "shirmani-multi-layer-production.yml",
)
CANONICAL_PUBLISHER = ROOT / ".github" / "workflows" / "public-production-automission.yml"


class PublicPagesCadenceTest(unittest.TestCase):
    def test_full_build_is_hourly_and_code_push_still_deploys(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn('cron: "17 * * * *"', workflow)
        self.assertNotIn('cron: "*/5 * * * *"', workflow)
        self.assertRegex(workflow, r"(?m)^  push:\n    branches: \[main\]")

    def test_only_canonical_workflow_deploys_pages(self):
        canonical = CANONICAL_PUBLISHER.read_text(encoding="utf-8")
        self.assertIn("actions/deploy-pages@v4", canonical)
        for path in LEGACY_PUBLISHERS:
            with self.subTest(path=path.name):
                legacy = path.read_text(encoding="utf-8")
                self.assertNotIn("actions/deploy-pages@", legacy)
                self.assertNotIn("pages: write", legacy)
                self.assertNotIn("id-token: write", legacy)

    def test_hourly_refresh_fits_runtime_freshness_window(self):
        smoke = SMOKE.read_text(encoding="utf-8")
        self.assertIn("age > 7200", smoke)
        self.assertIn("PAGES_RUNTIME_SMOKE_FAIL: stale/future deployed file", smoke)


if __name__ == "__main__":
    unittest.main()
