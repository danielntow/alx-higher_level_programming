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
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise ValueError("Value is not an integer")
    except ValueError as e:
        sys.stderr.write(f"Exception: {e}\n")
        return False
