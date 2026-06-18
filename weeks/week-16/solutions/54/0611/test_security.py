"""Stage 5 — 安全性自掃測試"""

import unittest
import json
import os
import tempfile
from benchmark import make_data
from plot import load_results


class TestSecurity(unittest.TestCase):

    def test_sorts_no_unused_random_import(self):
        with open("sorts.py") as f:
            content = f.read()
        self.assertNotIn("import random", content)

    def test_make_data_rejects_negative_n(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_load_results_rejects_non_dict_json(self):
        tmp = tempfile.mkdtemp()
        path = os.path.join(tmp, "bad.json")
        with open(path, "w") as f:
            json.dump([1, 2, 3], f)
        with self.assertRaises(ValueError):
            load_results(path)


if __name__ == "__main__":
    unittest.main()
