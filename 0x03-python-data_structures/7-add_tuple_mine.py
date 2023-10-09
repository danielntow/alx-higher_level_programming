#!/usr/bin/python3
def add_tuplea(tuple_a=(), tuple_b=()):
    a, b = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    x, y = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)
    return (a + x, b + y)


def add_tuples(tuple_a=(), tuple_b=()):
    result = {}
    for i in range(2):
        result[i] = tuple_a[i] if len(tuple_a) > i else 0
        result[i] += tuple_b[i] if len(tuple_b) > i else 0
    return tuple(result.values())


def add_tuples(tuple_a=(), tuple_b=()):
    result = [0, 0]
    for i in range(2):
        if i < len(tuple_a):
            result[i] += tuple_a[i]
        if i < len(tuple_b):
            result[i] += tuple_b[i]
    return tuple(result)


def add_tuples(tuple_a=(), tuple_b=()):
    return tuple(sum(x) for x in zip(tuple_a[:2], tuple_b[:2]))


def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]
    for i in range(2):
        if i < len(tuple_a):
            result[i] += tuple_a[i]
        if i < len(tuple_b):
            result[i] += tuple_b[i]
    return tuple(result)
