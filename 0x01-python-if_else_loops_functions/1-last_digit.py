#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number % 10)
if n > 5:
    print(f"{n} is greater than 5")
elif n == 0:
    print(f"{n} is 0")
else:
    print(f"{n}is less than 6 and not 0")
