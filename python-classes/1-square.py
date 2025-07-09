#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute.
"""


class Square:
    """
    Defines a square with a private size attribute.

    Attributes:
        __size (int): The size of the square side (private).
    """

    def __init__(self, size):
        """
        Initialize a Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
