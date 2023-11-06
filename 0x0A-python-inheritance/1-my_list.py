#!/usr/bin/python3
"""
module that sorts a list
"""


class MyList(list):
    """
    MyList class that inherits from list and
    print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        # Sort the list and print in ascending order
        sorted_list = sorted(self)
        print(sorted_list)
