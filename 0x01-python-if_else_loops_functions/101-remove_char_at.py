#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = str
    if (n == 0):
        newstr = newstr[1:]
    elif (n == (len(str) - 1)):
        newstr = newstr[:-1]
    else:
        newstr = newstr[:n]+""+newstr[n+1:]
    return newstr
