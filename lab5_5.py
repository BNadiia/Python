#!/usr/bin/env python3

def is_prime(num):
    count = 0
    i = 1
    while i != num + 1:
        if num % i == 0:
            count += 1
        i += 1
    return count == 2


number = int(input('Enter a number: '))

print(is_prime(number))