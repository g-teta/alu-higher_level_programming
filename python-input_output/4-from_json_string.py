#!/usr/bin/python3
"""
Module: 4-from_json_string
Parses a JSON string and returns the corresponding Python object.
"""

import json

def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: Python data structure corresponding to the JSON string.
    """
    return json.loads(my_str)
