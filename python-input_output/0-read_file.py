#!/usr/bin/python3
"""
Docstring for python-input_output.0-read_file

"""


def read_file(filename=""):
    with open(filename,encoding="utf-8") as file:
        text = file.read()
        print(text)
