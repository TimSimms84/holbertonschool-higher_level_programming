#!/usr/bin/python3
"""
Student class that defines a student by public: firstname, listname, age
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary representation of a Student instance
         """
        if not attrs:
            return vars(self)
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except Exception:
                pass
        return new_dict
