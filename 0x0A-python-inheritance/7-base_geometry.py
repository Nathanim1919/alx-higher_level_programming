#!/usr/bin/python3
""" a module includes abase class BaseGeometry """

class BaseGeometry:
    """ abase class """

    def area(self):
        """
        calculates the area of geometry

        Raises:
        - NotImplementedError

        """
        raise NotImplementedError("area() is not implemented")
    def integer_validator(self, name, value):
        """
        an integer validator public instance method

        Args:
        - name: always string type
        - value: an integer type

        Raise:
        - TypeError: if value is not instance of int
        - ValueError: if value if lessthan or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0")
