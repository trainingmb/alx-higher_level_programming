#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    rms = []
    for i in a_dictionary.keys():
        if a_dictionary[i] == value:
            rms.append(i)
    for i in rms:
        del a_dictionary[i]
    return(a_dictionary)
