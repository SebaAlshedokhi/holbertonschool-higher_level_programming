#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """ Instantiation with optional size
    Private instance attribute: size """
    def __init__(self, size=0):
        """
        initializating size
        """
        self.__size = size

    @property
    def size(self):
        """
        to retrieve the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter to set the size
        check if it is integer or less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the current square area
        """
        return self.__size ** 2
        
    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
