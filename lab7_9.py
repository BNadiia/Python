#!/usr/bin/python3

line = input("Enter ticket number: ")

left_sum = 0
right_sum = 0

for i in range(0,len(line) // 2):
  left_sum += int(line[i])
  right_sum += int(line[-(i+1)])

if left_sum == right_sum:
  print("It's lucky ticket:)")
else:
  print("It's unlucky ticket:(")