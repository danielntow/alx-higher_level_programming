#!/usr/bin/python3
def uppercase(s):
    result = ""  # Initialize an empty string to store the uppercase string

    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ord() and chr()
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char
        else:
            # For non-lowercase letters, add them to the result as they are
            result += char

    # Print the entire uppercase string followed by a new line
    print("{}".format(result))
