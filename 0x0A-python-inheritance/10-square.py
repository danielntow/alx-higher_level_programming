#!/usr/bin/python3

"""
a module depicting BaseGeomety
"""


class BaseGeometry:
    """
    A base class representing geometric entities.

    This class serves as the foundation for geometric
    calculations and structures.
    It's designed to be inherited by specific geometric
    entities to extend functionality.
    """

    def area(self):
        """
        Raises an Exception indicating that the area()
        method is not implemented.

        Raises:
            Exception: Indicates that the area()
            method is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value provided ensuring it is an
        integer and greater than 0.

        Args:
            name (str): A string representing the name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a Rectangle, inheriting from BaseGeometry.

    This class manages the properties and
    calculations specific to rectangles.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with specified width and height.

        Args:
            width (int): Width of the rectangle (positive integer).
            height (int): Height of the rectangle (positive integer).
        """
        super().__init__()
        self.__width = 0  # Initializing private attribute for width
        self.__height = 0  # Initializing private attribute for height
        # Validating width and height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width  # Setting the validated width
        self.__height = height  # Setting the validated height

    def __str__(self):
        """ string representation of rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        returns the area pf the rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    Square class inhertits from Rectangle

    This Class Clculates the area of a square
    """

    def __init__(self, size,):
        super().__init__(size, size)

    @property
    def size(self):
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        self.integer_validator("size", value)  # Validate the size
        self.width = value

    def area(self):
        """caculates area of a square

        Returns:
            _type_: _description_
        """
        return super().area()

    def __str__(self):
        """
        String representation of the Square.

        Returns:
            str: Square description in the format [Square] <size>/<size>
        """
        return f"[Square] {self.size}/{self.size}"
