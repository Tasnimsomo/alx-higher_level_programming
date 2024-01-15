#!/usr/bin/python3
""" module for Base class """

import json
import os


class Base:
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        if id is not None, assign the public instance attribute id
        with this argument value - you can assume id is an integer
        and you don’t need to test the type of it
        otherwise, increment __nb_objects and assign the new value
        to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        a = "{}.json".format(cls.__name__)
        with open(a, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        j = []
        if json_string is not None or json_string != '':
            if not isinstance(json_string, str):
                raise TypeError("json_string must be a string")
            j = json.loads(json_string)
        return j

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            instance = cls(width=1, height=1)
        elif cls.__name__ == 'Square':
            instance = cls(size=1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        a = "{}.json".format(cls.__name__)
        instance_list = []
        dictionary_list = []

        if os.path.exists(a):
            with open(a, "r") as f:
                my_str = f.read()
                dictionary_list = cls.from_json_string(my_str)
                for d in dictionary_list:
                    instance_list.append(cls.create(**d))
        return instance_list
