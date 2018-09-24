#!/usr/bin/python3

import math
import cmath

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

x1 = x2 = 0

if a == 0:
    if b == 0:
        x1 = x2 = - c
    else:
        x1 = x2 = -c / b
else:
    d = b**2 - 4*a*c
    if d < 0:
        x1 = (- b + 0j * cmath.sqrt(d)) / (2 * a)
        x2 = (- b - 0j * cmath.sqrt(d)) / (2 * a)
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
    else:
        x1 = x2 = -b / (2 * a)

print("x1: " + str(x1))
print("x2: " + str(x2))