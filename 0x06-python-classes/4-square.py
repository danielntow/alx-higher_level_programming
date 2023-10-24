#!/usr/bin/python3
"""
This is a module for defining a Square class.
"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square .
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """retrieve the size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """
        set
        Args:
            value (int): size of square

        Raises:
            TypeError:
            ValueError:

        Returns:
            int: size of square
        """

        self.__size = value


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """retrieve the size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """
        set
        Args:
            value (int): size of square

        Raises:
            TypeError:
            ValueError:

        Returns:
            int: size of square
        """

        self.__size = value
