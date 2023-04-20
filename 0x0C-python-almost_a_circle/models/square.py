#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle"""

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
        """Getter method for size property"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter method for size property"""
        self.__size = value
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes based on args and kwargs"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
