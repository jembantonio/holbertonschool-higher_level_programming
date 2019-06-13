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

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the json string representation
        '''
        empty_list = "[]"
        if json_string is None:
            if len(json_string) == 0:
                return empty_list
        return eval(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' creates a dummy instance with all its attributes set
        '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        if dummy is not None:
            dummy.update(**dictionary)
        return dummy
