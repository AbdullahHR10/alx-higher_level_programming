import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0, 1, 15, 6]), 15)
        self.assertEqual(max_integer([19, 120, 1100, 5960]), 5960)
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-15, -2, -600, -1520]), -2)
        self.assertEqual(max_integer([-1, 0, -8, -9]), 0)
        self.assertEqual(max_integer([-1, -210, 1, -2]), 1)
    def test_smaller_lists(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
