#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = {}
    for i in range(2):
        result[i] = tuple_a[i] if len(tuple_a) > i else 0
        result[i] += tuple_b[i] if len(tuple_b) > i else 0
    return tuple(result.values())
