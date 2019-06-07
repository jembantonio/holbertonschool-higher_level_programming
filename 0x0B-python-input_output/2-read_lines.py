#!/usr/bin/python3
'''  function that reads n lines of a text file (UTF8) and prints it to stdout
'''


def read_lines(filename="", nb_lines=0):
    if type(filename) is not str:
        raise TypeError("file should be a string")

    with open(filename, 'r', encoding='utf-8') as file:
        if nb_lines <= 0:
            print(file.read(), end='')
        while nb_lines != 0:
            print(file.readline(), end='')
            nb_lines -= 1
