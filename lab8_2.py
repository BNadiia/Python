#! /usr/bin/python3

import random

def insertionsort(A):
   
    for j in range(1,len(A)):
        key = A[j]
        i = j-1

        while (i > -1) and key < A[i]:
            A[i+1]=A[i] 
            i=i-1 
        A[i+1] = key

    return A

def rand_numbers(size: int) -> list:
    return [random.randint(0, 10) for _ in range(size)]

numbers = rand_numbers(15)
print(numbers)

insertionsort(numbers)
print(numbers)
