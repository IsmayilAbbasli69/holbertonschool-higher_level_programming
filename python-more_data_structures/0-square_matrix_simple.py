#!/usr/bin/python3
"""Define a function that squares all elements of a matrix."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with all values squared."""
    new_matrix = []
    for row in matrix:
        squared_row = []
        for value in row:
            squared_row.append(value ** 2)
        new_matrix.append(squared_row)
    return new_matrix
