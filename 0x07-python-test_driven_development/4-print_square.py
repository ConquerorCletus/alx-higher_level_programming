#!/usr/bin/python3
"""
4-print_square module.
"""


def print_square(size):
    """
prints a square with "#"'s that has a length of size 

args
	size: size of the square
Exception Error
	TypeError: if size is not integer
	ValueError: if size is less than 0.
"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
