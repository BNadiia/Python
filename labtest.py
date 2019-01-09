#! /usr/bin/python3

import unittest
import math

def calculate_area(a: float, b: float, c: float):
    """This function calculates and returns area of triangle."""
    p = (a + b + c) / 2.0
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

class Qwerty(unittest.TestCase):

    def test_triangleE(self):
        self.assertEqual(calculate_area(3, 4, 5), 6)

    def test_triangleNE(self):
        self.assertNotEquals(calculate_area(3, 4, 5), 10)

    def test_triangleAE(self):
         self.assertAlmostEquals(calculate_area(10, 7, 12), 34.98, 2)

    def test_triangleT(self):
        self.assertTrue(calculate_area(3, 4, 5) == 6)

    def test_triangleF(self):
        self.assertFalse(calculate_area(3, 4, 5) == 9)


if __name__ == "__main__":
     unittest.main()
