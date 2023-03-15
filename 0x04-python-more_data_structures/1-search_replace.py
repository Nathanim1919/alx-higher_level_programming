#!/usr/bin/python3
def search_replace(my_list, search, replace):
    j = 0
    for i in my_list:
        if i == search:
            my_list[j] = replace
        j+=1
    return my_list
