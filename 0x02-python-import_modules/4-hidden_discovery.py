#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    key = "__"

    for name in dir(hidden_4):
        if (name[0:2] != key):
            print("{}".format(name))
