#!/usr/bin/python3
i = 0
while i < 8:
    j = i + 1
    while j <= 9:
        print("{}{}, ".format(i, j), end="")
        j = j + 1
    i = i + 1

print("89")
