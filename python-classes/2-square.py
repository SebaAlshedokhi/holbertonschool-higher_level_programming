#!/usr/bin/python3
"""class Square that defines a square"""

class Square:
    """
    Instantiation with optional size
    Private instance attribute: size
    """

    def __init__(self, size=0):
        """
        check size if integer or not
        then check size if less than zero
        then assign size
        """
        if not isinstance(size, int)
            raise TypeError("size must be an integer")
            break
        if size < 0:
            raise ValueError("size must be >= 0")
            break
        self.__size = size
