#! /usr/bin/python3

def ui_input():
    return (input("Enter phrase : "))



def ui_output(phrase):
    print('*' * (len(phrase) + 4))
    print('* ' + phrase + ' *')
    print('*' * (len(phrase) + 4))


ui_output(ui_input())

