#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    rms = []
    for i in a_dictionary.keys():
        if a_dictionary[i] == value:
            rms.append(i)
    for i in rms:
        a_dictionary.pop(i,0)
    return a_dictionary

