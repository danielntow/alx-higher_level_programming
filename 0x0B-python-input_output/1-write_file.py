#!/usr/bin/python3

def write_file(filename="", text=""):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            char_count = file.write(text)
        return char_count
    except:
        return 0
