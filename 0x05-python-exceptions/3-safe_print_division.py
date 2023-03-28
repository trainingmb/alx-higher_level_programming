#!/usr/bin/python3

def safe_print_division(a, b):
    c = 0
    i = 0
    try:
        c = a / b
    except:
        c = None
        print("Inside result: {}".format(c))
    finally:
        return c
