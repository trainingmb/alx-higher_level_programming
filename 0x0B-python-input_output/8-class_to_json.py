#!/usr/bin/python3
"""
Jsonification of Class
"""
import json


def class_to_json(obj):
    """
    Jsonnify of Class
    """
    return (json.dumps(my_obj.__dict__))
