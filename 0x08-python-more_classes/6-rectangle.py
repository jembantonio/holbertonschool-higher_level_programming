#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0

    def __init__(self, width=0, height=0):

        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not type(height) is int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise TypeError("height must be >= 0")
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        s = "\n"
        return s.join(("#" * self.__width) for i in range(self.__height))

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
