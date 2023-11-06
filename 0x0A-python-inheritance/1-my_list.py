#!/usr/bin/python3

class MyList(list):
    """
    MyList class that inherits from list and includes a
    method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        # sorted_list = sorted(self)  # Sort the list in ascending order
        # print(sorted_list)          # Print the sorted list
        print(sorted(self))
