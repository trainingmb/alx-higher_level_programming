#!/usr/bin/python3
"""
Say my name please
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>

    Args:
        first_name (str): the first name
        last_name (str): the last name
    """
    err1 = "first_name must be a string"
    err2 = "last_name must be a string"
    say_it = "My name is {} {}"
    if not isinstance(first_name, str):
        raise TypeError(err1)
    if not isinstance(last_name, str):
        raise TypeError(err2)
    print(say_it.format(first_name, last_name))
