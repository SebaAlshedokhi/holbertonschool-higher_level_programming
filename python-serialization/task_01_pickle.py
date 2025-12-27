#!/usr/bin/env python3
"""custom object serialization using pickle"""
import pickle


class CustomObject:
    """
    custom class with serialization capabilities.
    """

    def __init__(self, name, age, is_student):
        """
        initialize a CustomObject instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        display the object's attributes in formatted output.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        serialize the current instance to a file.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize an instance from a file.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
