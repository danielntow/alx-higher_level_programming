#!/usr/bin/python3'
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        # print("Exception: ", file=sys.stderr, end=" ")
        print('Exception: ', e, file=sys.stderr)
        return False
