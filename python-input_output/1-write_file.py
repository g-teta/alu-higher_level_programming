#!/usr/bin/python3
"""
Module: 1-write_file
Writes a string to a UTF-8 text file and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write.

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
