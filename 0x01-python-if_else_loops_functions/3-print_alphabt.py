#!/usr/bin/python3
for alphabet in range(97, 123):
    if alphabet == 101 or alphabet == 113:
        continue
    print("{}".format(chr(alphabet)), end="")


'''
for i in range(97, 123):
    if i == ord('q') or i == ord('e'):
        continue
    print("{}".format(chr(i)), end='')


for i in range(ord('a'), ord('z') + 1):
    if i == ord('q') or i == ord('e'):
        continue
    print("{}".format(chr(i)), end='')


# Loop to print the alphabet without 'q' and 'e' using string format
for char in 'abcdefghijklmnopqrstuvwxyz':
    if char != 'q' and char != 'e':
        print("{}".format(char), end='')

'''
