#!/usr/bin/python3
"""
Docstring for python-input_output.0-read_file

"""


def write_file(filename="", text=""):
    """
    FILE
    """
    with open(filename, "w", encoding="utf-8") as file:
        print(file.write(text), end="")

    with open(filename, "r", encoding="utf-8") as file:
        print(len(file.read()))
