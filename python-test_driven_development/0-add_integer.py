#!/usr/bin/python3
"""Defines an integer addition function"""
def add_integer(a, b=98):
    """Return the integer addition of a and b
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
        OverflowError: If float infinity or NaN is passed.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and (a == float('inf') or a == float('-inf') or a != a):
        raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf') or b != b):
        raise OverflowError("cannot convert float infinity to integer")
    return int(a) + int(b)
