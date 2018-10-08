#! /usr/bin/python3

def ui_input():
    return (input("Enter phrase : "))

def count_vowel(phrase):
    phrase = phrase.lower()
    vowel = ['a','o','u','i','e','y',]
    number = 0

    for _ in vowel:
        number += phrase.count(_)

    return number

def ui_output(number):
    print("There are " + str(number) + " vowel")

ui_output(count_vowel(ui_input()))

