#!/usr/bin/python3
'''is_same_class module
'''


def is_same_class(obj, a_class):
    ''' returns true if object is exactly an instance of the class
    '''
    return True if type(obj) is a_class else False
