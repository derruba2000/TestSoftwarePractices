import unittest
from src.sample import is_divisible


class Test_test_3(unittest.TestCase):
    def test_A(self):
        self.fail("Not implemented")

    def test_divisible_numbers(self):
       self.assertTrue(is_divisible(10, 2))
       self.assertTrue(is_divisible(10, 10))
       self.assertTrue(is_divisible(1000, 1))

    def test_not_divisible_numbers(self):
       self.assertFalse(is_divisible(5, 3))
       self.assertFalse(is_divisible(5, 6))
       self.assertFalse(is_divisible(10, 3))

if __name__ == '__main__':
    unittest.main()
