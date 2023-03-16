#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if len(a_dictionary.keys() == 0):
        return None
    else:
        for key, value in a_dictionary.items():
            if a_dictionary[key] > max:
                max = value
        return max
