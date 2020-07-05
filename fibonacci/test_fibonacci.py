import unittest

from fibonacci import n_dynamic_fibonacci, n_fibonacci


class TestFibonacci(unittest.TestCase):
    def test_n_fibonacci(self):
        self.assertEqual(n_fibonacci(7), 13)

    def test_n_dynamic_fibonacci(self):
        self.assertEqual(n_dynamic_fibonacci(7), 13)


if __name__ == "__main__":
    unittest.main()
