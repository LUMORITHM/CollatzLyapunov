import unittest
from growth_streak import update_growth_streak

class TestGrowthStreak(unittest.TestCase):
    
    def test_initial_growth_prone(self):
        self.assertEqual(update_growth_streak(3, 0), 1)
        self.assertEqual(update_growth_streak(7, 2), 3)
        self.assertEqual(update_growth_streak(11, 5), 6)
        self.assertEqual(update_growth_streak(15, 10), 11)

    def test_non_growth_prone_resets(self):
        self.assertEqual(update_growth_streak(0, 4), 0)
        self.assertEqual(update_growth_streak(1, 1), 0)
        self.assertEqual(update_growth_streak(10, 6), 0)
        self.assertEqual(update_growth_streak(14, 3), 0)

    def test_negative_input_handling(self):
        self.assertEqual(update_growth_streak(-13, 2), 3)  # -13 % 16 = 3
        self.assertEqual(update_growth_streak(-1, 7), 8)   # -1 % 16 = 15
        self.assertEqual(update_growth_streak(-4, 5), 0)   # -4 % 16 = 12

if __name__ == '__main__':
    unittest.main()
