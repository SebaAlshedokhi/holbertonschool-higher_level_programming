#!/usr/bin/python3
"""generating Pascal's triangle"""


def pascal_triangle(n):
    """
    generate Pascal's triangle of size n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

