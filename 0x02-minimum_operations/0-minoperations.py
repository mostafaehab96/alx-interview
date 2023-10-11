#!/usr/bin/python3

"""Solving minimum operations task."""
from math import sqrt


def prime_factor(n):
    """
    Determines whether n is a prime number
    :param n: (int)
    :return: (tuple) first element True of False determing wether the number
    is prime or not, second element is the lowest factor of the number
    """
    if n <= 3:
        return True, 1

    if n % 2 == 0:
        return False, 2

    for i in range(3, round(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False, i

    return True, 1


def minOperations(n, i=0):
    """You can execute only two operations in this file: Copy All and Paste.
    this method calculates the fewest number of operations needed to result in
    exactly n H characters in a file"""

    if n <= 0:
        return 0

    check_n = prime_factor(n)
    if check_n[0]:
        return n
    lowest_factor = check_n[1]

    if prime_factor(n // lowest_factor)[0]:
        return lowest_factor + ((n - lowest_factor) // lowest_factor) + 1 + i
    else:
        return minOperations(n // lowest_factor, i + 1) + 1
