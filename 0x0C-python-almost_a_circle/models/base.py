#!/usr/bin/python3
"""
Module:
    Base Class
"""


class Base():
    """
    Docstring for Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
