#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print("", end='')
    else:
        i = len(my_list)- 1
        while i >= 0:
            print("{}".format(my_list[i]))
            i = i - 1