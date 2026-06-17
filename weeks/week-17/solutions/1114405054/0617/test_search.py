import unittest
from search import linear_search, binary_search


class TestSearch(unittest.TestCase):

    def test_linear_finds_first_occurrence(self):
        self.assertEqual(linear_search([10, 20, 20, 30], 20), 1)

    def test_linear_returns_minus_one_when_missing(self):
        self.assertEqual(linear_search([10, 20, 30], 99), -1)

    def test_linear_empty_list(self):
        self.assertEqual(linear_search([], 99), -1)

    def test_linear_single_element_found(self):
        self.assertEqual(linear_search([42], 42), 0)

    def test_linear_single_element_not_found(self):
        self.assertEqual(linear_search([42], 99), -1)

    def test_binary_finds_target_in_sorted(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 5), 2)

    def test_binary_returns_minus_one_when_missing(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 4), -1)

    def test_binary_empty_list(self):
        self.assertEqual(binary_search([], 99), -1)

    def test_binary_single_element_found(self):
        self.assertEqual(binary_search([42], 42), 0)

    def test_binary_single_element_not_found(self):
        self.assertEqual(binary_search([42], 99), -1)

    def test_binary_target_at_leftmost(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 1), 0)

    def test_binary_target_at_rightmost(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 7), 3)

    def test_binary_even_length(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)

    def test_binary_odd_length(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_binary_target_smaller_than_all(self):
        self.assertEqual(binary_search([10, 20, 30], 5), -1)

    def test_binary_target_larger_than_all(self):
        self.assertEqual(binary_search([10, 20, 30], 40), -1)
