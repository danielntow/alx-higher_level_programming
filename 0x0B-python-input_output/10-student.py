#!/usr/bin/python3

"""
python module
"""


class Student:
    """
    Class defining a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name,
        last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of strings of attributes to retrieve.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        student_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                student_dict[attr] = getattr(self, attr)
        return student_dict
