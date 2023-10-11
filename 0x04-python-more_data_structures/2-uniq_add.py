#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to eliminate duplicates and then sum the unique values
    unique_values = set(my_list)
    result = sum(unique_values)
    return result
