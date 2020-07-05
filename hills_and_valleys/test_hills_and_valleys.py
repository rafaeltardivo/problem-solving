import unittest

from .hills_and_valleys import n2_hills_and_valley


class TestHillsAndValleys(unittest.TestCase):
    def test_empty_list_edge_case(self):
        self.assertEqual(n2_hills_and_valley([]), 0)

    def test_one_item_edge_case(self):
        self.assertEqual(n2_hills_and_valley([1]), 1)

    def test_one_repeated_item_edge_case(self):
        self.assertEqual(n2_hills_and_valley([1, 1, 1, 1, 1]), 1)

    def test_two_items_hills_and_valleys(self):
        self.assertEqual(n2_hills_and_valley([1, 2]), 2)

    def test_one_item_repeated_hills_and_valleys(self):
        self.assertEqual(n2_hills_and_valley([-10, 2, 2, 2, 2]), 2)

    def test_three_items_hills_and_valleys(self):
        self.assertEqual(n2_hills_and_valley([1, 2, 1]), 3)

    def test_mixed_repeated_items_hills_and_valleys(self):
        self.assertEqual(n2_hills_and_valley([1, 2, 3, 4, 4, 3, 4, 4, 5, 6]), 4)
