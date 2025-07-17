#!/usr/bin/python3
"""
Module: 2-append_write
Appends a string to a UTF-8 text file and returns the number of characters added.
"""

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append.

    Returns:
        int: Number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
