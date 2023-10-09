#!/usr/bin/python3
def no_c(my_string):
    result_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            result_string += char
    return result_string
