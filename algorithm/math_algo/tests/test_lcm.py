import unittest
from algorithm.math_algo import lcm

class TestMathAlgo(unittest.TestCase):
    def test_lcm_with_integers(self):
        test_cases = [
            (4, 6, 12),
            (6, 4, 12),
            (4, 4, 4),
            (0, 5, 0),
            (7, 0, 0),
            (3, 5, 15)
        ]
        for num1, num2, expected in test_cases:
            with self.subTest(num1=num1, num2=num2):
                self.assertEqual(lcm(num1, num2), expected)

    def test_lcm_with_floats_equivalent_to_integers(self):
        test_cases = [
            (4.0, 6.0, 12),
            (6.0, 4.0, 12),
            (4.0, 4.0, 4),
            (0.0, 5.0, 0),
            (7.0, 0.0, 0),
            (3.0, 5.0, 15)
        ]
        for num1, num2, expected in test_cases:
            with self.subTest(num1=num1, num2=num2):
                self.assertEqual(lcm(num1, num2), expected)

    def test_lcm_with_invalid_floats(self):
        test_cases = [
            (4.2, 6),
            (6, 4.5),
            (3.1, 5.2)
        ]
        for num1, num2 in test_cases:
            with self.subTest(num1=num1, num2=num2):
                with self.assertRaises(ValueError):
                    lcm(num1, num2)

    def test_lcm_with_negative_numbers(self):
        test_cases = [
            (-4, 6, 12),
            (6, -4, 12),
            (-4, -6, 12),
            (-3, 5, 15)
        ]
        for num1, num2, expected in test_cases:
            with self.subTest(num1=num1, num2=num2):
                self.assertEqual(lcm(num1, num2), expected)