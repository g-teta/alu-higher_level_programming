#!/usr/bin/python3
"""
This module defines a class Square with size validation on instantiation.
"""


class Square:
    """
    Defines a square with a private size attribute that is validated.

    Attributes:
        __size (int): The size of the square side (private).
    """

    def __init__(self, size=0):
        """
        Initialize a Square with optional size.

        Args:
            size (int, optional): The size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
