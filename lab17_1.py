#! /usr/bin/python3

import unittest
import lab6_1

class Qwerty(unittest.TestCase):

    def test_triangleE(self):
        self.assertEqual(lab6_1.calculate_area(3, 4, 5), 6)

    def test_triangleNE(self):
        self.assertNotEqual(lab6_1.calculate_area(3, 4, 5), 10)

    def test_triangleAE(self):
        self.assertAlmostEqual(lab6_1.calculate_area(10, 7, 12), 34.98, 2)

    def test_triangleT(self):
        self.assertTrue(lab6_1.calculate_area(3, 4, 5) == 6)

    def test_triangleF(self):
        self.assertFalse(lab6_1.calculate_area(3, 4, 5) == 9)


if __name__ == "__main__":
     unittest.main()
