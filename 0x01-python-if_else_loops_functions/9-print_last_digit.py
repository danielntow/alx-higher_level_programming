#!/usr/bin/python3
def print_last_digit(number):
    # Ensure that the number is positive (handle negative numbers)
    number = abs(number)

    # Get the last digit using the modulo operator
    last_digit = number % 10

    # Print the last digit
    print("{:d}".format(last_digit), end="")

    # Return the last digit
    return last_digit
