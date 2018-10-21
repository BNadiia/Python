#! /usr/bin/python3

def ui_input():
    return (input("Enter phrase: "))

def delete_space(phrase):
    words = phrase.split()
    changed_phrase = ''
    
    for i in words:
        changed_phrase += " " + str(i)
        
    return changed_phrase


def ui_output(changed_phrase):
    print("The filtered phrase is: " + str(changed_phrase))
    

ui_output(delete_space(ui_input()))
