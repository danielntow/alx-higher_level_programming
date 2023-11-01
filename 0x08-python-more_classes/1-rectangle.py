#!/usr/bin/python3
"""
module that defines a rectangle
"""


class Rectangle:
    """
    Represents a basic Rectangle.

    """

    def __init__(self, width=0, height=0) -> None:
        """
        Initializes a Rectangle object.

        Parameters:
        -----------
        width : int, optional
            Width of the rectangle (default is 0).
        height : int, optional
            Height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(self.value, int):
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
    ----------
    __width : int
        Private attribute to store the width of the rectangle.
    __height : int
        Private attribute to store the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object.

        Parameters:
        -----------
        width : int, optional
            Width of the rectangle (default is 0).
        height : int, optional
            Height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
