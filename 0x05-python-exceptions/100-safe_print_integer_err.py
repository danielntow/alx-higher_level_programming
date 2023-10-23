#!/usr/bin/python3
import sys  # Import the sys module to access stderr


def safe_print_integer_err(value):
    try:
        # Attempt to convert the value to an integer
        value_as_integer = int(value)
        print("{:d}".format(value_as_integer))  # Print the integer value
        return True  # Return True if it's an integer
    except (ValueError, TypeError):
        # Handle the exception and print the error message in stderr
        print("Exception: You have to use an integer", file=sys.stderr)
        return False
