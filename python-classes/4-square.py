#!/usr/bin/python3
"""Defines a Square class with a private size attribute and area computation."""


class Square:
    """Represents a square with size validation."""

    def __init__(self, size=0):
        """Initialize a square with an optional size."""
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
