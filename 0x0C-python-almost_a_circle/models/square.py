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
