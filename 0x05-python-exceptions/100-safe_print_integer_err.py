#!/usr/bin/python3'
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as ne:
        print("Exception: ", file=sys.stderr, end="")
        print(ne, file=sys.stderr)
        return False


def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except (ValueError, TypeError):
        sys.stderr.write("Exception: You must provide an integer\n")
        return False
