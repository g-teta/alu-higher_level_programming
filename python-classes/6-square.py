#!/usr/bin/python3
"""
This module defines a Square class that can represent a square with
a private size and position attribute. It supports area calculation
and printing the square with positional offsets.
"""


class Square:
    """
    Defines a square by its size and position.

    Attributes:
        __size (int): The size of the square's sides (private).
        __position (tuple): The position offset (horizontal, vertical) (private).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): Optional size of the square side (default 0).
            position (tuple): Optional tuple of two positive integers
                              representing position offsets (default (0, 0)).

        Raises:
            TypeError: If size is not int or position not tuple of 2 positive ints.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: Gets or sets the size of the square side."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: Gets or sets the position (horizontal, vertical) of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """
        Calculates the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#' on stdout, respecting
        the position offsets. Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print the square rows with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
