import unittest

from anagram import nlogn_anagram, n_anagram

class TestAnagram(unittest.TestCase):
    
    def test_nlogn_length_edge_case(self):
        self.assertFalse(nlogn_anagram("len4", "len44"))

    def test_nlogn_different_words(self):
        self.assertFalse(nlogn_anagram("school master", "class"))

    def test_nlogn_anagram(self):
        self.assertTrue(nlogn_anagram("clint eastwood", "old west action"))

    def test_n_length_edge_case(self):
        self.assertFalse(n_anagram("len4", "len44"))

    def test_n_different_words(self):
        self.assertFalse(n_anagram("school master", "class"))

    def test_n_anagram(self):
        self.assertTrue(n_anagram("clint eastwood", "old west action"))


if __name__ == '__main__':
    unittest.main()