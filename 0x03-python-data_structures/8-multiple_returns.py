#!/usr/bin/python3


def multiple_returns(sentence):
    if (sentence is None) or (len(sentence) < 1):
        return (0, None)
    return (len(sentence), sentence[0])
