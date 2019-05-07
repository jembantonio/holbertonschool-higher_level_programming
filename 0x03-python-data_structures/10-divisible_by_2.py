#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is None:
        return

    div_two = []
    for num in my_list:
        if (num % 2 == 0):
            div_two.append(True)
        else:
            div_two.append(False)

    return div_two
