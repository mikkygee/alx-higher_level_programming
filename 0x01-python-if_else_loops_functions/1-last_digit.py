#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastd = number % 10
print("Last digit of {:d} is ".format(number), end="")

if lastd > 5:
    print("{:d} and is greater than 5" .format(lastd))
elif lastd == 0:
    print("{:d} and is 0" .format(lastd))
else:
    print("{:d} and is less than 6 and not 0" .format(lastd))
