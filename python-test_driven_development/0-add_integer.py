#!/usr/bin/python3
"""

Add Integer or Float Module

"""


def add_integer(a, b=98):
    """
    ADD Two integer a and b

    Args:
        a (int/float): first int
        b (int/float): Second int

    Raises:
        TypeError: in case the arguments are not int or float

    Return:
        (int) : Sum of the int a and b
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
