#! /usr/bin/python3

import unittest
import math

def calculate_area(a: float, b: float, c: float):
    """This function calculates and returns area of triangle."""
    p = (a + b + c) / 2.0
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

class Qwerty(unittest.TestCase):

    def test_qwerty(self):
        self.assertEqual(calculate_area(3, 4, 5), 6)

    def test_qwerty1(self):
        self.assertNotEquals(calculate_area(3, 4, 5), 10)

    def test_qw(self):
         self.assertAlmostEquals(calculate_area(10, 7, 12), 34.98, 2)



if __name__ == "__main__":
     unittest.main()