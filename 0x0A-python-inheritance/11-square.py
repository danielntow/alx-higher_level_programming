#!/usr/bin/python3
"""
this is a square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a Square, inheriting from Rectangle.

    This class manages the properties and calculations specific to squares.
    """

    def __init__(self, size):
        """
        Initializes a Square with the specified size.

        Args:
            size (int): Size of the square (positive integer).
        """
        # Initialize using size for both width and height
        super().__init__(size, size)

    def __str__(self):
        """
        String representation of the Square.

        Returns:
            str: Square description in the format [Square] <width>/<height>
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
