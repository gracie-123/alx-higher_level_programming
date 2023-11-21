#!/usr/bin/python3

class Square:
    """ A Square class """
    def __init__(self, size=0):
        """ initialize square with a specific size
        Args:
            __size: size of the square
        """
        self.__size = size

    def area(self):
        """ compute the area of a square
        Return:
            the area
        """
        return self.__size ** 2

    @property
    def size(self):
        """ getter method for the __size private instance
            attribute

        Return:
            __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for the __size private instance
            attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ prints a square using the character #
            if size is 0, prints a blank line
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
