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


status_codes = {"200": 0, "301": 0, "400": 0,
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_file_size = 0
lines_count = 0

try:
    for line in sys.stdin:
        lines_count += 1
        parts = line.split()
        if len(parts) > 2:
            status_code = parts[-2]
            file_size = int(parts[-1])
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_file_size += file_size

        if lines_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_codes):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
            print()
except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


status_codes = {"200": 0, "301": 0, "400": 0,
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_file_size = 0
lines_count = 0

try:
    for line in sys.stdin:
        lines_count += 1
        parts = line.split()
        if len(parts) > 2:
            status_code = parts[-2]
            file_size = int(parts[-1])
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_file_size += file_size

        if lines_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_codes):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
            print()
except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0,
                      401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin, start=1):
        try:
            parts = line.split()
            if len(parts) >= 9:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_file_size += file_size
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

            if i % 10 == 0:
                print("Total file size: File size: {}".format(total_file_size))
                for code in sorted(status_code_counts.keys()):
                    count = status_code_counts[code]
                    if count > 0:
                        print("{}: {}".format(code, count))
                print()

        except (ValueError, IndexError):
            pass

except KeyboardInterrupt:
    print("Total file size: File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print("{}: {}".format(code, count))
