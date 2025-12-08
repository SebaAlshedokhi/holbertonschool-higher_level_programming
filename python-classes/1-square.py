#!/usr/bin/python3
"""
a class Square that defines a square by: (based on 0-square.py)
"""

class Square:
    """
    Defines a square object with a private size attribute.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size (side length) of the square.
        """
        self.__size = size
