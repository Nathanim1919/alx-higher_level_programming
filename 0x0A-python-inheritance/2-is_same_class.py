#!/usr/bin/python3
""" module that contains one function """
def is_same_class(obj, a_class):
    """ 
    check if the given object is an instance of the specified class.

        Arg:
        -obj: an object
        -class: a class or type
       
       Returns:
            - True if obj is an instance of class, false otherwise
    """
    return type(obj) is a_class
