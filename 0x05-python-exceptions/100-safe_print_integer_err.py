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
    except (TypeError, ValueError) as e:
        error_message = f"Exception: {e}"
        print(error_message, file=sys.stderr)
        return False


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        error_message = f"Exception: {e}"
        sys.stderr.write(error_message + "\n")
        return False
