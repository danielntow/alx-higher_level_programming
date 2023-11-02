#!/usr/bin/python3
"""
Locked Class module
"""


class LockedClass:
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'")
        super().__setattr__(name, value)


class LockedClass:

    """
    Class that restrict the dynamically creating
    instance with certain condition
    """

    __slots__ = ('first_name',)

    def __init__(self):
        self.first_name = ""


class LockedClass:
    """
    Class that restrict the dynamically creating
    instance with certain condition
    """
    __slots__ = ["first_name"]
