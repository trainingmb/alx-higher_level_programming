#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for i in a_dictionary.keys():
        if a_dictionary[i] == value:
            a_dictionary.pop(i, 0)
    return a_dictionary
