import unittest
from algorithms.karatsuba import karatsuba

class TestKaratsuba(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(karatsuba(3, 7), 3 * 7)
        self.assertEqual(karatsuba(12, 34), 12 * 34)
        self.assertEqual(karatsuba(0, 123), 0 * 123)
        self.assertEqual(karatsuba(123, 0), 123 * 0)

    def test_medium_numbers(self):
        self.assertEqual(karatsuba(1234, 5678), 1234 * 5678)
        self.assertEqual(karatsuba(34567, 89012), 34567 * 89012)
        self.assertEqual(karatsuba(1, 100000), 1 * 100000)

    def test_large_numbers(self):
        self.assertEqual(karatsuba(123456789, 987654321), 123456789 * 987654321)
        self.assertEqual(karatsuba(10**10, 10**10), 10**10 * 10**10)
        self.assertEqual(karatsuba(10**15, 10**15), 10**15 * 10**15)

    def test_negative_numbers(self):
        self.assertEqual(karatsuba(-123, 456), -123 * 456)
        self.assertEqual(karatsuba(123, -456), 123 * -456)
        self.assertEqual(karatsuba(-123, -456), -123 * -456)

    def test_mixed_sign_large_numbers(self):
        self.assertEqual(karatsuba(-123456789, 987654321), -123456789 * 987654321)
        self.assertEqual(karatsuba(123456789, -987654321), 123456789 * -987654321)
        self.assertEqual(karatsuba(-10**10, 10**10), -10**10 * 10**10)

    def test_edge_cases(self):
        self.assertEqual(karatsuba(0, 0), 0 * 0)
        self.assertEqual(karatsuba(1, 1), 1 * 1)
        self.assertEqual(karatsuba(1, 0), 1 * 0)

if __name__ == "__main__":
    unittest.main()
