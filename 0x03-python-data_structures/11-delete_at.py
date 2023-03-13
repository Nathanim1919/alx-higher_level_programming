#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []

    if idx >= 0 and idx < len(my_list):
        for i in my_list:
            if (i != my_list[idx]):
                new_list.append(i)
        return new_list
    else:
        return my_list
