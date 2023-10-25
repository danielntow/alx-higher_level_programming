#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        """
        Initialize a Node with data and an optional reference to the next node.

        Args:
            data: Data to be stored in the node.
            next_node: Reference to the next node in the linked list (default is None).
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data in the node, ensuring it is an integer.

        Args:
            value: The new data to be stored in the node.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the reference to the next node in the linked list.

        Returns:
            The reference to the next node (Node object).
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node in the linked list.

        Args:
            value: The reference to the next node (Node object).

        Raises:
            TypeError: If the provided value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    def __repr__(self):
        """
        Create a string representation of the linked list.

        Returns:
            A string representation of the linked list in the format "data1\ndata2\ndata3".
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Insert a new node with the given value into the linked list in sorted order.

        Args:
            value: The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if not self.head or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
