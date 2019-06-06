#!/usr/bin/python3
''' is_kind_of_class module
'''


def is_kind_of_class(obj, a_class):
    ''' returns True if the object is an instance of, or if
    the object is an instance of class that inherited from,
    the class
    '''
    return True if isinstance(obj, a_class) is True else False
