#!/usr/bin/python3
""" class to get index """


class Base:
    """
    initializing object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        self(int)
        id(int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
