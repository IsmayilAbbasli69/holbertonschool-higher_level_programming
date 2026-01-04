#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it as data.json.

    :param csv_filename: Name of the input CSV file
    :return: True if successful, False otherwise
    """
    try:
        data = []

        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, IOError, csv.Error, json.JSONDecodeError):
        return False
