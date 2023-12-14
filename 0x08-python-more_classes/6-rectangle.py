#!/usr/bin/python3

""" This module defines a class called Rectangle"""


class Rectangle:
    """ The Rectangle class

    Attributes:
       the number_of_instances (int): number of instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes the instance

        Args:
            width: rectangle width
            height: rectangle height

        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Returns the value of the width

        Returns:
            rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Defines the width

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
        """ Returns the value of the height

        Returns:
            rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Defines the height

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
        """ Returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Returns a string that represents the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """ Returns a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Deletes an instance of Rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
