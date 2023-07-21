#!/usr/bin/python3
""" Rectangle class from Base class """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle inherited from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        width(int), height(int), x(int), y(int)
        id is from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ the getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ the width setter """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """ this will return the are if the rectangle
        from the height and width

        Args:(width and height)
        """
        return self.__width * self.__height

    def display(self):
        """
        this will display the rectangle in form
        of # on the command line
        all variableust be integer
        """
        print("\n" * self.__y)
        for i in range(self.__height):
            print(self.__x * " " + self.__width * "#")

    def __str__(self):
        """
        this is to write the string of a
        given word
        """
        return f"[Rectangle] {self.__x}/{self.__y} \
                - {self.__width}/{self.__height}"
