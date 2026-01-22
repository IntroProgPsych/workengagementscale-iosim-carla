# tests.py
import unittest
# We import the function we want to test from app.py
from app import interpret_score

class TestWorkEngagement(unittest.TestCase):

    def test_interpret_high(self):
        # Requirement: High if mean > 4
        self.assertEqual(interpret_score(4.5), "High")
        self.assertEqual(interpret_score(6), "High")

    def test_interpret_moderate(self):
        # Requirement: Moderate if 2 <= mean <= 4
        self.assertEqual(interpret_score(4.0), "Moderate")
        self.assertEqual(interpret_score(2.0), "Moderate")
        self.assertEqual(interpret_score(3.5), "Moderate")

    def test_interpret_low(self):
        # Requirement: Low if mean < 2
        self.assertEqual(interpret_score(1.5), "Low")
        self.assertEqual(interpret_score(0), "Low")

if __name__ == '__main__':
    unittest.main()
