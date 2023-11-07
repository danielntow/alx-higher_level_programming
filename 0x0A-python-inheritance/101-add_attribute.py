#!/usr/bin/python3

""" module that adds attributes"""


def add_attribute(obj, name, value):
    """
    function that add new attribute if possible
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: Object to which the attribute will be added.
        attr: Name of the attribute.
        value: Value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if hasattr(obj, '__dict__') or (
        hasattr(obj, '__slots__'
                ) and attr in obj.__slots__):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
