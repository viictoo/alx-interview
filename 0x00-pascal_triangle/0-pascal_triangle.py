#!/usr/bin/python3
"""pascals never ending tree"""


def pascal_triangle(n):
    """this method draws pascals triangle given an integer n"""
    _list = []

    if (n <= 0):
        return _list
    for i in range(1, n + 1):
        arr = []
        for j in range(1, i + 1):
            # corner conditions
            if i <= 2 or j == i or j == 1:
                val = 1
            else:
                val = _list[i - 2][j - 1] + _list[i - 2][j - 2]
            arr.append(val)
        _list.append(arr)
    return _list
