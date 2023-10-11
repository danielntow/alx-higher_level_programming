#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0.0  # Return 0.0 if the list is empty to avoid division by zero

    weighted_sum = 0.0
    total_weight = 0

    for row in my_list:
        if len(row) == 2:  # Ensure each row contains two elements
            value, weight = row[0], row[1]
            weighted_sum += value * weight
            total_weight += weight

    if total_weight == 0:
        return 0.0  # Handle e case er t_weight is 0 to avd division by zero

    weighted_avg = weighted_sum / total_weight
    return weighted_avg


def weight_average(my_list=[]):
    result = 0
    divisor = 0
    def divisors(y): return y + y
    for row in my_list:
        if len(row) == 2:
            x, y = row[0], row[1]
            result += x * y
            divisor += y

    return result / divisor


def weight_average(my_list=[]):
    weighted_sum = 0
    total_weight = 0

    for row in my_list:
        if len(row) == 2:
            value, weight = row[0], row[1]
            weighted_sum += value * weight
            total_weight += weight

    if total_weight == 0:
        return 0.0

    weighted_avg = weighted_sum / total_weight
    return weighted_avg
