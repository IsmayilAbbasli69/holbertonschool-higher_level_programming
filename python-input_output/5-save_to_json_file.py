#!/usr/bin/python3
"""Module that returns JSON representation of an object"""


import json


def save_to_json_file(my_obj, filename):

    with (filename, "w") as f:

        json.dump(my_obj, f)
