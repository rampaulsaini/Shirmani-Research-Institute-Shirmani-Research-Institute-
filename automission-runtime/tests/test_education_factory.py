import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from education_factory import build_program, validate_program

class EducationFactoryTests(unittest.TestCase):
    def test_affordable_program_blueprint(self):
        p = build_program(
            "Affordable AI & Software Engineering",
            "computer_science",
            level="professional",
            delivery="hybrid",
            languages=["en", "hi"],
            fee_inr=15000,
            duration_weeks=24,
        )
        self.assertEqual(p["fee_inr"], 15000)
        self.assertIn("practical_projects", p["curriculum"])
        self.assertFalse(p["quality"]["recognized_degree_claim_allowed"])
        self.assertTrue(validate_program(p))

    def test_invalid_level_rejected(self):
        with self.assertRaises(ValueError):
            build_program("X", "AI", level="degree")

if __name__ == "__main__":
    unittest.main()
