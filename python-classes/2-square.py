#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size=0):
        """Initialize a square with a given size."""
        if size is not int:
            raise TypeError("size must be an integer")
            """ if if if """

        elif size < 0:
            raise ValueError("size must be >= 0")
