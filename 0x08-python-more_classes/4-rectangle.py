#!/usr/bin/python3

""" This module defines a class called Rectangle"""


class Rectangle:
    """ The empty class Rectangle, that defines the rectangle """

    def __init__(self, width=0, height=0):
        """ This method initializes the instance

        Args:
            width: rectangle width
            height: rectangle height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ The method that returns the value of the width

        Returns:
            rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """ This Method defines the width

        Args:
            value: width

        Raises:
            TypeError: if the width is not an int
            ValueError: if the width is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ the Method that returns the value of the height

        Returns:
            rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """ This method defines the height

        Args:
            value: height

        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ The method that returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ The method that returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """ This method returns the string that represents the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def __repr__(self):
        """ This method returns a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)
