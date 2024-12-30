import unittest
from algorithm.math_algo import gcd

class TestGcd(unittest.TestCase):
    def test_gcd_with_integers(self):
        test_cases = [
            (4, 6, 2),
            (6, 4, 2),
            (4, 4, 4),
            (2, 4, 2)
        ]
        for num1, num2, expected in test_cases:
            with self.subTest(num1=num1, num2=num2):
                self.assertEqual(gcd(num1, num2), expected)

    def test_gcd_with_floats(self):
        test_cases = [
            (4.0, 6.0, 2),
            (6.0, 4.0, 2),
            (4.0, 4.0, 4),
            (2.0, 4.0, 2)
        ]
        for num1, num2, expected in test_cases:
            with self.subTest(num1=num1, num2=num2):
                self.assertEqual(gcd(num1, num2), expected)

    def test_gcd_with_float_decimals(self):
        num1, num2 = 4.2, 6.2
        with self.assertRaises(ValueError):
            gcd(num1, num2)

    def test_gcd_with_negatives(self):
        test_cases = [
            (-4, 6, 2),
            (6, -4, 2),
            (-4, -4, 4),
            (-2, -4, 2)
        ]
        for num1, num2, expected in test_cases:
            with self.subTest(num1=num1, num2=num2):
                self.assertEqual(gcd(num1, num2), expected)
