#!/usr/bin/python3
class Node:

    data = None
    next_node = None

    def __init__(self, data, next_node=None):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not value isinstance(value, int):
            raise TypeError("data must be an integer")
        self.data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
