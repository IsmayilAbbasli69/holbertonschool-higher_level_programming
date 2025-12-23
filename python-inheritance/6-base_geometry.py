#!/usr/bin/python3
"""
This module defines a BaseGeometry class with a public method area.
The area() method is not implemented and raises an Exception.
"""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")
