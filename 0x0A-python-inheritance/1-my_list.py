#!/usr/bin/python3
""" this module contains two classes"""

class list:
    """" abase class called list"""
    pass

class MyList(list):
    """ child class called MyList"""

    def print_sorted(self):
        return sorted(dir(self))
