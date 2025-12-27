#!/usr/bin/python3
"""defining Student class"""


class Student:
    """
    represent a student with personal information.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return dictionary representation of Student.
        """
        return self.__dict__
