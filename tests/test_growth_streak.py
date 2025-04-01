✅ test_growth_streak.py (Final Test File)
python
Copy
Edit
import unittest
from growth_streak import update_growth_streak

class TestGrowthStreak(unittest.TestCase):

    def test_growth_prone_residues(self):
        # Residues 3, 7, 11, 15 should increment the streak
        for residue in [3, 7, 11, 15]:
            n = 1000 + residue
            self.assertEqual(update_growth_streak(n, 2), 3)

    def test_non_growth_residues(self):
        # All other residues should reset the streak
        for residue in [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]:
            n = 1000 + residue
            self.assertEqual(update_growth_streak(n, 5), 0)

    def test_streak_starts_from_zero(self):
        self.assertEqual(update_growth_streak(19, 0), 1)  # 19 mod 16 = 3 (growth-prone)
        self.assertEqual(update_growth_streak(20, 0), 0)  # 20 mod 16 = 4 (not growth-prone)

    def test_negative_streak_input(self):
        with self.assertRaises(ValueError):
            update_growth_streak(19, -1)

if __name__ == "__main__":
    unittest.main()
