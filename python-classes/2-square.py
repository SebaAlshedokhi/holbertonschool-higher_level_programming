#!/usr/bin/python3
"""
class Square that defines a square
"""

class Square:
    """
    Instantiation with optional size
    Private instance attribute: size
    """

    def __init__(self, size=0):
        """
        size must be an integer,
        otherwise raise a TypeError exception with the message size must be an integer
        if size is less than 0, raise a ValueError exception
        with the message size must be >= 0
        """
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
