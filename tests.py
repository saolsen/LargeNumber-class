#/usr/bin/env python
# Normal Test Driver for the LargeNumber class
# Stephen Olsen

import unittest
from largeNumber import LargeNumber

class TestLargeNumberClass(unittest.TestCase):

    def test_toAndFromString(self):
        num_str = "1234543212345"
        num = LargeNumber(num_str)
        self.assertEqual(num_str, str(num))

    def test_lessThan(self):
        num1 = LargeNumber("123454321")
        num2 = LargeNumber("123454322")
        self.assertTrue(num1 < num2)

    def test_greaterThan(self):
        num1 = LargeNumber("123454321")
        num2 = LargeNumber("123454322")
        self.assertTrue(num2 > num1)

    def test_equality(self):
        num1 = LargeNumber("123454321")
        num2 = LargeNumber("123454321")
        self.assertTrue(num1 == num2)

    def test_addition(self):
        num1 = LargeNumber("123454321")
        num2 = LargeNumber("1")
        num3 = num1 + num2
        self.assertEqual(num3, LargeNumber("123454322"))

    def test_subtraction(self):
        num1 = LargeNumber("123454321")
        num2 = LargeNumber("1")
        num3 = num1 - num2
        self.assertEqual(num3, LargeNumber("123454320"))

    def test_multiplication(self):
        num1 = LargeNumber("1111111")
        num2 = LargeNumber("2222222")
        num3 = LargeNumber("2")
        self.assertEqual(num1 * num3, num2)

    def test_division(self):
        num1 = LargeNumber("2222222")
        num2 = LargeNumber("1111111")
        num3 = LargeNumber("2")
        self.assertEqual(num1 / num3, num2)

    def test_modulus(self):
        num1 = LargeNumber("2222222")
        num2 = LargeNumber("1111110")
        num3 = LargeNumber("2")
        self.assertEqual(num1 % num2, num3)

    def test_rightshift(self):
        num1 = LargeNumber("222222")
        num2 = LargeNumber("6944")
        self.assertEqual(num1 >> 5, num2)

    def test_generateRandomInARange(self):
        num1 = LargeNumber("12345")
        num2 = LargeNumber("54321")
        num3 = LargeNumber.Random(num1, num2)
        self.assertTrue(num3 >= num1)
        self.assertTrue(num3 <= num2)

if __name__ == "__main__":
    unittest.main()
