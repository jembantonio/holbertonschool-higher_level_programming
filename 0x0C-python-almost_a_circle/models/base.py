#!/usr/bin/python3
''' Base class module
'''


class Base:
    ''' base class/ parent class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' base class initiation
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns JSON representation of dictionaries
        '''
        if list_dictionaries is None:
            return str([])
        return str(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation list to a file
        '''
        filename = (cls.__name__ + '.json')
        if list_objs is None:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(Base.to_json_string([]))

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(Base.to_json_string([i.to_dictionary()
                                            for i in list_objs]))
