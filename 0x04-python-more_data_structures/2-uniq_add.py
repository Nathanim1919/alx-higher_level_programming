#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    lists = []
    for i in my_list:
        if i not in lists:
            result += i
            lists.append(i)
    return result
