#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Initialize the sum to 0
    total = 0

    # Iterate through command-line arguments (excluding the script name)
    for arg in argv[1:]:
        # Cast each argument to an integer and add it to the total
        total += int(arg)

    # Print the result using string formatting
    print("{}".format(total))
