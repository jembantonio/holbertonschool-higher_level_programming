#!/usr/bin/python3
''' MyInt module
'''


class MyInt(int):
    ''' class MyInt, inherits attributes from class int
    '''
    def __init__(self, value):
        ''' Init method value with MyInt class
        '''
        if type(value) is not int:
            raise TypeError("must be an integer")
        self.__value = value

    def __eq__(self, other):
        return not (self._value == other)

    def __ne__(self, other):
        return not (self.__value != other)
