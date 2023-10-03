#!/usr/bin/python3
# Loop for the tens place digit (0 to 8)
for tens_digit in range(9):
    # Loop for the ones place digit (1 to 9)
    for ones_digit in range(tens_digit + 1, 10):
        # Print the combination in ascending order with two digits
        print("{:d}{:d}".format(tens_digit, ones_digit),
              end=", " if tens_digit < 8 else "\n")
