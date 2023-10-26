#!/usr/bin/python3

"""Module that defines a validUTF8 function."""

from typing import List


def validUTF8(data: List) -> bool:
    """
    :param data: a list of integers representing characters
    :return: True if all characters are utf8 valid, False otherwise
    """
    for num in data:
        if num in range(0, 128):
            return True
        binary = bin(num)[2::]
        if num in range(128, 2028) and binary[:3] != '110':
            return False
        if num in range(2048, 65536) and binary[:4] != '1110':
            return False
        if num in range(65536, 1114112) and binary[:5] != '11110':
            return False

        return True
