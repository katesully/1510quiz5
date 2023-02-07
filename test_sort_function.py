from unittest import TestCase

from sort import is_sorted


class TestSorted(TestCase):
    def test_is_sorted(self):
        self.assertEqual(True, is_sorted([1, 2, 3]))
    def test_is_sorted_decreasing(self):
        self.assertEqual(False, is_sorted([12, 6, 2]))
    def test_is_sorted_zeroes(self):
        self.assertEqual(True, is_sorted([0, 0, 0]))

    def test_is_sorted_negatives_ascending(self):
        self.assertEqual(True, is_sorted([-1, 0, 3]))

    def test_is_sorted_negatives_decreasing(self):
        self.assertEqual(False, is_sorted([-1, -3, -6]))

    def test_is_sorted_empty(self):
        self.assertEqual(False, is_sorted([]))
