#!/usr/bin/python3

# Program to print the ASCII alphabet in lowercase without a new line
def print_alphabet():
    for i in range(ord('a'), ord('z') + 1):
        print("{}".format(chr(i)), end='')


# Call the function to print the alphabet
print_alphabet()
