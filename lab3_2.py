#! /usr/bin/python3

zero_f = 32
boiling_f = 212
boiling_c = 100

k = (boiling_f - zero_f)/boiling_c

temperature_fahrenheit = int(input("Enter temperature in F: "))

temperature_celsius =  (temperature_fahrenheit - zero_f) / k

print("Temperature in Celsius: " + str(temperature_celsius))

