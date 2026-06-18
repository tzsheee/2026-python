"""Stage 4 — 繪圖測試"""

import unittest
import os
import json
import tempfile
from plot import load_results, plot_results


class TestPlot(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.sample_data = {
            "500": {"bubble_sort": 0.005, "quick_sort": 0.0004, "merge_sort": 0.0005},
            "1000": {"bubble_sort": 0.025, "quick_sort": 0.0008, "merge_sort": 0.001},
        }
        self.json_path = os.path.join(self.tmp, "results.json")
        with open(self.json_path, "w") as f:
            json.dump(self.sample_data, f)

    def test_load_results_returns_dict(self):
        data = load_results(self.json_path)
        self.assertIsInstance(data, dict)

    def test_load_results_keys_are_ints(self):
        data = load_results(self.json_path)
        for key in data:
            self.assertIsInstance(key, int)

    def test_plot_output_png_exists(self):
        out_path = os.path.join(self.tmp, "benchmark.png")
        data = load_results(self.json_path)
        plot_results(data, out_path)
        self.assertTrue(os.path.isfile(out_path))
        self.assertGreater(os.path.getsize(out_path), 0)


if __name__ == "__main__":
    unittest.main()
