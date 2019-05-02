#!/usr/bin/python3
import sys

if __name__ == '__main__':
    ac = len(sys.argv) - 1

    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("1 argument:")
        print("{}: {}".format(ac, sys.argv[1]))
    else:
        print("{} arguments:".format(ac))
        for i in range(1, ac):
            print("{}: {}".format(i, sys.argv[i]))
