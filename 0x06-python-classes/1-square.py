#!/usr/bin/python3
"""
This is a module for defining a Square class.
"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (no type/value verification).
        """
        self.__size = size
