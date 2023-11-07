#!/usr/bin/python3

"""
This module contains a function to read a text file and print
its content to the standard output (stdout).
"""


def read_file(filename=""):
    """
    Reads the content of a text file in UTF-8 encoding and
    prints it to the standard output (stdout).

    :param filename: (str) The name of the text file.
    Default is an empty string.
    :return: None
    """

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(),  end="")
