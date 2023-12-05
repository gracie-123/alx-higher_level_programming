#!/usr/bin/python3
"""Module student. Main class
"""


class Student:
    """the class that contains the functions"""

    def __init__(self, first_name, last_name, age):
        """initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a student instance"""
        return self.__dict__
