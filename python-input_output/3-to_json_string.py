#!/usr/bin/python3
"""
Module: 3-to_json_string
Converts a Python object to its JSON string representation.
"""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
