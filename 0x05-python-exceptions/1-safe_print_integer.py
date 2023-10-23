#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Try to format and print the value as an integer
        print("{:d}".format(value))
        # If the formatting and printing succeeded, return True
        return True
    except (ValueError, TypeError):
        # Handle exceptions for non-integer values
        return False


def safe_print_integer(value):
    if isinstance(value, int):
        print("{:d}".format(value))
        return True
    else:
        return False


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
