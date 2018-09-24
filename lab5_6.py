#!/usr/bin/python3

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


if a + b > c and b + c > a and c + a > b:
    print("This triangle can exist")
else:
    print("This triangle cannot exist")