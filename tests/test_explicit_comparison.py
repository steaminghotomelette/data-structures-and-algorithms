import unittest
from utils.explicit_comparison import explicit_comparison

class TestExplicitComparison(unittest.TestCase):

    def test_forward_match(self):
        result = explicit_comparison("test", 0, "test", 0)
        self.assertEqual(result, (False, 4, 4))

    def test_forward_mismatch(self):
        result = explicit_comparison("wooloo", 0, "woomoo", 0)
        self.assertEqual(result, (True, 3, 3))

    def test_forward_mismatch_diff_index(self):
        result = explicit_comparison("hello", 2, "jello", 3)
        self.assertEqual(result, (True, 3, 4))

    def test_reverse_match(self):
        result = explicit_comparison("test", 3, "test", 3, reverse=True)
        self.assertEqual(result, (False, -1, -1))

    def test_reverse_mismatch(self):
        result = explicit_comparison("west", 3, "test", 3, reverse=True)
        self.assertEqual(result, (True, 0, 0))

    def test_reverse_mismatch_diff_index(self):
        result = explicit_comparison("moogoo", 5, "foogoo", 2, reverse=True)
        self.assertEqual(result, (True, 3, 0))

    def test_out_of_bounds_1(self):
        with self.assertRaises(IndexError):
            explicit_comparison("hello", 6, "hello", 0)
        with self.assertRaises(IndexError):
            explicit_comparison("hello", 0, "hello", 6)

    def test_out_of_bounds_2(self):
        with self.assertRaises(IndexError):
            explicit_comparison("hello", -1, "hello", 0)
        with self.assertRaises(IndexError):
            explicit_comparison("hello", 0, "hello", -1)

if __name__ == "__main__":
    unittest.main()
