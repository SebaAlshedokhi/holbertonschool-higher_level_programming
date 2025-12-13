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
        self.width = width
        self.height = height

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

    def area(self):
        """
        returns the current rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        str constructor
        Print the rectangle using the '#' character.
        if width or height is equal to 0, return an empty string
        """
        my_rectangle = ""
        if self.width == 0 or self.height == 0:
            return ""
        for H in range(self.height):
            for W in range(self.width):
                my_rectangle += "#"
            if H != self.height - 1:
                my_rectangle += "\n"
        return my_rectangle

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        my_rectangle = "Rectangle(" + str(self.__width)
        my_rectangle += ", " + str(self.__height) + ")"
        return (my_rectangle)

    def __del__(self):
        """
        Print the message Bye rectangle... 
        when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
