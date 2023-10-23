#!/usr/bin/python3'
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception: ", file=sys.stderr, end="")
        print(e, file=sys.stderr)
        return False


def safe_print_integer_err(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return True
    except TypeError as te:
        error_message = f"Type Error: {te}"
    except ValueError as ve:
        error_message = f"Value Error: {ve}"
    print(f"Exception: {error_message}", file=sys.stderr)
    return False
