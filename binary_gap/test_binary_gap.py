import unittest

from binary_gap import n_binary_gap


class TestBinaryGap(unittest.TestCase):
    def test_n_binary_gap_no_gap(self):
        self.assertEqual(n_binary_gap(1), 0)

    def test_n_binary_gap(self):
        self.assertEqual(n_binary_gap(529), 4)


if __name__ == "__main__":
    unittest.main()
