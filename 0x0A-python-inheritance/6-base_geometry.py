#!/usr/bin/python3
""" this module containe a class called BaseGeometry """

class BaseGeometry:

    """ 
    -Base class for geometry objects.

    """

    def area(self):

        """
        calculate the are of the geomtry object.

        Raises:
        - NotImplementedError: if the method is not implemented by the subclass.
        """
        raise NotImplementedError("area() is not implemented")
