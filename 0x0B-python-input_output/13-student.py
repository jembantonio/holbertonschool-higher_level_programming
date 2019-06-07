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

    def to_json(self, attrs=None):
        ''' retrieves dict of student instance
        '''
        if attrs is None:
            return self.__dict__
        if type(attrs) is not list:
            return self.__dict__
        return{i: self.__dict__[i] for i in attrs if i in self.__dict__.keys()}

    def reload_from_json(self, json):
        ''' replaces all attributes of the Student instance
        '''
        for key, value in json.items():
            setattr(self, key, value)
