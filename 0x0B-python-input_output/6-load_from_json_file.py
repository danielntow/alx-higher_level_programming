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
        None.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.loads(file)
