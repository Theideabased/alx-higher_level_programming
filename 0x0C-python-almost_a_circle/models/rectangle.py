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
        return self.width * self.height

    def display(self):
        """
        this will display the rectangle in form
        of # on the command line
        all variableust be integer
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(self.x * " " + self.width * "#")

    def __str__(self):
        """
        this is to write the string of a
        given word
        """
        return (f"[Rectangle] ({self.id})  {self.x}/{self.y} \
                - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Method that changed the order of arguments for
        rectangle object
        """
        dict_order = ['id', 'width', 'height', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """
        Method that returns a dictionary with
        attributes of the object
        """
        dict_order = ['x', 'y', 'id', 'height', 'width']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
