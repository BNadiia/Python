#!/usr/bin/env python3
arr = [int(x) for x in input("Enter list of number: " ).split()] 

arr.sort()
s = 0
for x in arr:
  s = s + x
s /= arr.__len__();

m = 0

if arr.__len__() % 2 == 0:
  m = (arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]) / 2
else:
  m = arr[len(arr) // 2]

print("Average value: ", s);
print("Median: ", m);
