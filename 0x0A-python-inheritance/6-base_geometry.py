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
