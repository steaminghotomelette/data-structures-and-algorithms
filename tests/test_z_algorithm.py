import unittest
from algorithms.z_algorithm import z_algorithm

class TestZAlgorithm(unittest.TestCase):

    def test_basic_pattern(self):
        result = z_algorithm("aabcaabxaaaz")
        self.assertEqual(result, [12, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0])
    
    def test_difficult_pattern(self):
        result = z_algorithm("aaabddsaaabfdsssfaaannfllssssaaaaaaanffssssakeuiqqqqqudfallaaababababaljalsduishfafafkafjneedlehaystackneedlehaystackblahblahablajfalfjdkfjffqqqdaoffahaystackneedlewwawaaasfwwwfjakforwadjfkjdlsfj")
        self.assertEqual(result, [195, 2, 1, 0, 0, 0, 0, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 4, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_periodic_pattern(self):
        result = z_algorithm("aabaabaab")
        self.assertEqual(result, [9, 1, 0, 6, 1, 0, 3, 1, 0])
    
    def test_repeated_pattern(self):
        result = z_algorithm("aaaaaaaa")
        self.assertEqual(result, [8, 7, 6, 5, 4, 3, 2, 1])
    
    def test_all_unique_pattern(self):
        result = z_algorithm("abcdefg")
        self.assertEqual(result, [7, 0, 0, 0, 0, 0, 0])
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            z_algorithm("")

if __name__ == "__main__":
    unittest.main()
