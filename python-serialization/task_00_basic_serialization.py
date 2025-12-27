#!/usr/bin/env python3
"""basic JSON serialization and deserialization"""
import json


def serialize_and_save_to_file(data, filename):
    """
    serialize a Python dictionary and save to a JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    load and deserialize data from a JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
