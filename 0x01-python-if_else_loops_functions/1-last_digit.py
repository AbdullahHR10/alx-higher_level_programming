#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = number % 10 if number >= 0 else (number % 10) - 10
if lastnum > 5:
    print(f"Last digit of {number} is {lastnum} and is greater than 5")
elif lastnum == 0:
    print(f"Last digit of {number} is {lastnum} and is 0")
elif lastnum < 6 and lastnum != 0:
    print(f"Last digit of {number} is {lastnum} and is less than 6 and not 0")
