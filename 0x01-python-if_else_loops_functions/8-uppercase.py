#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ord() and chr()
            uppercase_char = chr(ord(char) - 32)
            print(uppercase_char, end='')
        else:
            # For non-lowercase letters, print them as they are
            print(char, end='')
