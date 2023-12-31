#!/usr/bin/python3
"""Define a MagicClass matching exactly to do some things."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Arg:
            radius (float or int): this is a function which doing som opration.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """this is a function which doing som opration for our program."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """this is a function which doing som opration for our program."""
        return (2 * math.pi * self.__radius)
