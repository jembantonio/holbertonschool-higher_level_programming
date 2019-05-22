#!/usr/bin/python3
class Square:
    '''Square class

    Attributes:
        __size: size of the square
    '''

    def __init__(self, size=0):
        '''Initialize class

        Arguments:
        self: the object itself
        size (int): size of the Square

        Return: None
        '''
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''Area method to calculate the area of the given square

        Arguments:
        self - the object itself

        Return: area of the Square
        '''
        return self.__size**2
