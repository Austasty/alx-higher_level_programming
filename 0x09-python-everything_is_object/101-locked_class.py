#!/usr/bin/python3
"""Defines a class locked."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    """

    __slots__ = ["first_name"]
