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
        has_int = False
        has_str = False

        for member in self:
            if isinstance(member, int):
                has_int = True
            elif isinstance(member, str):
                has_str = True

        if has_int and has_str:
            raise TypeError(
                "'<' not supported between instances of 'int' and 'str'")

        sorted_list = sorted(self)  # Sort the list in ascending order
        print(sorted_list)  # Print the sorted list
