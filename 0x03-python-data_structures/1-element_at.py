#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list is None:
        return
    if idx is None:
        return
    if idx < 0:
        return
    if idx >= len(my_list):
        return
    else:
        return my_list[idx]
