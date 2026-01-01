#!/usr/bin/python3
"""
Docstring for python-input_output.6-load_from_json_file
"""

import json 

def load_from_json_file(filename):
    with open(filename, "w") as f:
        json.load(filename, f)
