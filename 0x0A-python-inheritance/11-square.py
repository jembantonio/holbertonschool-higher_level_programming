#!/usr/bin/python3
''' BaseGeometry module
'''


class BaseGeometry:
    ''' class BaseGeometry
    '''
    def area(self):
        ''' instance that raises Exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Validates that value attribute is an integer
        '''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    ''' class Rectangle, inherits attributes from class BaseGeometry
    '''
    def __init__(self, width, height):
        ''' Initialize private instance attributes width and height
        '''
        self.integer_validator("width", width)
        self.integer_validator("length", height)

        self.__width = width
        self.__height = height

    def area(self):
        ''' Returns area of an instance Rectangle
        '''
        return (self.__width * self.__height)

    def __str__(self):
        ''' prints an instance Rectangle info
        '''
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):
    ''' class Square, inherits attributes from class Rectangle
    '''
    def __init__(self, size):
        ''' Initialize size of Square
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' Returns the area of the instance Square
        '''
        return (self.__size ** 2)

    def __str__(self):
        ''' Prints an instance of Square info
        '''
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
