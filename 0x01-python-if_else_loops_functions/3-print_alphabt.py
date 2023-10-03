#!/usr/bin/python3
# Loop to print the alphabet without 'q' and 'e' using string format
for char in 'abcdefghijklmnopqrstuvwxyz':
    if char != 'q' and char != 'e':
        print("{}".format(char), end='')
