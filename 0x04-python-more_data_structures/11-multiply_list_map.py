#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = list(my_list)
    return [x*number for x in new_list]
