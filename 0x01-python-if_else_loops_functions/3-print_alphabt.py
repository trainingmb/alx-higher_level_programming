#!/usr/bin/python3
i = 97
while i <= 122:
    if i != 113 and i != 101:
        print("{0}".format(chr(i)), end="")
    i = i + 1
