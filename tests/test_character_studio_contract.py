"""Static acceptance checks for the SHIRMANI SUPREME Character Studio.

These checks guard the page's honesty/asset contract and key local-workbench hooks.
They do not replace browser, accessibility, provider, photo/voice, or end-to-end tests.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
STUDIO = ROOT / "showroom" / "shirmani-supreme-character-studio.html"


class CharacterStudioContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = STUDIO.read_text(encoding="utf-8")

    def test_page_exists_and_identifies_as_prototype(self):
        self.assertIn("<title>SHIRMANI SUPREME Character Studio", self.html)
        self.assertIn("PROTOTYPE — NOT A LIVE AVATAR", self.html)
        self.assertIn("यह AI model/API call नहीं करता", self.html)

    def test_missing_original_media_is_not_misrepresented(self):
        self.assertIn("मूल फोटो:", self.html)
        self.assertIn("ASSET REQUIRED", self.html)
        self.assertIn("मूल अधिकृत आवाज़:", self.html)
        self.assertIn("External provider: NOT CONNECTED / NOT VERIFIED", self.html)
        self.assertNotRegex(self.html, re.compile(r"<(?:img|audio|video)\b", re.IGNORECASE))

    def test_evidence_labels_and_insufficient_evidence_phrase_remain_visible(self):
        for label in (
            "INDEPENDENTLY VERIFIED",
            "SOURCE-BASED",
            "PHILOSOPHICAL / PERSONAL PERSPECTIVE",
            "INSUFFICIENT EVIDENCE",
            "अभी पर्याप्त प्रमाण उपलब्ध नहीं है।",
        ):
            with self.subTest(label=label):
                self.assertIn(label, self.html)

    def test_workbench_controls_and_handlers_exist(self):
        for element_id in ("question", "depth", "evidence", "generate", "copy", "download", "output"):
            with self.subTest(element_id=element_id):
                self.assertIn(f'id="{element_id}"', self.html)
        self.assertIn("$('generate').addEventListener('click',make)", self.html)
        self.assertIn("navigator.clipboard.writeText(latest)", self.html)
        self.assertIn("URL.createObjectURL(new Blob", self.html)

    def test_identity_line_is_present(self):
        self.assertIn(
            "Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet "
            "Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh",
            self.html,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
