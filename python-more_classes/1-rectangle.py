#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """
    defines a rectangle by two private instance attributes
    width and height
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Square instance.
        arguments are width and height
        """
        self.__width = width
        self.__height = height


    @property
    def width(self):
        """
        to retrieve the width
        """
        return self.__width


    @width.setter
    def width(self, value):
        """
        check it integer and greater or equal zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """
        to retrieve the height
        """
        return self.__height


    @height.setter
    def height(self, value):
        """
        check it integer and greater or equal zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
