#!/usr/bin/python3
''' Square class module
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' class Square which inherits from class Rectangle which inherits from
        class Base
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
