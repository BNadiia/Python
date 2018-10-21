#! /usr/bin/python3

def ui_input():
    return (input("Enter phrase: "))

def sort_words(phrase):
    words = phrase.split()
    sorted_words = sorted(words, key=len)
    
    changed_phrase = ''
    for i in sorted_words:
        changed_phrase += " " + str(i)
        
    return changed_phrase


def ui_output(changed_phrase):
    print("The sorted phrase is: " + str(changed_phrase))
    

ui_output(sort_words(ui_input()))
