#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    cpy = {}
    for i in a_dictionary.keys():
        cpy[i] = a_dictionary[i] * 2
    return cpy
