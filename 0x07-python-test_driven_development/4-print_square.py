#!/usr/bin/python3
"""this is the fourth file for this project."""


def print_square(size):
    """Method for printing a square with # characters.

    Args:
        size: The int size  jfjnsi.

    Raises:
        TypeError: If size is not an int ,is string or boolean.
        ValueError: If size is less than z0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")
