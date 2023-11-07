#!/usr/bin/python3
"""
module that returns the dictionary description
with simple data structure
"""


def class_to_json(obj):
    """
    Returns a dictionary representation of the object for JSON serialization.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary description suitable for JSON serialization.
    """
    attributes = obj.__dict__ if hasattr(obj, '__dict__') else vars(obj)
    serializable = {}

    for key, value in attributes.items():
        # Check if the attribute is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            serializable[key] = value

    return serializable
