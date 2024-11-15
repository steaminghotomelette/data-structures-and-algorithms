import unittest
from algorithms.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_short_search_int(self):
        result = binary_search([0, 2, 4, 5, 6, 9, 10], 6)
        self.assertEqual(result, 4)

    def test_long_search_int(self):
        result = binary_search([4, 6, 7, 10, 9, 11, 112, 223, 331, 444, 445, 777, 819, 1000, 1003, 1004, 4000, 5000, 9000, 10000, 11100, 100000, 1000000, 9999999], 9999999)
        self.assertEqual(result, 23)

    def test_not_in_array_int(self):
        result = binary_search([1, 2, 3, 4, 5, 6], 7)
        self.assertIsNone(result)

    def test_short_search_str(self):
        result = binary_search(['a', 'b', 'c', 'd'], 'c')
        self.assertEqual(result, 2)

    def test_long_search_str(self):
        result = binary_search(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 'd')
        self.assertEqual(result, 3)

    def test_not_in_array_str(self):
        result = binary_search(['a', 'b', 'c', 'd'], 'x')
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
