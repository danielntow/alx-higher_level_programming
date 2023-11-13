#!/usr/bin/python3

"""This module defines a base class and subclasses
for rectangles.
"""
from models.base import Base


class Rectangle(Base):
    """Class for creating and managing rectangles."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.
            x: X coordinate of the rectangle (default is 0).
            y: Y coordinate of the rectangle (default is 0).
            id: Id of the rectangle (inherited from Base class).

        Attributes:
            width: Width of the rectangle.
            height: Height of the rectangle.
            x: X coordinate of the rectangle.
            y: Y coordinate of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        String representation of the Rectangle object.

        Returns:
            String in the format: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id}) {self.x}/\
{self.y} - {self.width}/{self.height}"

    def validate_attributes(self, attr_name, value):
        """Generic attribute validation method."""
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        if value <= 0 and (attr_name == "width" or attr_name == "height"):
            raise ValueError(f"{attr_name} must be > 0")
        if value < 0 and (attr_name == "x" or attr_name == "y"):
            raise ValueError(f"{attr_name} must be >= 0")

    def validate_attribute(self, attr_name, value):
        """Generic attribute validation method."""
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        if value <= 0 and (attr_name == 'width' or attr_name == 'height'):
            raise ValueError(f"{attr_name} must be > 0")
        elif value < 0 and (attr_name == 'x' or attr_name == 'y'):
            raise ValueError(f"{attr_name} must be >= 0")

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes with no-keyword arguments."""
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def updates(self, *args, **kwargs):
        """Update attributes with arguments in this order:
            id, width, height, x, y.
        """
        if args:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']

        if len(args) > 1:
            self.width = args[1]
        elif 'width' in kwargs:
            self.width = kwargs['width']

        if len(args) > 2:
            self.height = args[2]
        elif 'height' in kwargs:
            self.height = kwargs['height']

        if len(args) > 3:
            self.x = args[3]
        elif 'x' in kwargs:
            self.x = kwargs['x']

        if len(args) > 4:
            self.y = args[4]
        elif 'y' in kwargs:
            self.y = kwargs['y']

    @staticmethod
    def verify_int(value):
        """method for validating type """
        if not isinstance(value, int):
            raise TypeError("{value} must be an integer")
        if value <= 0:
            raise ValueError("{value} must be > 0")

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.validate_attribute("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.validate_attribute("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for X."""
        self.validate_attribute("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for width."""
        self.validate_attribute("y", value)
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with '#' characters.
        considering x and y.
        """
        for _ in range(self.__height):
            print(" " * self.x + "#" * self.width)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.

        Returns:
            Dictionary with keys: 'id', 'width', 'height', 'x', 'y'.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        return {attr: getattr(self, attr) for attr in attributes}

    def to_dictionarys(self):
        """
        Returns the dictionary representation of a Rectangle.

        Returns:
            Dictionary with keys: 'id', 'width', 'height', 'x', 'y'.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
