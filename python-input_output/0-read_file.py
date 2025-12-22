#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """
    a function that reads a text file and prints it
    """
    with open('filename', encoding="utf-8") as f:
        read_data = f.read()
