#!/usr/bin/python3
"""
python module
"""


import sys
from collections import defaultdict


def print_statistics(total_size, status_count):
    """
    Print statistics based on total file size and
    status code occurrences.

    Args:
        total_size (int): The accumulated total file size.
        status_count (dict): Dictionary with status
        codes and their occurrences.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_count.keys()):
        if status_count[status] > 0:
            print(f"{status}: {status_count[status]}")


def process_lines(lines):
    """
    Process the lines to calculate total file size
    and status code occurrences.

    Args:
        lines (list): List of lines to process.

    Returns:
        int: Total file size from the processed lines.
        dict: Dictionary with status codes and their occurrences.
    """
    total_size = 0
    status_count = defaultdict(int)
    for line in lines:
        elements = line.split()
        if len(elements) > 6:
            status = elements[8]
            if status.isdigit():
                total_size += int(elements[9])
                status_count[status] += 1
    return total_size, status_count


try:
    lines = []
    count = 0
    for line in sys.stdin:
        lines.append(line)
        count += 1
        if count == 10:
            total_size, status_count = process_lines(lines)
            print_statistics(total_size, status_count)
            lines = []
            count = 0

except KeyboardInterrupt:
    total_size, status_count = process_lines(lines)
    print_statistics(total_size, status_count)
