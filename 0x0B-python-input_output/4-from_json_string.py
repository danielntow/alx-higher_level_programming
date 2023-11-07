#!/usr/bin/python3
"""
module demonstrating python i/o
"""

import json


def from_json_string(my_str):
    """
    Convert a json string to python obj

    Args:
    my_str (str): the json string

    Returns:
    A python object
    """
    json_string = json.loads(my_str)
    return json_string
