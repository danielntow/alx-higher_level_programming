#!/usr/bin/python3

"""This module defines a base class and subclasses
for rectangles.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size: Size of the square.
            x: X coordinate of the square (default is 0).
            y: Y coordinate of the square (default is 0).
            id: Id of the square (inherited from Rectangle class).

        Attributes:
            size: Size of the square.
            x: X coordinate of the square.
            y: Y coordinate of the square.
        """
        # width = height = size
        # super(Square, self).__init__(width, height, x, y, id)
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the Square object.

        Returns:
            String in the format: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/\
{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the Square object with the new provided values.
        """
        attributes = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        def to_dictionary(self):
            """
            Returns the dictionary representation of a Square.

            Returns:
                Dictionary with keys: 'id', 'size', 'x', 'y'.
            """
            return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
            }
