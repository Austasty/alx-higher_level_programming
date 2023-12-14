#!/usr/bin/python3

"""a function that prints a square with the character #."""


def print_square(size):

    """To print a square with the character 
    The Arguments:
        size: the length of the square of type (int)
    Raise exception:
        TypeError: size must be an integer if not an int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
