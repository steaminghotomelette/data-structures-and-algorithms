import unittest
from utils.swap import swap

class TestSwap(unittest.TestCase):

    def test_swap_same_list(self):
        lst = [1, 2, 3]
        swap(lst, 0, lst, 1)
        self.assertEqual(lst, [2, 1, 3])

    def test_swap_diff_list(self):
        lst1 = [1, 2]
        lst2 = [3, 4]
        swap(lst1, 0, lst2, 0)
        self.assertEqual(lst1, [3, 2])
        self.assertEqual(lst2, [1, 4])

    def test_out_of_bounds_1(self):
        with self.assertRaises(IndexError):
            swap([1, 2, 3, 4], 6, [1, 2], 0)
        with self.assertRaises(IndexError):
            swap([1, 2, 3, 4], -1, [1, 2], 0)

    def test_out_of_bounds_2(self):
        with self.assertRaises(IndexError):
            swap([1, 2, 3, 4], 0, [1, 2], 4)
        with self.assertRaises(IndexError):
            swap([1, 2, 3, 4], 0, [1, 2], -1)

if __name__ == "__main__":
    unittest.main()
