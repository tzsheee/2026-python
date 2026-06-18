import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        @timeit(repeat=3)
        def add(a, b):
            return a + b
        self.assertEqual(add(2, 3), 5)

    def test_preserves_function_metadata(self):
        @timeit(repeat=3)
        def sample():
            """docstring"""
            pass
        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "docstring")

    def test_records_each_repeat_and_average(self):
        @timeit(repeat=5)
        def empty():
            pass
        empty()
        self.assertEqual(len(empty.records), 5)
        self.assertIsInstance(empty.last_elapsed, float)

    def test_rejects_invalid_repeat(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def f():
                pass

    def test_no_print_pollution(self):
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        try:
            @timeit(repeat=3)
            def f():
                pass
            f()
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "")

    def test_repeat_1_works(self):
        @timeit(repeat=1)
        def f():
            return 42
        self.assertEqual(f(), 42)
        self.assertEqual(len(f.records), 1)
