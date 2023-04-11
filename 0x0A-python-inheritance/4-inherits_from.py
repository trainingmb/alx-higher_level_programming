#!/usr/bin/python3
"""
issubclass Module
"""


def inherits_from(obj, a_class):
    """
    Is subclass of class a_class
    """
    return issubclass(type(obj), a_class)
