#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    a = list(tuple_a)
    b = list(tuple_b)
    len_a = len(a)
    len_b = len(b)

    while len(a) < 2:
        a.append(0)
        len_a += 1
    while len(b) < 2:
        b.append(0)
        len_b += 1
    sum_a = a[0] + b[0]
    sum_b = a[1] + b[1]
    return (sum_a, sum_b)
