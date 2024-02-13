"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(max_integer([1, 8, 3, 4]), 8)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0, 2, 6, 4]), 6)
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_negative(self):
        self.assertEqual(max_integer([-10, -6, -1, -7]), -1)
        self.assertEqual(max_integer([-10, -6, -5, -3]), -3)
        self.assertEqual(max_integer([-2, -6, -9, -7]), -2)
        self.assertEqual(max_integer([-10, -1, -9, -7]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_same_elements(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        
    def test_multimax(self):
        self.assertEqual(max_integer([5, 5, 3, 2]), 5)
        self.assertEqual(max_integer([-10, -5, -1, -1]), -1)
    
    def test_types(self):
        with self.assertRaises(TypeError):
            max_integer([10, "string", 5])
