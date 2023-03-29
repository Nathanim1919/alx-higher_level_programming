#!/usr/bin/python3

""" a class called Square"""

class Square:
    """instation of size attributes"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
