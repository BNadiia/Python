#! /usr/bin/python3

import math
import decimal

def ui_input():
    return decimal.Decimal(input("Enter start sum:")), decimal.Decimal(input("Enter percent:")), decimal.Decimal(input("Enter final sum:"))


def calculate_final_sum(start_sum: decimal.Decimal, percent: decimal.Decimal, final_sum: decimal.Decimal):
    percent = (percent / 100) + 1
    years = 0
    while start_sum < final_sum:
        start_sum *= percent
        years += 1
    return years


def ui_output(years: int):

    print("You'll get final sum in " + str(years) + " years")


ui_output(calculate_final_sum(*ui_input()))
