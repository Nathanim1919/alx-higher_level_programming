#!/usr/bin/python3
""" a module that contains is_kind_of_class function """
def is_kind_of_class(obj, a_class):
    """
    -checks if an object is an instance of , or if the object is an insatnce of a class that inhirited from.

    Args:
    -obj: an object
    a_class: a class

    Returns:
    -true if an object is an instance of , or if the object is an instance of a class that inhirited from otherwise false.

    """
    return isinstance(obj, a_class)
