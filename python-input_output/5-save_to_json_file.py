#!/usr/bin/python3
"""
Module: 5-save_to_json_file
Serializes a Python object to a file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The file where the JSON data will be written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
