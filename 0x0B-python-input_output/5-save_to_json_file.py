#!/usr/bin/python3
"""
Jsonification Into File
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Jsonnify into file
    """
    if len(filename) > 0:
        with open(filename, 'wb') as file:
            return (json.dump(my_obj, file))
