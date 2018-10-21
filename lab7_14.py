#! /usr/bin/python3

def ui_input():
    return (input("Enter email: "))


def verify_email(email):
    parts = email.split('@')
    if len(parts) != 2:
        return False
        
    parts = parts[1].split('.')
    if len(parts) != 2:
        return False
    if len(parts[0]) < 2 or len(parts[1]) < 2:
        return False
    return True


if verify_email(ui_input()):
    print("It's correct email.")
else:
    print("It's incorrect email")
