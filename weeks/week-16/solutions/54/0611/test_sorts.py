"""Stage 2 — 排序正確性測試"""

import unittest
from sorts import bubble_sort, quick_sort, merge_sort

SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):

    def _check_sorted(self, sort_fn, data):
        expected = sorted(data)
        result = sort_fn(data)
        self.assertEqual(result, expected)
        self.assertIsNot(result, data)

    def test_basic_cases(self):
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self._check_sorted(fn, [3, 1, 2])
                self._check_sorted(fn, [1])
                self._check_sorted(fn, [])

    def test_already_sorted(self):
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self._check_sorted(fn, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self._check_sorted(fn, [5, 4, 3, 2, 1])

    def test_all_equal(self):
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self._check_sorted(fn, [7, 7, 7, 7])

    def test_random_data_matches_builtin(self):
        import random
        random.seed(42)
        data = [random.randint(0, 1000) for _ in range(200)]
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                self._check_sorted(fn, data)

    def test_input_not_mutated(self):
        original = [3, 1, 4, 1, 5, 9]
        backup = list(original)
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                fn(original)
                self.assertEqual(original, backup)

    def test_uncomparable_elements(self):
        for fn in SORT_FUNCTIONS:
            with self.subTest(fn=fn.__name__):
                with self.assertRaises(TypeError):
                    fn([1, "a", 2])


if __name__ == "__main__":
    unittest.main()
