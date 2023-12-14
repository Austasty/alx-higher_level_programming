#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ A square instance"""

    def __init__(self, size=0):
        """A new Square.

        Args:
            size (int): new square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
