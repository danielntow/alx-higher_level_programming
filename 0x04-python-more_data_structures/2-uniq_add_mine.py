#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to eliminate duplicates and then sum the unique values
    unique_values = set(my_list)
    result = sum(unique_values)
    return result


def uniq_add(my_list=[]):
    unique_values = set()
    result = 0
    for num in my_list:
        if num not in unique_values:
            result += num
            unique_values.add(num)
    return result


def uniq_add(my_list=[]):
    result = 0
    unique_values = []
    for num in my_list:
        if num not in unique_values:
            result += num
            unique_values.append(num)
    return result


def uniq_add(my_list=[]):
    unique_values = []
    [unique_values.append(num) for num in my_list if num not in unique_values]
    return sum(unique_values)


def uniq_add(my_list=[]):
    unique_values = set()
    for num in my_list:
        if num not in unique_values:
            unique_values.add(num)
    result = sum(unique_values)
    return result


def uniq_add(my_list=[]):
    unique_value = set()
    for num in my_list:
        if num not in unique_value:
            unique_value.add(num)
    result = sum(unique_value)
    return result


def uniq_add(my_list=[]):
    unique_values = set()
    for num in my_list:
        unique_values.add(num)
    result = sum(unique_values)
    return result
