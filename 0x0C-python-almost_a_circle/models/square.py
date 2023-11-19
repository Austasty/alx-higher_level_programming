#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class representation"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square"""
        # Change every attribute to args value
        if args:
            # Attribute list
            attr_list = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], value)
                else:
                    raise ValueError(f"Too many arguments provided")
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise ValueError(f"{key} is not an attribute in this class")

    def to_dictionary(self):
        """Square to dictionary"""
        square_dict = {}
        square_dict["id"] = self.id
        square_dict["size"] = self.size
        square_dict["x"] = self.x
        square_dict["y"] = self.y
        return square_dict
