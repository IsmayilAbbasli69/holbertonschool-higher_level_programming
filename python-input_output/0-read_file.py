#!/usr/bin/python3
"""
Docstring for python-input_output.0-read_file

"""


def read_file(filename=""):
    """
    FILE
    """
    with open(filename,"r",encoding="utf-8") as file:
        print(file.read(), end="")
