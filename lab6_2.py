#! /usr/bin/python3

import math
import decimal

def ui_input():
    return decimal.Decimal(input("Enter start sum:")), decimal.Decimal(input("Enter percent:")), int(input("Enter years:"))


def calculate_final_sum(start_sum: decimal.Decimal, percent: decimal.Decimal, years: int):
    percent = (percent / 100) + 1
    for i in range(0,years):
        start_sum *= percent
    return start_sum


def ui_output(final_sum: decimal.Decimal):

    print("Your final sum: {:.2f}".format(final_sum))


ui_output(calculate_final_sum(*ui_input()))
