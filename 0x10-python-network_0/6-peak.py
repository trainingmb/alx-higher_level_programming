#!/usr/bin/python3
"""Find a peak"""

def find_peak(l):
    """Find the First peak from the left
    """
    if len(l) < 1:
        return None
    m = l[0]
    for i in range(1, len(l)):
        if l[i] >= m:
            m = l[i]
        else:
            return m
    return m
