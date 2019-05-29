#!/usr/bin/python3
'''
add_integer

This module adds two ints and/or floats
'''


def add_integer(a, b=98):
    '''add_integer function adds (a) and (b)
    Return: sum of (a) and (b)
    '''
    if not type(a) is int:
        if not type(a) is float:
            raise TypeError("a must be an integer")
    if not type(b) is int:
        if not type(b) is float:
            raise TypeError("b must be an integer")
    return (int(a) + int(b))
