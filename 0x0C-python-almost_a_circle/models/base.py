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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file"""
        filename = cls.__name__ + ".json"
        text = []
        if list_objs is not None:
            for lst in list_objs:
                text.append(lst.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(Base.to_json_string(text))


    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)