#!/usr/bin/python3
""" 'Rectangle.py' module """
from models.base import Base

class Rectangle(Base):
    """ a subclass Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization of the Rectangle model """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter of the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getter of the x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter of the x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter of the y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter of the y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ return the area value of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """
        that prints in stdout the Rectangle
        instance with the character #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("")for a in range(self.y)]
        for c in range(self.height):
            [print(" ", end="") for b in range(self.y)]
            [print("#", end="") for d in range (self.width)]
            print("")

    def update(self, *args, **kwargs):
        """ update the class Rectangle """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
    def to_dictionary(self):
        """  that returns the dictionary representation of a Rectangle """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
                }

    def __str__(self):
        """ print out the Rectangle representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
