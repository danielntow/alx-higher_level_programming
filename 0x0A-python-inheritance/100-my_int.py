#!/usr/bin/python3
"""
module that reverses == and != operators
"""


class MyInt(int):
    """
    A class representing a rebel MyInt, inheriting from int.

    This class inverts the behavior of the equality and inequality operators.
    """

    def __eq__(self, other):
        """
        Inverts the behavior of the equality operator (==).
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the inequality operator (!=).
        """
        return super().__eq__(other)
