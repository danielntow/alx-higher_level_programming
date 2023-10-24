#!/usr/bin/python3
"""
This is a module for defining a Square class.
"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (any):
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        self._position = position

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter method for setting the size attribute.

        Args:
            value (int): The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Args:
            value (int): The size of the square.
        """

        self.__init__(value)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def my_print(self):
        """
        Prints the area of the square as #

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self._position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self._position[0] + "#" * self.__size)
