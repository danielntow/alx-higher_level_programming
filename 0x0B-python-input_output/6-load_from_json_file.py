#!/usr/bin/python3
"""
module demonstrating python i/o
"""

import json


def load_from_json_file(filename):
    """
    create pythin obj from json file

    Args:
        filename (str): The name of the file to save the python obj.

    Returns:
        object: The Python object represented by the JSON file content.
    """
    with open(filename, 'r') as file:
        return json.load(file)
