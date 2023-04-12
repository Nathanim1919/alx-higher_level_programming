#!/usr/bin/python3
""" this module containes one function called inherits_from(obj, a_class)"""

def inherits_from(obj, a_class):
    """
    -checks if the object is an instance of a class that inherited from the specified class.

    Args:
    -obj: an object
    -a_class: a class or type

    Returns:
    -True if an object is an instance of a class that inhirited from the specified class.
    """
    if issubclass(type(obj), a_class):
        return True

    for base_class in type(obj).__bases__:
        if inherits_from(base_class, a_class):
            return True
    return False
