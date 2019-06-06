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
