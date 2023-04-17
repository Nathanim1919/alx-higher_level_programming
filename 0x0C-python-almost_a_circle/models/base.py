#!/usr/bin/python3
""" this modlue icludes one base class"""


class Base:
    """
    A base class to manage the id attribute in all future classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
