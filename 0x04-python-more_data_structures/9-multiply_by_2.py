#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}


def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict


def multiply_by_2(a_dictionary):
    return map(lambda x: y, x, y * 2 for x, y in a_dictionary, a_dictionary )
