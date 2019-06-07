#!/usr/bin/python3
''' a function that returns the number of lines of a text file
'''


def number_of_lines(filename=""):
    with open(filename, 'r') as file:
        return len(file.readlines())
