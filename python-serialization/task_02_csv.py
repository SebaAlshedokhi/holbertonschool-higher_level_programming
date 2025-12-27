#!/usr/bin/env python3
"""converting CSV data to JSON format"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    convert CSV file to JSON format.
    """
    try:
        data = []
        with open(csv_filename, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(row)
        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
