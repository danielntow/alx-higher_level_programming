#!/usr/bin/python3
"""
module demonstrates python i/o
"""


def append_write(filename="", text=""):
    """
    Writes the given string to a text file in UTF-8 encoding.

    Args:
        filename (str): The name of the file to write the text to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, "a") as file:
        characters_written = file.write(text)
        return characters_written
