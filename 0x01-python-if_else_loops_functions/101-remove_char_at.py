#!/usr/bin/python3
def remove_char_at(input_str, n):
    # Check if n is a valid index
    if 0 <= n < len(input_str):
        # Create a new string by excluding the character at position n
        result_str = input_str[:n] + input_str[n+1:]
        return result_str
    else:
        # If n is out of bounds, return the original string
        return input_str
