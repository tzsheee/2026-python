"""數字根 — 測試

複製自 starter，包含基本、edge、與例外案例。
"""

import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic(self):
        # example from README
        self.assertEqual(digit_root(199), 1)
        self.assertEqual(digit_root(10), 1)
        self.assertEqual(digit_root(7), 7)

    def test_edge_case(self):
        # large value near the upper bound
        self.assertEqual(digit_root(2000000000), digit_root(2_000_000_000))
        # repetitive digits
        self.assertEqual(digit_root(999999999), 9)

    def test_invalid_input_raises(self):
        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(0)
        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(-5)


if __name__ == "__main__":
    unittest.main()
