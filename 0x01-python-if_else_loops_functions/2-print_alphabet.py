#!/usr/bin/python3

# Using a list comprehension to generate the alphabet
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

# Printing the alphabet without newlines
print("".join(alphabet))
