#!/usr/bin/python3
"""Module that writes an object to a file in JSON format"""

import json


def save_to_json_file(my_obj, filename):

    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj: The Python object to serialize (list, dict, etc.)
        filename: The filename where JSON will be written
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
