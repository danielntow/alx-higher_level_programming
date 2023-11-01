#!/usr/bin/python3
def magic_string():
    n = i + 1
    return ', '.join(["BestSchool"] * n)


def magic_string(my_list=[]):
    my_list.append("BestSchool")
    return ', '.join(my_list)


def magic_string():
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return ", ".join(["BestSchool"] * magic_string.counter)
