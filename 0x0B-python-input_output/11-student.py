#!/usr/bin/python3
"""
Student class.
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
        true_dict = (self.__dict__)
        if isinstance(attrs, list) and
        all([isinstance(i, str) for i in attrs]):
            false_dict = {}
            for s in attrs:
                if s in true_dict.keys():
                    false_dict[s] = true_dict[s]
            return (false_dict)
        else:
            return (true_dict)

    def reload_from_json(self, json):
        for key, value in json.items():
            if key == 'first_name':
                self.first_name = value
            elif key == 'last_name':
                self.last_name = value
            elif key == 'age':
                self.age = value
