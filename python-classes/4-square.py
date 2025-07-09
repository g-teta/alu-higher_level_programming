#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute,
property getter and setter, and an area method.
"""


class Square:
    """
    Defines a square with a private size attribute, accessible via
    properties, and a method to calculate area.

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
        self.size = size  # Use property setter for validation

    @property
    def size(self):
        """int: The size of the square side."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate and return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
