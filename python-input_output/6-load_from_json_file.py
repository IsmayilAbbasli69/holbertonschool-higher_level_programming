#!/usr/bin/python3
"""
Module
"""
import json


def load_from_json_file(filename):
    """
THis gotta work
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
