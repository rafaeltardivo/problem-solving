import unittest

from .missing_element import n_missing_element, n_missing_element_dic


class TestMissingElement(unittest.TestCase):
    def test_n_missing_element(self):
        self.assertEqual(n_missing_element([1, 2, 3, 4], [1, 2, 3]), [4])

    def test_n_missing_element_dic(self):
        self.assertEqual(n_missing_element_dic([1, 2, 3, 4], [1, 2, 3]), [4])
