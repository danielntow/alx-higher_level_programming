#!/usr/bin/python3
from functools import reduce


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = 0
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return max


def max_integer(my_list=[]):
    if not my_list:
        return None
    return my_list[0] if len(my_list) == 1 else max(my_list[0], max_integer(my_list[1:]))

# recursion


def max_integer(my_list=[]):
    if not my_list:
        return None
    if len(my_list) == 1:
        return my_list[0]
    else:
        return max(my_list[0], max_integer(my_list[1:]))


def max_integer(my_list=[]):
    if not my_list:
        return None

    max_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_num = num

    return max_num


def max_integer(my_list=[]):
    if not my_list:
        return None

    return reduce(lambda x, y: x if x > y else y, my_list)


def max_integer(my_list=[]):
    if not my_list:
        return None

    return max([x for x in my_list])


def max_integer(my_list=[]):
    if not my_list:
        return None

    sorted_list = sorted(my_list)
    return sorted_list[-1]
