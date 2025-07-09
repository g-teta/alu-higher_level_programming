#!/usr/bin/python3
"""
This module defines a Square class with private size and position
attributes. It supports area calculation and printing the square
using the `#` character and specified position offset.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position offset for printing.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): The position offset (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (
            isinstance(value, tuple)
            and len(value) == 2
            and isinstance(value[0], int) and value[0] >= 0
            and isinstance(value[1], int) and value[1] >= 0
        ):
            self.__position = value
        else:
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using '#' and the position offset."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
