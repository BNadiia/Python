#! /usr/bin/python3

def ui_input():
    return (input("Enter phrase : "))

def verify_palindrome(phrase):
    phrase = phrase.lower()

    symbols = [' ', '\'', '\"', '.', ',', ';', ':', '\\', '*', '!']
    verifyed_phrase = []

    for _ in phrase:
        if _ not in symbols:
            verifyed_phrase.append(_)

    return verifyed_phrase == verifyed_phrase[::-1]

print(verify_palindrome(ui_input()))
