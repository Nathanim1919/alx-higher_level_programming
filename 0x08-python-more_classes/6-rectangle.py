#!/usr/bin/python3
""" defiend a class called Rectangle """

class Rectangle:
    """ instantiate aclass Rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    """public instance method to find the area of rectangle """
    def area(self):
        return self.__height * self.__width

    """ public instance method to find the permeter of ractangle """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)

    """ Returns a string representation of the Rectangle instance """
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
