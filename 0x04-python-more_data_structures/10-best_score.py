#!/usr/bin/python3
def best_score(a_dictionary):
    best = ''
    max = 0
    if len(a_dictionary.keys() == 0):
        return None
    for key, value in a_dictionary.items():
        if a_dictionary[key] > max:
            max = value
            best = key
    return best
