import unittest
from factory.supreme_nlp_scientific_benchmark import evaluate, smoke

class ScientificBenchmarkTests(unittest.TestCase):
    def test_smoke(self):
        self.assertEqual(smoke()["accuracy"], 0.75)
        self.assertAlmostEqual(smoke()["macro_f1"], 2/3, places=8)

    def test_perfect_labelled_set(self):
        r=evaluate([{"label":"a","prediction":"a"},{"label":"b","prediction":"b"}])
        self.assertEqual(r["accuracy"],1.0)
        self.assertEqual(r["macro_f1"],1.0)

    def test_empty_is_not_accuracy(self):
        r=evaluate([])
        self.assertIsNone(r["accuracy"])
        self.assertFalse(r["measured"])

if __name__=="__main__":
    unittest.main()
