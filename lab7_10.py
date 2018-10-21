#! /usr/bin/python3

def ui_input():
    return (input("Enter phrase: "))

def is_the_shortest(phrase):
    
    words = phrase.split()
    the_shortest = min(words, key = len)
      
    return the_shortest


def ui_output(the_shortest):
    print("The shortest word is: " + str(the_shortest))

ui_output(is_the_shortest(ui_input()))
