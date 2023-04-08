#!/usr/bin/python3
"""
    this module containe one function 
"""
def print_square(size):
    """ function that prints a square with the character # """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    for j in range(0, size):
        for k in range(0, size):
            print("#",end="" if k < size - 1 else "\n")
            i+=1
