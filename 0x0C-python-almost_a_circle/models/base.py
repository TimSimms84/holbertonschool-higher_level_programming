#!/usr/bin/python3
"""base class
"""
import json


class Base:
    """base class for almost a circle"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns json representation of a string
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
         writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        jstring = []
        if list_objs is not None:
            for i in list_objs:
                jstring.append(cls.to_dictionary(i))
        with open(filename, "w") as file:
            file.write(cls.to_json_string(jstring))
