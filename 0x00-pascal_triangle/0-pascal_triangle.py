#!/usr/bin/python3


"""Algorithm for pascal triangle"""

# Factorials dict for memoization and performance
factorials = {}


def fact(n):
    """Calculates the factorial of a number"""
    if factorials.get(n, None):
        return factorials.get(n)
    if n <= 1:
        return 1

    factorials[n] = n * fact(n - 1)
    return factorials[n]


def coefficient(n, k):
    """Calculates the coefficient of position k with power n"""
    return fact(n) // (fact(k) * fact(n - k))


def coefficients(n):
    """Returns an array of coefficients in a degree n"""
    if n < 1:
        return [1]

    result = []
    for i in range(n + 1):
        result.append(coefficient(n, i))

    return result


def pascal_triangle(n):
    result = []
    for i in range(n):
        result.append(coefficients(i))

    return result
