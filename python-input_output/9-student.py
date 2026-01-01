#!/usr/bin/python3
"""
Docstring for python-input_output.6-load_from_json_file
"""


class Student:
    """
    Docstring for Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Docstring for __init__
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Docstring for to_json
        """
        return self.__dict__
