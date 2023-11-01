#!/usr/bin/python3
"""
Module that prints text with specific indentation rules.

"""


def text_indentation(text):
    """
    the function indents a code

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the text input is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for alpha in range(len(text)):
        if text[alpha] in (".", "?", ":"):
            print("{:s}".format(text[alpha]).strip())
            print('\n')
            continue
        print("{:s}".format(text[alpha]).strip(), end="")


# def text_indentation(text):
#     """ this function does exactly
#     what is described in the module
#     """

#     chars = ".?:"
#     if type(text) is not str:
#         raise TypeError("text must be a string")
#     i = 0
#     while i < len(text):
#         if text[i] in chars:
#             print(text[i], end="\n\n")
#             i = i + 2
#             continue
#         print(text[i], end="")
#         i = i + 1


# def text_indentation(text):
#     """
#     Prints a text with 2 new lines after each '.', '?' and ':' characters.

#     Args:
#         text (str): The text input.

#     Raises:
#         TypeError: If the text is not a string.

#     Returns:
#         None
#     """

#     if not isinstance(text, str):
#         raise TypeError("text must be a string")

#     special_chars = ['.', '?', ':']
#     start = 0

#     text = text.strip()

#     for i in range(len(text)):
#         if text[i] in special_chars:
#             print(text[start:i + 1].strip())
#             print()
#             start = i + 1

#     if start < len(text):
#         print(text[start:].strip())

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':' characters.

    Args:
        text (str): The text input.

    Raises:
        TypeError: If the text is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    result = ""
    last_char = ''  # Variable to store the last printed character

    for char in text:
        if char in special_chars:
            result += char + "\n\n"
            last_char = '\n'  # Update last printed character
            continue
        elif char != ' ' or last_char != ' ':
            result += char
            last_char = char  # Update last printed character

    print(result.strip())


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':' characters.

    Args:
        text (str): The text input.

    Raises:
        TypeError: If the text is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    lines = text.split('\n')

    for line in lines:
        line = line.strip()  # Remove leading/trailing spaces
        if line:
            leading_spaces = 0
            for char in line:
                if char == ' ':
                    leading_spaces += 1
                else:
                    break  # Stop counting leading spaces

            for char in line[leading_spaces:]:
                # Print after the leading spaces
                if char in special_chars:
                    print(char + '\n')
                else:
                    print(char, end='')
            print()
        else:
            print()  # For blank lines


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the text is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    print_line = False  # Flag to handle no spaces at the beginning
    for char in text:
        if char in (".", "?", ":"):
            print(char + '\n\n')
            print_line = False
        elif char != ' ' and not print_line:
            print(char, end='')
            print_line = True
        elif char != ' ':
            print(char, end='')
        elif print_line:
            print(char, end='')
    print()


def text_indentation(text):
    """
    the function indents a code

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the text input is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for alpha in range(len(text)):
        if text[alpha] in (".", "?", ":"):
            print("{}".format(text[alpha: + 1]).strip(), end="")
            print('\n')
            continue
        print("{:s}".format(text[alpha]).strip(), end="")


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of
    the following characters: ., ? and :

    Args:
      text: The text to be printed. Must be a string.

    Raises:
      TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove any leading and trailing whitespace from the text.
    text = text.strip()

    # Iterate over the characters in the text.
    for i in range(len(text)):
        char = text[i]

        # If the character is a period, question mark,
        # or colon, print two new lines.
        if char in [".", "?", ":"]:
            print(char)
            if char == " ":
                continue
            print("\n", end="")

            continue

        # Print the current character.
        print(char, end="")


text_indentation("Hello. How are you? I'm fine.")
