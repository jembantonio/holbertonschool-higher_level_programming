#!/usr/bin/python3
''' inherits_from module
'''


def inherits_from(obj, a_class):
    ''' returns True if the object is an instance of a class that
    inherited from the specified class
    '''
    return False if type(obj) == a_class else True
