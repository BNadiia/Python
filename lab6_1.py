#! /usr/bin/python3

import math


def ui_input():
    """This function make input for 3 sides of triangle."""
    return float(input("Enter a:")), float(input("Enter b:")), float(input("Enter c:"))


def calculate_area(a: float, b: float, c: float):
    """This function calculates and returns area of triangle."""
    p = (a + b + c) / 2.0
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


def ui_output(area: float):
    """This function print area of triangle."""
    print("The area of triangle: " + str(area))


A, B, C = ui_input()

ui_output(calculate_area(A, B, C))
