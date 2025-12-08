#!/usr/bin/python3
"""class Square that defines a square."""


class Square:
    """ Instantiation with optional size
    Private instance attributes: size and position """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize square with size and position.
        """
        self.size = size
        self.position = position

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
        Print the square with '#' characters based on size and position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] +"#" * self.__size)

    @property
    def position(self):
        """
        to retrieve the position
        """
        return self.__position
        
    @position.setter
    def position(self, value):
        """
        setter to set the position
        check if it is integer or less than zero
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
