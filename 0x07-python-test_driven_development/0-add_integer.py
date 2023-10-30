#!/usr/bin/python3
"""
this is a module for adding integers

"""


def add_integer(a, b=98):
    """Function to add integers

    Args:
        a (int): first number
        b (int, optional): second number. Defaults to 98.

        Returns:
            int: the sum of 2 integers

        Raises:
        TypeError: If a or b is not an integer or float.
    """

    # Check if a is an integer or float, and cast it to an integer if necessary
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    a = int(a)

    # Check if b is an integer or float, and cast it to an integer if necessary
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    b = int(b)

    # Return the sum of a and b as an integer
    return a + b
