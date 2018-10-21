#! /usr/bin/python3

def ui_input():
    return (input("Enter phrase: "))

def is_the_shortest(phrase):
    
    words = phrase.split()
    the_shortest = min(words, key = len)
    len_of_the_shortest = len(the_shortest)
     
    return the_shortest, len_of_the_shortest


def ui_output(the_shortest, len_of_the_shortest):
    print("The shortest word is: " + str(the_shortest))
    print("Length of the shortest word is: " + str(len_of_the_shortest))

ui_output(*is_the_shortest(ui_input()))
