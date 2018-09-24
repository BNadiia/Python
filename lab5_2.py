#!/usr/bin/python3

h = int(input("Enter height of the door: "))
w = int(input("Enter width  of the door: "))

a = int(input("Enter height of the box: "))
b = int(input("Enter width of the box: "))
c = int(input("Enter length of the box: "))

if (a <= h or a <= w) and (b <= h or b <= w):
    print("You can fit the box through the door")

elif (a <= h or a <= w) and (c <= h or c <= w):
    print("You can fit the box through the door")

elif (b <= h or b <= w) and (c <= h or c <= w):
    print("You can fit the box through the door")

else: print("You cannot fit the box through the door")
