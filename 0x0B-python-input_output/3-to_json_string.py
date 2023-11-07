#!usr/bin/python3
"""
module demonstrating python i/o
"""

import json


def to_json_string(my_obj):
    """
    function that returns json repr of an onj

    """

    return json.dumps(my_obj)
