import unittest

from src.metrics.core import cr, ctr, roi, safe_divide


class TestMetricsCore(unittest.TestCase):
    def test_safe_divide_normal(self):
        self.assertEqual(safe_divide(10, 2), 5)

    def test_safe_divide_zero_denominator(self):
        self.assertEqual(safe_divide(10, 0), 0.0)

    def test_ctr(self):
        self.assertAlmostEqual(ctr(50, 1000), 0.05)

    def test_cr(self):
        self.assertAlmostEqual(cr(20, 200), 0.1)

    def test_roi(self):
        self.assertAlmostEqual(roi(3000, 1000), 3.0)


if __name__ == "__main__":
    unittest.main()
