#!/usr/bin/python3

""" square class """
from rectangle import Rectangle


class Square(Rectangle):
    """ square ckass inherited from Rectangle """
    
    def __init__(self, size, x=0, y=0, id=None):
        """
        Method that initialized the square
        args:
        size: side's size of the square
        x: position on x axis.
        y: position on y axis.
        """
        super().__init__(id, x, y, size, size)
    
    def __str__(self):
        """
        Method that returns a string
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,\
                 self.y, self.width))

    @property
    def size(self):
        """
        Getter the size of the square
        """
        return self.width
   
    @size.setter
    def size(self, value):
        """
        setter the size of the square
        value: size to assign
        """
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """
        Method that update arguments for square object
        *args: list of arguments.
        """
        dict_order = ['id', 'size', 'x', 'y']
        if args id not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in  dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """
        Method that returns the dictionary
        representation of a square
        """
        dict_order = ['id', 'x', 'size', 'y']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs

