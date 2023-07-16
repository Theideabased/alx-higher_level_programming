#!/usr/bin/python3
""" Reactangle class from Base class """
from base import Base

class Rectangle(Base):
    """ Rectamgle inherited from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        width(int), height(int), x(int), y(int)
        id is from Base
        """
        Base.__init__(self, id=None)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        elif self.__width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        elif self.__height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if not isinstance(self.__x, int):
            raise TypeError('x must be an integer')
        elif self__x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,y):
        if not isinstance(self.__x, int):
            raise TypeError('x must be an integer')
        elif self__x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__y = y
