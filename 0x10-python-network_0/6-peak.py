#!/usr/bin/python3
""" Finds a peak in an unsorted integers of a list 
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    fir_e = size
    fir = size // 2

    if size == 0:
        return None

    while True:
        fir_e = fir_e // 2
        if (fir < size - 1 and
                list_of_integers[fir] < list_of_integers[fir + 1]):
            if fir_e // 2 == 0:
                fir_e = 2
            fir = fir + fir_e // 2
        elif fir_e > 0 and list_of_integers[fir] < list_of_integers[fir - 1]:
            if fir_e // 2 == 0:
                fir_e = 2
            fir = fir - fir_e // 2
        else:
            return list_of_integers[fir]
