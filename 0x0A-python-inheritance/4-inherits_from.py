#!/usr/bin/python3

"""
module that checks the sub_class of an object
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
    obj: Any object
    a_class: Class to check against

    Returns:
    bool: True if obj is an instance of a subclass of a_class; otherwise False
    """
    # below line works exactly
    # return issubclass(type(obj), a_class) and type(obj) is not a_class
    return issubclass(type(obj), a_class) and type(obj) is not a_class
