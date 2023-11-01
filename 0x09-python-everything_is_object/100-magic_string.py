#!/usr/bin/python3
""" magic string module """


def magic_string():
    n = i + 1
    return ', '.join(["BestSchool"] * n)


def magic_string(my_list=[]):
    my_list.append("BestSchool")
    return ', '.join(my_list)


def magic_string():
    """
    Generates a string containing 'BestSchool' repeated a
    number of times based on the iteration.

    Returns:
        str: A string where 'BestSchool' is repeated the
        number of times corresponding to the iteration number.
    """
    # Get the current value of the counter attribute and increment it
    magic_string.counter = getattr(
        magic_string, 'counter', 0
    ) + 1

    # Join 'BestSchool' strings using comma and space based
    # on the current value of the counter
    return ", ".join(["BestSchool"] * magic_string.counter)
