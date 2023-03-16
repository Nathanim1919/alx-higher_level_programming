#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp = dict(a_dictionary)
    for key, value in a_dictionary:
        temp[key] = value * 2
    return temp
