#!/usr/bin/python3
''' Student module
'''


class Student:
    ''' initializes student class
    '''
    def __init__(self, first_name, last_name, age):
        if type(first_name) is not str:
            raise TypeError("first_name must be type str")
        if type(last_name) is not str:
            raise TypeError("last_name must be type str")
        if type(age) is not int:
            raise TypeError("last_name must be type int")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' retrieves dict of student instance
        '''
        return self.__dict__
