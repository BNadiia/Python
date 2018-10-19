#! /usr/bin/python3

def ui_input():
    return (input("Enter phrase: "))



def shift(phrase):
    changed_phrase = ''
    for i in phrase:

#        if i=='z':
#            changed_phrase += 'a'
#            continue
#        if i=='Z':
#            changed_phrase += 'A'
#            continue
#        changed_phrase += chr(ord(i) + 1)

        changed_phrase += 'a' if i == 'z' else 'A' if i == 'Z' else chr(ord(i) + 1)


    return changed_phrase



def ui_output(changed_phrase):
    print("Changed phrase: " + str(changed_phrase))

ui_output(shift(ui_input()))