#!/usr/bin/python3
"""
module demonstrating python i/o
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes the JSON representation of the given object to a text file

    Args:
        my_obj: The object to be saved as JSON.
        filename (str): The name of the file to save the JSON representation.

    Returns:
        None.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
