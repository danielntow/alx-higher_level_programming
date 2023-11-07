#!/usr/bin/python3
"""
Module demonstrating Python I/O
"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# Get the existing list from the file, if it exists
try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []

# Adding new arguments to the existing list
for arg in sys.argv[1:]:
    existing_list.append(arg)

# Saving the updated list to the file
save_to_json_file(existing_list, "add_item.json")
