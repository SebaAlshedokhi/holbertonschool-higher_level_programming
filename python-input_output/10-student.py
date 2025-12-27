#!/usr/bin/python3
"""defining Student class with filtered serialization"""


class Student:
    """
    represent a student with filtered serialization.
    """

    def __init__(self, first_name, last_name, age):
        """
        initialize a new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return dictionary representation of Student.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__
