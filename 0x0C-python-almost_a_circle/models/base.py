#!/usr/bin/python3
""" class to get index """


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        """
        self(int)
        id(int)
        """
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
