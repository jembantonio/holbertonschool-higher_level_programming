#!/usr/bin/python3
class Square:
    '''Sqaure class

    Attributes:
    self - the object itself
    __size - the size of the square
    position - coordinates of the square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialiazing class

        Arguments:
        self: the object itself
        size (int): size of the square
        position (tuple): coordinates of the square

        Return: None
        '''
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not type(position) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not type(position[0]) is int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not type(position[1]) is int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
        if self.__size == 0:
            print()

    @property
    def position(self):
        '''Position method to get coordinates

        Arguments:
        self - the object itself

        Return: coordinates of the square
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''Position method to set coordinates

        Arguments:
        self - the object itself
        value (tuple) - new value of the coordinates

        Return: None
        '''
        if not type(position) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not type(position[0]) is int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not type(position[1]) is int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
