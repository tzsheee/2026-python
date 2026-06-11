"""Stage 1 — @timeit 裝飾器測試"""

import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(1, 2), 3)

        @timeit
        def returns_none():
            pass

        self.assertIsNone(returns_none())

    def test_preserves_function_metadata(self):
        @timeit
        def foo():
            """docstring"""
            return 42

        self.assertEqual(foo.__name__, "foo")
        self.assertEqual(foo.__doc__, "docstring")

    def test_records_elapsed_time(self):
        @timeit
        def wait():
            return 1

        wait()
        self.assertIsInstance(wait.last_elapsed, float)
        self.assertGreaterEqual(wait.last_elapsed, 0)
        self.assertEqual(len(wait.records), 1)
        self.assertEqual(wait.records[0], wait.last_elapsed)

        wait()
        self.assertEqual(len(wait.records), 2)

    def test_edge_case_exception_still_records(self):
        @timeit
        def raiser():
            raise ValueError("boom")

        with self.assertRaises(ValueError):
            raiser()
        self.assertIsInstance(raiser.last_elapsed, float)
        self.assertEqual(len(raiser.records), 1)

    def test_edge_case_no_params_and_none_return(self):
        @timeit
        def noop():
            return None

        self.assertIsNone(noop())
        self.assertIsInstance(noop.last_elapsed, float)

    def test_edge_case_multiple_calls_accumulates(self):
        @timeit
        def fast():
            return 0

        for _ in range(5):
            fast()
        self.assertEqual(len(fast.records), 5)
        for t in fast.records:
            self.assertIsInstance(t, float)


if __name__ == "__main__":
    unittest.main()
