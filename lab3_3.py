#! /usr/bin/python3

height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))

bmi = weight/height**2

print("Your BMI: " + str(bmi))
