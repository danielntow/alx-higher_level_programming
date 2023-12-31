#!/usr/bin/python3
"""
module that checks the instance of an object
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
    obj: Any object
    a_class: Class to check against

    Returns:
    bool: True if obj is exactly an instance of a_class; otherwise False
    """

    return type(obj) is a_class
