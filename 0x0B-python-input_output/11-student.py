#!/usr/bin/python3
"""
Student class.

"""


class Student:
    """
    Student class
    Converts to a dict json
    Converts from a json dict
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with:
        first_name,
        last_name
        age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py):
        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        true_dict = (self.__dict__)
        if isinstance(attrs, list):
            if all([isinstance(i, str) for i in attrs]):
                false_dict = {}
                for s in attrs:
                    if s in true_dict.keys():
                        false_dict[s] = true_dict[s]
                return (false_dict)
        else:
            return (true_dict)

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public
        attribute
        """
        for key, value in json.items():
            if key == 'first_name':
                self.first_name = value
            elif key == 'last_name':
                self.last_name = value
            elif key == 'age':
                self.age = value
