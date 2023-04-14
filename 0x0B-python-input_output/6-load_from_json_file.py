#!/usr/bin/python3
"""
UnJsonification from File
"""
import json


def load_from_json_file(filename):
    """
    UnJsonnify from file
    """
    if len(filename) > 0:
        with open(filename, 'r') as file:
            return (json.load(file))
