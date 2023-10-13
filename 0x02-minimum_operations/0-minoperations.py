#!/usr/bin/python3

"""Solving minimum operations task."""
from math import sqrt


def is_prime(n):
    """
    Determines whether n is a prime number
    :param n: (int)
    :return: (tuple) first element True of False determing wether the number
    is prime or not, second element is the lowest factor of the number
    """
    if n <= 3:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, round(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def minOperations(n):
    """You can execute only two operations in this file: Copy All and Paste.
    this method calculates the fewest number of operations needed to result in
    exactly n H characters in a file"""

    if n <= 1:
        return 0

    if is_prime(n):
        return n

    h_count = 1
    adder = 0
    count = 0
    while h_count < n:
        if n % h_count == 0:
            adder = h_count
            h_count += adder
            count += 2
        else:
            h_count += adder
            count += 1

    return count
