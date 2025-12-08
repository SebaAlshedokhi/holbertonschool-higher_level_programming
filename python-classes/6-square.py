#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """ Instantiation with optional size
    Private instance attributes: size and position """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializating size
        """
        self.__size = size
        self.__position = position

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
        """Print the square using the '#' character.

        If size is 0, prints an empty line. Otherwise, prints a square
        pattern using '#' characters where each side has length equal to size.
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
        if not isinstance(self.value, int) or len(self.value) != 2:
            if self.value[0] < 0 or self.value[0] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
