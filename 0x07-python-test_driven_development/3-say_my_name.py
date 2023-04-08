#!/usr/bin/python3
""""
    this is 3-say_my_name module and it includes one function
"""

def say_my_name(first_name, last_name=""):
    """ prints my name is <first name> <last name>"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name")
