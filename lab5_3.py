#!/usr/bin/python3

import random

print("1.Rock")
print("2.Scissors")
print("3.Paper")

us = int(input("Enter your choice: "))

pc = random.randrange(1, 3)
print("Computer's choice is: " + str(pc))

if (us == 1 and pc == 2) or (us == 2 and pc == 3) or (us == 3 and pc == 1):
    print("You win!")
elif (pc == 1 and us == 2) or (pc == 2 and us == 3) or (pc == 3 and us == 1):
    print("Computer win!")
elif pc == us:
    print("Your choices are equal, try again.")
else:
    print("You can choice only 1, 2 or 3. Try again.")
