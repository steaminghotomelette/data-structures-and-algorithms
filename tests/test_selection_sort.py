import unittest
from algorithms.selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        selection_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_single_element(self):
        arr = [42]
        selection_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        selection_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        selection_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_random_integers(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        selection_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_duplicates(self):
        arr = [4, 2, 4, 2, 4, 2]
        selection_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_negative_numbers(self):
        arr = [3, -1, -4, 2, 0]
        selection_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_strings(self):
        arr = ["apple", "orange", "banana", "pear"]
        selection_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_mixed_case_strings(self):
        arr = ["Apple", "orange", "Banana", "pear"]
        selection_sort(arr)
        self.assertEqual(arr, sorted(arr))

if __name__ == "__main__":
    unittest.main()
