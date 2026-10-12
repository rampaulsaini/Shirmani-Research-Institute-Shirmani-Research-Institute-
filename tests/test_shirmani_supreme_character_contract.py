"""Contract tests for the approved SHIRMANI SUPREME character brief.

These tests validate that the public specification preserves the owner's
identity lock and evidence boundaries. They do not prove live integrations.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BRIEF = ROOT / "docs/production/SHIRMANI-SUPREME-FINAL-CHARACTER-BRIEF-2026-10-12.md"
DECISION = ROOT / "docs/production/SHIRMANI-SUPREME-APPROVED-CHARACTER-DECISION-2026-10-12.md"
STUDIO = ROOT / "showroom/heart-view-character-studio.html"

class CharacterContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.brief = BRIEF.read_text(encoding="utf-8")
        cls.decision = DECISION.read_text(encoding="utf-8")
        cls.studio = STUDIO.read_text(encoding="utf-8")

    def test_original_photo_is_locked(self):
        for text in (self.brief, self.decision):
            self.assertIn("original photo", text.lower())
            self.assertIn("proportional resizing", text.lower())
            self.assertIn("PHOTO ASSET REQUIRED", text)
            self.assertIn("regeneration", text.lower())

    def test_voice_requires_authorised_asset_and_test(self):
        self.assertIn("VOICE ASSET REQUIRED", self.brief)
        self.assertIn("end-to-end test", self.brief)
        self.assertIn("authorised voice", self.brief.lower())

    def test_exact_uncertainty_notice_is_present(self):
        self.assertIn("अभी पर्याप्त प्रमाण उपलब्ध नहीं है।", self.brief)
        self.assertIn("अभी पर्याप्त प्रमाण उपलब्ध नहीं है।", self.studio)

    def test_personal_philosophy_is_separated_from_evidence(self):
        self.assertIn("PHILOSOPHICAL / PERSONAL PERSPECTIVE", self.brief)
        self.assertIn("INDEPENDENTLY VERIFIED", self.brief)
        self.assertIn("SOURCE-BASED", self.brief)

    def test_product_media_must_be_real_or_labelled_pending(self):
        for phrase in ("STORYBOARD — NOT RECORDED", "ILLUSTRATIVE MOCK-UP",
                       "unique QR", "usage guide", "dated QC state"):
            self.assertIn(phrase, self.brief)

    def test_no_claim_of_deleted_chat_restoration(self):
        self.assertIn("deleted ChatGPT conversation", self.brief)
        self.assertIn("not restored", self.brief.lower())

    def test_studio_exposes_four_capability_versions(self):
        for phrase in ("V1 — Clear Script", "V2 — Voice", "V3 — Avatar", "V4 — Live Presenter"):
            self.assertIn(phrase, self.studio)

if __name__ == "__main__":
    unittest.main(verbosity=2)
