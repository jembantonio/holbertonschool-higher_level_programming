#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx > len(new_list) or new_list is None or idx is None
    or element is None:
        return new_list
    new_list[idx] = element
    return new_list
