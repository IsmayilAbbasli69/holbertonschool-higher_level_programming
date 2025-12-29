#!/usr/bin/python3
"""Module that returns JSON representation of an object"""


import json


def save_to_json_file(my_obj, filename):

    """
    Docstring for save_to_json_file
    :param my_obj: Description
    :param filename: Description
    """

    with (filename, "w") as f:

        json.dump(my_obj, f)
