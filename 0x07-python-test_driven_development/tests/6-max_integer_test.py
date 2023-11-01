#!/usr/bin/python3
"""this module is a unittest"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_integer_single_element(self):
        self.assertEqual(max_integer([100]), 100)

    def test_max_integer_negative_numbers(self):
        self.assertEqual(max_integer([-10, -20, -5, -1]), -1)

    def test_max_integer_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_mixed_numbers(self):
        self.assertEqual(max_integer([10, -20, 30, -40]), 30)

    def test_max_integer_duplicate_max(self):
        self.assertEqual(max_integer([10, 100, 100, 50]), 100)


if __name__ == '__main__':
    unittest.main()
