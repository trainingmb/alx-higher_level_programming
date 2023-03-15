#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    kys = sorted(a_dictionary.keys())
    for i in kys:
        print(i, end=": ")
        print(a_dictionary[i])
