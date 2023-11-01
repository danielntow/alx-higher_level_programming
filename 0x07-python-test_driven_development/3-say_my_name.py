#!/usr/bin/python3
"""
module that prints one's full name
"""


def say_my_name(first_name="", last_name=""):
    """
    Prints the full name composed of the given first name and last name.

    Args:
        first_name (str, optional): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Returns:
        None

    """
    # Validate first_name and last_name
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    output = ""
    if first_name and last_name:
        output = f"My name is {first_name} {last_name}".strip()
    elif last_name:
        output = f"My name is {last_name}".strip()
    elif first_name:
        output = f"My name is {first_name}".strip()
    else:
        output = "My name is"

    print("{:s}".format(output))
