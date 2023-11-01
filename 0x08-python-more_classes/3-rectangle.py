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

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join(
                ['#' * self.__width for _ in range(self.__height)])

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return '\n'.join(
            '#' * self.__width for _ in range(self.__height)
        ) if self.__width != 0 and self.__height != 0 else ""

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return '\n'.join(
            ['#' * self.__width for _ in range(self.__height)]
        ) if self.__width != 0 and self.__height != 0 else ""

    def __str__(self) -> str:
        """Returns a string representation of the rectangle."""
        if self.__height == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join(['#' * self.__width] * self.__height)


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

    def __init__(self, width=0, height=0) -> None:
        """
        Initializes a Rectangle object.

        Parameters:
        -----------
        width : int, optional
            Width of the rectangle (default is 0).
        height : int, optional
            Height of the rectangle (default is 0).

        Raises:
            TypeError: if width is not integer
            ValueError: if height is less than zero
        """
        self.width = width
        self.height = height

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

    def area(self):
        """ Claculates Area of Rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""

        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """Returns a string representation of the rectangle."""
        if self.__height == 0 or self.__height == 0:
            return str()
        else:
            return '\n'.join(['#' * self.__width] * self.__height)
