#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Instantiation with optional size
    Private instance attribute: size"""

    def __init__(self, size):
        """
        Initializes a new Square instance.
        size: The size (side length) of the square.
        """
        self.__size = size
