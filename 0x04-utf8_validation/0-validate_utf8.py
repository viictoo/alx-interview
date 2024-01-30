#!/usr/bin/python3
""" validate a data set for consistency with utf8 encoding"""
from typing import List


def validUTF8(data: List) -> bool:
    """ a pythonic solution for determining is the first
    bits are in the correct sequence for valid utf8 encoding
    Returns:
        boolean: True if valid utf8 otherwise false
    """
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
    if len(data) > 0:
        try:
            for b in data:
                if type(b) is not int:
                    return False
                b.to_bytes(1, 'big').decode('utf-8')
            return True
        except Exception:
            return False
    return False


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
    data = ['a']
    print(validUTF8(data))  # False
