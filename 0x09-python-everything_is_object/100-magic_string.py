#!/usr/bin/python3
def magic_string():
    magic_string.iters = getattr(magic_string, 'iters', 0) + 1
    print("BestSchool" + (", BestSchool" * (magic_string.iters-1)))
