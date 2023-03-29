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
         """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        slef.__size = value

    def area(self):
        """public instance method called area"""
        return self.__size ** 2
