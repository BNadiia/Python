#! /usr/bin/python3

def ui_input():
    return (input("Enter phrase: ")), (int(input("Enter number shift: ")))

def shift(phrase, number):
    if number > len(phrase)/2:
        print('Enter another number shift.')
        exit()
    changed_phrase = phrase[number:] + phrase[:number]
    return changed_phrase

def ui_output(changed_phrase):
    print("Changed phrase: " + str(changed_phrase))

ui_output(shift(*ui_input()))

