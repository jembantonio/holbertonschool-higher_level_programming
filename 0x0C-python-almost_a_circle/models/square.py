#!/usr/bin/python3
''' Square class module
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' class Square which inherits from class Rectangle which inherits from
        class Base
    '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' initializing class square
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' str method used to print properties of square
        '''
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                          self.x,
                                                          self.y,
                                                          self.width))

    @property
    def size(self):
        ''' property getter for size
        '''
        return self.width

    @size.setter
    def size(self, value):
        ''' property setter for size
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' takes arguments and updates the instances using the setter method
        '''
        place = 0
        if (args is not None) and (len(args) > 0):
            for arg in args:
                if place == 0:
                    self.id = arg
                elif place == 1:
                    self.size = arg
                elif place == 2:
                    self.x = arg
                elif place == 3:
                    self.y = arg
                place += 1

        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
