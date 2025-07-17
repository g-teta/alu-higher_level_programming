#!/usr/bin/python3
"""
Module: 5-save_to_json_file
This module provides a function to serialize a Python object to a JSON file.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to be serialized.
        filename (str): The name of the file to write the JSON representation to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
