#!/usr/bin/python3
""" This module contain a function that adds to integers or float"""


def add_integer(a, b=98):
    """Returns addition of a and b.

    Raises:
        TypeError: If either of a or b is not integer  or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
