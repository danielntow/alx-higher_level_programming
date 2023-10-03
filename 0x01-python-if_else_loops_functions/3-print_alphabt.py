#!/usr/bin/python3
# Loop to print the alphabet without 'q' and 'e' using string format
for i in range(ord('a'), ord('z') + 1):
    if i == ord('q') or i == ord('e'):
        continue
    print("{}".format(chr(i)), end='')
