#!/usr/bin/python3
"""
this is the first file for this project.
this file function to add two number tohather.
>>> add_integer(10, 12)
"""


def add_integer(a, b=98):
    """
        Adds two integer.
        Args:
            a (int|float): a is number int or float.
            b (int|float): b is number int or float.
        Returns: The sum of `a` and `b`
    """

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is not int:
        raise TypeError("b must be an integer")

    return (a + b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
