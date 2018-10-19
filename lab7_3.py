#!/usr/bin/python3

def isClosure(c):
    if c=='(':
        return True
    elif c==')':
        return True
    elif c==']':
        return True
    elif c=='[':
        return True
    elif c=='}':
        return True
    elif c=='{':
        return True
    else:
        return False


def filter(string):
    filtered_string = ''

    for _ in string:
        if isClosure(_):
            filtered_string += _

    return filtered_string


def check(line):
    closures = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    if len(line) % 2 == 1:
        return False

    while line != '':
        flag = True
        i = 0
        for i in range(0, len(line) - 1):
            if line[i] not in closures:
                flag = False
                break
            if closures[line[i]] == line[i + 1]:
                break
        else:
            break

        if not flag:
            break

        line = line[:i] + line[i + 2:]
        print(line)
    else:
        return True
    return False


string = input("Text: ")
print(filter(string))
print(check(filter(string)))