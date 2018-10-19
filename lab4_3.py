#!/usr/bin/env python3

import decimal

income = decimal.Decimal(input('Enter your income: '))

tax = income * decimal.Decimal('0.18')
mil_tax = income * decimal.Decimal('0.015')

summary_tax = decimal.Decimal(tax) + decimal.Decimal(mil_tax)

print('Tax = ', tax, 'Military tax = ', mil_tax)
print('Summary tax = ', summary_tax)