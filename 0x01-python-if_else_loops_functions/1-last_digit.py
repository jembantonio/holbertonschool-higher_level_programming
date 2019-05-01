#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_num = number % 10
else:
    last_num = (number % -10)

if last_num > 5:
    message = "greater than 5"
elif last_num == 0:
    message = "0"
else:
    message = "less than 6 and not 0"

print("Last digit of {} is {} and is {}".format(number, last_num, message))
