#!/usr/bin/python3

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))

x = (((a*b)**0.5)/(math.exp(a)*b)) + a*math.exp((2*a)/b)

print("Result: " + str(x))
