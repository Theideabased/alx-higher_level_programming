#!/usr/bin/python3

""" square class """
from rectangle import Rectangle


class Square(Rectangle):
    """ square ckass inherited from Rectangle """
    
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(self, id, x, y, width, height)
        self.width = size
        self.height = size
