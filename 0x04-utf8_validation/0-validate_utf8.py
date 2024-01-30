#!/usr/bin/python3
""" validate a data set for consistency with utf8 encoding"""
from typing import List


def validUTF8(data: List) -> bool:
    """ a pythonic solution for determining is the first
    bits are in the correct sequence for valid utf8 encoding
    Returns:
        boolean: True if valid utf8 otherwise false
    """
    # fails 3 checks

    # bitSeq = 0
    # for b in data:
    #     b = bin(b).replace('0b', '').rjust(8, '0')
    #     if bitSeq != 0:
    #         bitSeq -= 1
    #         if not b.startswith('10'):
    #             return False
    #     elif b[0] == '1':
    #         bitSeq = len(b.split('0')[0]) - 1
    # return True

    # fails 3 checks:
    # try:
    #     for b in data:
    #         if type(b) is not int:
    #             return False
    #         b.to_bytes(1, 'big').decode('utf-8')
    #     return True
    # except Exception:
    #     return False

    def check(num):
        mask = 1 << (8 - 1)  # 10000000
        i = 0
        while num & mask:  # 11000110 & 100000
            mask >>= 1
            i += 1
        return i

    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            cur = check(data[i])
            if cur != 1:
                return False
            i += 1
    return True


if __name__ == "__main__":
    """
    Main file for testing
    """

    validUTF8 = __import__('0-validate_utf8').validUTF8

    data = [65]
    print(validUTF8(data))  # True

    data = [80, 121, 116, 104, 111, 110, 32, 105,
            115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
    data = []
    print(validUTF8(data))  # False
