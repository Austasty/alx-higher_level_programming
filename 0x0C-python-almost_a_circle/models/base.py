#!/usr/bin/python3
""" module containing base model """
import json
import csv


class Base():
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):

        """ initializing the base model """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """
        that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """  writes the JSON string representation of list_objs to a file """
        file_n = "cls.__name__" + ".json"
        with open(file_n, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_new = [i.to_dictionary() for i in list_objs]
                json_file.write(Base.to_json_string(list_new))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "[]":
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
