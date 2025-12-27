#!/usr/bin/python3
"""converting class instances to dictionaries"""


def class_to_json(obj):
    """
    Return dictionary description for JSON serialization.
    """
    return obj.__dict__
