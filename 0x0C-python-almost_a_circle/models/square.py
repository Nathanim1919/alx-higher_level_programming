#!/usr/bin/python3
"""this module inherits from Rectangle class the Base module"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class that defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size
    
    def __str__(self):
        """Returns string representation of the object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    

    @property
    def size(self):
        """getter method fro size property"""
        return self.__size
    

    @size.setter
    def size(self, value):
        """ setter for size property"""
        self.__size = value
        self.width = value
        self.height = value