#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except BaseException as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return None
