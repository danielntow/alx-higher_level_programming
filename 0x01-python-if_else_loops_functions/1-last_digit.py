#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Calculate the last digit of the number
last_digit = abs(number) % 10

# Determine the comparison message
if number < 0:
    last_digit = -last_digit
    comparison_message = "and is less than 6 and not 0"
else:
    if last_digit > 5:
        comparison_message = "and is greater than 5"
    elif last_digit == 0:
        comparison_message = "and is 0"
    else:
        comparison_message = "and is less than 6 and not 0"

# Print the result
print(f"Last digit of {number} is {last_digit} {comparison_message}")
