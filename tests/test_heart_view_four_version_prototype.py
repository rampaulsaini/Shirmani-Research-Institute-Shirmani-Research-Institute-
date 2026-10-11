"""Static regression checks for the browser-local Heart-View prototype.

These checks verify source-level contracts only. They do not claim browser,
audio, avatar, video, or live-provider integration has been exercised.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "showroom" / "heart-view-character-four-version-prototype.html"


class HeartViewPrototypeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = PAGE.read_text(encoding="utf-8")

    def test_page_is_hindi_and_mobile_friendly(self):
        self.assertIn('<html lang="hi">', self.html)
        self.assertIn('name="viewport"', self.html)
        self.assertIn("@media(max-width:520px)", self.html)

    def test_four_distinct_versions_are_selectable(self):
        for version in ("v1", "v2", "v3", "v4"):
            self.assertRegex(self.html, rf'data-version="{version}"')
        self.assertIn("V1 — स्पष्ट स्क्रिप्ट", self.html)
        self.assertIn("V2 — आवाज़ अभ्यास", self.html)
        self.assertIn("V3 — अवतार योजना", self.html)
        self.assertIn("V4 — लाइव प्रस्तोता", self.html)
        self.assertIn("aria-pressed", self.html)

    def test_evidence_and_uncertainty_boundary_present(self):
        self.assertIn("अभी पर्याप्त प्रमाण उपलब्ध नहीं है।", self.html)
        self.assertIn("दार्शनिक / व्यक्तिगत दृष्टिकोण", self.html)
        self.assertIn("स्रोत उपलब्ध, स्वतंत्र जाँच बाकी", self.html)
        self.assertIn("वैज्ञानिक तथ्य के रूप में प्रस्तुत न करें", self.html)

    def test_authorization_gate_and_external_service_disclosure(self):
        self.assertIn("अनुमति की पुष्टि बाकी — मीडिया निर्माण रोकें", self.html)
        self.assertIn("HeyGen या किसी अन्य प्रदाता से कनेक्शन", self.html)
        self.assertIn("लाइव सेवा नहीं", self.html)

    def test_output_actions_and_status_are_wired(self):
        for token in ('addEventListener', "function build()", "Blob(", "navigator.clipboard.writeText", "aria-live"):
            self.assertIn(token, self.html)

    def test_no_remote_script_or_tracking_pixel(self):
        self.assertIsNone(re.search(r'<script[^>]+src\s*=', self.html, re.I))
        self.assertIsNone(re.search(r'<img[^>]+src\s*=\s*["\']https?://', self.html, re.I))

    def test_all_versions_disclose_capability_limits(self):
        for token in ("ऑडियो जनरेट नहीं होता", "फोटो/चेहरा एनिमेट नहीं होता",
                      "कोई लाइव सेवा नहीं", "कोई बाहरी सेवा नहीं"):
            self.assertIn(token, self.html)


if __name__ == "__main__":
    unittest.main(verbosity=2)
