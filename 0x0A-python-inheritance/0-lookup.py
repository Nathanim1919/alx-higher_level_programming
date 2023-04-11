#!/usr/bin/python3
""" this module containe one function called lookup """

def lookup(obj):
    """ this function returns list of available
        attributes and methods of an object

        Arg: obj
        return: list
    """
    return dir(obj)
