#! /usr/bin/python3

def ui_input():
    return (int(input("Enter quantity of people: ")), int(input("Enter step: ")))


def kill_nth(people_quantity, step):
    people_list = list(range(1, people_quantity + 1))
    print(people_list)

    i = 0
    while(len(people_list) != 1 ):
        i += 1
        first_elem = people_list.pop(0)
        if i % step:
            people_list.append(first_elem)
    print(people_list)



kill_nth(*ui_input())