import unittest
import math
from lyapunov_function import V

class TestLyapunovFunction(unittest.TestCase):

    def test_basic_value(self):
        # V(16, 0) = log2(16) + alpha(0) + beta * 0
        # log2(16) = 4, alpha(0) = -0.06, beta * 0 = 0
        expected = 4.0 - 0.06
        result = V(16, 0)
        self.assertAlmostEqual(result, expected, places=6)

    def test_streak_contribution(self):
        # V(16, 2) = log2(16) + alpha(0) + 0.7 * 2 = 4 - 0.06 + 1.4
        expected = 4.0 - 0.06 + 1.4
        result = V(16, 2)
        self.assertAlmostEqual(result, expected, places=6)

    def test_custom_beta(self):
        # Test with beta = 1.0
        expected = math.log2(10) + 0.11 + 1.0 * 3  # 10 mod 16 = 10, alpha(10) = -0.05
        result = V(11, 3, beta=1.0)
        self.assertAlmostEqual(result, math.log2(11) + 0.11 + 3.0, places=6)

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            V(0, 0)
        with self.assertRaises(ValueError):
            V(-5, 1)

    def test_invalid_streak(self):
        with self.assertRaises(ValueError):
            V(10, -1)

if __name__ == '__main__':
    unittest.main()
