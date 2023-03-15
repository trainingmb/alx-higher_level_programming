#!/usr/bin/python3


def best_score(a_dictionary):
    kys = list(a_dictionary.keys())
    if len(kys) < 1:
        return None
    bsk = kys[0]
    for i in kys:
        if a_dictionary[i] > a_dictionary[bsk]:
            bsk = i
    return bsk
