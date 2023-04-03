#!/usr/bin/python3
""" defiend a class called Rectangle """

class Rectangle:
    """ instantiate aclass Rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ return the value of width"""
    @property
    def width(self):
        return self.__width

    """ set the value of width """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """ return the value of height """
    @property
    def height(self):
        return self.__height
    """ set the value of height """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
