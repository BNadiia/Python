#! /usr/bin/python3

def ui_input():
    return (input("Enter first phrase: "), input("Enter second phrase: "))

def verify_phrases(first_phrase, second_phrase):
    first_letters = list(first_phrase)
    second_letters = list(second_phrase)
    
    if all(elem in first_letters  for elem in second_letters):
        print("Yes, You can create the second prase from the first.")
    else:
        print("No, You cannot create the second prase from the first.")
    

verify_phrases(*ui_input())
