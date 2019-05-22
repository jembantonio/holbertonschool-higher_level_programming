#!/usr/bin/python3
class Square:
    '''A square class for the size of a square

    Attributes:
        __size: size of the square
    '''

    def __init__(self, size=0):
        '''Initialize class

        Arguments:
        self: the object itself
        size (int): size of the square

        Return: None
        '''
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
