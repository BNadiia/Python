#!/usr/bin/python3

n = int(input("Enter a: "))

print(n != 0 and ((n & (n - 1)) == 0))
