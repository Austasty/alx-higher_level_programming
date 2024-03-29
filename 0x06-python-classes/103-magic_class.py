#!/usr/bin/python3
"""Define a MagicClass exactly a bytecode provided by Holberton school"""

import math


class MagicClass:
    """Represent a circle instance."""

    def __init__(self, radius=0):
        """ MagicClass initialization.

        Arg:
            radius (float or int): new MagicClass radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
