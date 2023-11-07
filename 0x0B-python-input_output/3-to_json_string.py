#!/usr/bin/python3
"""
module demonstrating python i/o
"""

import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON representation.

    Args:
    my_obj: The Python object to be converted to JSON.

    Returns:
    A JSON-formatted string representing the Python object.
    """
    json_string = json.dumps(my_obj)
    return json_string
