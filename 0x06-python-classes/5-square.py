#!/usr/bin/python3
class Square:
    '''Sqaure class

    Attributes:
    __size - the size of the square
    '''
    def __init__(self, size=0):
        '''Initialiazing class

        Arguments:
        self: the object itself
        size (int): size of the square

        Return: None
        '''
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Area method to calculate the area of a square

        Arguments:
        self - the object itself

        Return: area of square
        '''
        return self.__size**2

    @property
    def size(self):
        '''Size method to get size

        Arguments:
        self - the object itself

        Return: size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Size method to set size

        Arguments:
        self - the object itself
        value - value to change the size size to

        Returns: new size of the square
        '''
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''Print method to print square

        Arguments:
        self - the object itself

        Returns: None
        '''
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
