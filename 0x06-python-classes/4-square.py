#!/usr/bin/python3
""" a class called Square"""

class Square:
    """represent a square"""

    def __init__(self, size=0):
        """ Instiation a new Square.
        Args:
            size (int): The size of the new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """get the value of the size of the square
        Return:
            __size (int): the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the value for th size of the square"""
        self.__size = value

    def area(self):
        """public instance method called area
        Return:
            area (int): the area of the square
        """
        return self.__size ** 2
