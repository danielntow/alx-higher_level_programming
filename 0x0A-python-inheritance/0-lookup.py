#!/usr/bin/python3

""""

"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj: The object to be inspected.

    Returns:
    - A list containing the names of attributes and methods
    of the given object.

    Raises:
    - None.
    """
    return [attr for attr in dir(obj)]
