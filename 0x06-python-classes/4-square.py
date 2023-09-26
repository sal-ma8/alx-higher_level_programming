#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        elcomment hena 8aryb gedan fa yala bena no7ot ely 
        fahmenoo
        """
        self.size = size

    @property
    def size(self):
        """5od aw 7ot ay haga kolo zay b3d gedn yalaa."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """htrag3ly alarea bta3et al function self so 5od."""
        return (self.__size * self.__size)
